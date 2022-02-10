#! /bin/bash
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.68.tar.gz
tar zxvf bcm2835-1.68.tar.gz 
cd bcm2835-1.68/
sudo ./configure && sudo make && sudo make check && sudo make install
sudo apt-get -y install wiringpi
wget https://project-downloads.drogon.net/wiringpi-latest.deb
sudo dpkg -i wiringpi-latest.deb
gpio -v
sudo apt-get -y install ttf-wqy-zenhei
sudo apt-get -y install python3-pip
sudo apt-get -y install libatlas-base-dev
sudo apt-get -y install libopenjp2-7
sudo apt-get -y install libtiff5
sudo pip3 install RPi.GPIO --timeout 1000
sudo pip3 install spidev --timeout 1000
sudo pip3 install numpy --timeout 1000
pip3 install Pillow
wget https://www.piwheels.org/simple/numpy/numpy-1.20.1-cp37-cp37m-linux_armv6l.whl
pip3 install numpy-1.20.1-cp37-cp37m-linux_armv6l.whl
wget https://www.piwheels.org/simple/pillow/Pillow-8.1.0-cp37-cp37m-linux_armv6l.whl
pip3 install Pillow-8.1.0-cp37-cp37m-linux_armv6l.whl
sudo apt-get install p7zip-full
wget http://www.waveshare.net/w/upload/b/bd/1.3inch_LCD_HAT_code.7z
7z x 1.3inch_LCD_HAT_code.7z -r -o./1.3inch_LCD_HAT_code
sudo chmod 777 -R 1.3inch_LCD_HAT_code
cd 1.3inch_LCD_HAT_code
cd c
make clean
make
