# !/usr/bin/env python
# coding: latin-1
# Autor:   Ingmar Stapel
# Datum:   20170723
# Version:   1.0
# Homepage:   http://custom-build-robots.com

import smbus
import time
import subprocess
import os

dev = smbus.SMBus(1)
os.system('clear')
 
print('---------------------------------------------------------')
print('Searching for i2c devices...')
time.sleep(0.5)
print('This are the devices which are available:')
print('---------------------------------------------------------')
output = subprocess.check_output("i2cdetect -y 1", shell=True)
output = output.decode("utf-8")
print(output)
print('---------------------------------------------------------')
print('Now you could change the sensor I2C address.')
print('---------------------------------------------------------')

try:
   addressOld = input("The actual sensor address:")
   addressNew = input("The new sensor address:") 
except ValueError: 
   sys.exit()

print('---------------------------------------------------------')
print('Checking if the new address could be used')
addressOld = int(addressOld, 16)
addressNew = int(addressNew, 16)

if addressNew in range(3, 120):

   time.sleep(0.5)
   print('Changing the sensor I2C address...')
   print('---------------------------------------------------------')

   addressNew = addressNew << 1
   dev.write_block_data(addressOld, 0xe0, [0xAA, 0xA5, addressNew])
   time.sleep(1)
   os.system('clear')
   print('---------------------------------------------------------')
   print('Searching for i2c devices...')
   time.sleep(0.5)
   print('This are the devices which are available:')
   print('---------------------------------------------------------')
   output = subprocess.check_output("i2cdetect -y 1", shell=True)
   output = output.decode("utf-8")
   print(output)
else:
   os.system('clear')
   print('---------------------------------------------------------')
