import RPi.GPIO as GPIO
import time
import argparse

description =   "Solenoid.py: This program is a simple way to control and toggle power to the pi's GPIO "\
"""             Pin 1 Pin2   <--   **Corner of board
           +3V3 [ ] [ ] +5V
 SDA1 / GPIO  2 [ ] [ ] +5V
 SCL1 / GPIO  3 [ ] [ ] GND
        GPIO  4 [ ] [ ] GPIO 14 / TXD0
            GND [ ] [ ] GPIO 15 / RXD0
        GPIO 17 [ ] [ ] GPIO 18
        GPIO 27 [ ] [ ] GND
        GPIO 22 [ ] [ ] GPIO 23
           +3V3 [ ] [ ] GPIO 24
 MOSI / GPIO 10 [ ] [ ] GND
 MISO / GPIO  9 [ ] [ ] GPIO 25
 SCLK / GPIO 11 [ ] [ ] GPIO  8 / CE0#
            GND [ ] [ ] GPIO  7 / CE1#
ID_SD / GPIO  0 [ ] [ ] GPIO  1 / ID_SC
        GPIO  5 [ ] [ ] GND
        GPIO  6 [ ] [ ] GPIO 12
        GPIO 13 [ ] [ ] GND
 MISO / GPIO 19 [ ] [ ] GPIO 16 / CE2#
        GPIO 26 [ ] [ ] GPIO 20 / MOSI
            GND [ ] [ ] GPIO 21 / SCLK
             Pin 39 Pin 40""" 

class SolenoidCtrl(object):
    def __init__(self):        
        self.parser = argparse.ArgumentParser(description=description, prefix_chars="-",formatter_class=argparse.RawTextHelpFormatter)    
        self.parser.add_argument("-p","-P","--pin",default=18,type=int, dest="gpiopin", help="GPIO # of pin desired to use, default GPIO 18")
        self.parser.add_argument("-t","-T","--ontime",default=3.0,type=float, dest="ontime",help="Time in seconds of how long to output power, default 3")
        self._args = self.parser.parse_args()
        self.powersolenoid(self._args.gpiopin, self._args.ontime)
    
    def powersolenoid(self, pin, ontime):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(pin,GPIO.OUT)
        print "GPIO {0:d} ON for {1:f}s".format(pin,ontime)
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(ontime)
        print "GPIO {0} OFF".format(pin)
        GPIO.output(pin,GPIO.LOW)


if __name__ == "__main__":
    SolenoidCtrl()
