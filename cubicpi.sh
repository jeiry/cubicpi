#! /bin/bash
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.68.tar.gz
tar zxvf bcm2835-1.68.tar.gz 
cd bcm2835-1.68/
sudo ./configure && sudo make && sudo make check && sudo make install
sudo apt-get install wiringpi
#对于树莓派2019年5月之后的系统（早于之前的可不用执行），可能需要进行升级：
wget https://project-downloads.drogon.net/wiringpi-latest.deb
sudo dpkg -i wiringpi-latest.deb
gpio -v
sudo apt-get install ttf-wqy-zenhei
sudo apt-get install python3-pip
sudo pip3 install RPi.GPIO
sudo pip3 install spidev
sudo apt-get install p7zip-full
wget http://www.waveshare.net/w/upload/b/bd/1.3inch_LCD_HAT_code.7z
7z x 1.3inch_LCD_HAT_code.7z -r -o./1.3inch_LCD_HAT_code
sudo chmod 777 -R 1.3inch_LCD_HAT_code
cd 1.3inch_LCD_HAT_code
cd c
make clean
make
sudo ./main
