import os

#os.system('cd /home/pi/raspberrypi/i2c_cmd/bin')

os.system('cd /home/pi/raspberrypi/i2c_cmd/bin && ./veye_mipi_i2c.sh -w -f daynightmode -p1 0xFF -b 0') #color
os.system('cd /home/pi/raspberrypi/i2c_cmd/bin && ./veye_mipi_i2c.sh -w -f daynightmode -p1 0xFE -b 0') #color