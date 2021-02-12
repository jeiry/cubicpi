import spidev as SPI
import ST7789
import time
import requests
import json
import os
from PIL import Image,ImageDraw,ImageFont
import threading
# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 24
bus = 0
device = 0

# 240x240 display with hardware SPI:
disp = ST7789.ST7789(SPI.SpiDev(bus, device),RST, DC, BL)

# Initialize library.
disp.Init()

# Clear display.
disp.clear()

fans = 0
fansChange = ''
def updateBFans():
    global fans
    global fansChange
    print('check bb')
    try:
        # 获取粉
        r = requests.get('https://api.bilibili.com/x/relation/stat?vmid=46891041')
        fans = r.json()['data']['follower']
        file = "blog.log"
        # 记录6小时内粉变动
        if os.path.exists(file):
            print('logs')
            with open(file, "r") as f:
                data = json.load(f)
            arr = []
            for obj in data:
                if obj['t']+3600*6 > int(time.time()):
                    arr.append(obj)
            arr.append({'t':int(time.time()),'f':fans})
            with open(file, "w+") as f:
                f.write(json.dumps(arr))
        else:
            with open(file, "w+") as f:
                f.write(json.dumps([{'t':int(time.time()),'f':fans}]))
        with open(file, "r") as f:
            data = json.load(f)
        countFans = data[len(data)-1]['f'] - data[0]['f']
        fansChange = '+%d'%countFans if countFans >=0 else '%d'%countFans
    except Exception as e:
        print(e)
if __name__ == '__main__':
    i = 0
    checkFans = 0
    while True:
        if checkFans == 0:
            t = threading.Thread(target=updateBFans, args=())  # 创建线程
            t.setDaemon(True)
            t.start()
        image1 = Image.new("RGBA", (disp.width, disp.height), "black")
        draw = ImageDraw.Draw(image1)
        # draw.text((90, 120), 'Electronic ', fill="white", font=font)
        draw.text((20, 40), time.strftime("%Y-%m-%d", time.localtime()) , fill="white", font=ImageFont.truetype("迷你简综艺.TTF", 34))
        draw.text((20, 80), time.strftime("%H:%M:%S", time.localtime()) , fill="white", font=ImageFont.truetype("迷你简综艺.TTF", 49))
        draw.text((105, 150), '%s'%fans, fill="#01b0ff",
                  font=ImageFont.truetype("迷你简综艺.TTF", 36))
        draw.text((105, 186), '%s'%fansChange, fill="#00ff12",
                  font=ImageFont.truetype("迷你简综艺.TTF", 30))
        btv = Image.open("btv.png")
        btv = btv.resize((74, 68))
        image1.paste(btv, box=(20, 150))
        image1 = image1.rotate(180)
        image1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
        disp.ShowImage(image1, 0, 0)
        time.sleep(1)
        i += 1
        checkFans += 1
        if checkFans == 60:
            checkFans = 0

