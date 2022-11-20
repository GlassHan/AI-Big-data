#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple client for GiGA Genie AI Makers Kit"""

from __future__ import print_function
from __future__ import absolute_import

import gkit
import time
import ex2_getVoice2Text as gv2t
import ex1_kwstest as kws
import math
import random
#from neopixel import *
from array import *
import argparse
import signal
import sys
import datetime
from socket import *
reload(sys)
sys.setdefaultencoding('utf-8')

def signal_handler(signal, frame):
        colorWipe(strip, Color(0,0,0))
        sys.exit(0)

def opt_parse():
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', action='store_true', help='clear the display on exit')
        args = parser.parse_args()
        if args.c:
                signal.signal(signal.SIGINT, signal_handler)

#LED strip configuration:
LED_COUNT      = 60      # Number of LED pixels.
LED_PIN        = 31      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

#Define functions which animate LEDs in various ways.
#def SetAll(strip, color):
#    """Wipe color across display a pixel at a time."""
#    for i in range(strip.numPixels()):
 #       strip.setPixelColor(i, color)


    
def sample():
    KWSID = ['기가지니', '지니야', '친구야', '자기야']
    while 1:
	    recog=kws.test(KWSID[1])
	    if recog == 200:
                    text = gv2t.getVoice2Text()
                    on='스탠드 켜'
                    if(on in text):
                            print('on')
                            return 5
                            #led = gkit.get_led()
                            #led.set_state(gkit.LED.ON)
                            
                    off='스탠드 꺼'
                    if(off in text):
                            print('off')
                            return 6
                            #led = gkit.get_led()
                            #led.set_state(gkit.LED.OFF)
                            
		    study='공부 모드'
		    if(study in text):
                            print('공부모드')
                            return 2
                            #SetAll(strip, color(green))
                            
                    computer='컴퓨터 모드'
		    if(computer in text):
                            print('컴퓨터모드')
                            return 3
                            #SetAll(strip, color(blue))
                            
                    rest='휴식 모드'
		    if(rest in text):
                            print('휴식모드')
                            return 4
                            #SetAll(strip, color(blue))
                                        rest='휴식 모드'
		    if(rest in text):
                            print('Automode')
                            return 0
                            #SetAll(strip, color(blue))
                                            rest='휴식 모드'
		    if(rest in text):
                            print('Manualmode')
                            return 1
                            #SetAll(strip, color(blue))      
	    else:
		    print('KWS Not Dectected ...')
    

   
def main():
    #serverSock = socket(AF_INET, SOCK_STREAM)
    #.bind(('', 8081))
    #serverSock.listen(1)

    #connectionSock, addr = serverSock.accept()

    #print(str(addr),'에서 접속이 확인되었습니다.')

    #data = connectionSock.recv(1024)
    #print('받은 데이터 : ', data.decode('utf-8'))

    test = str(sample())
    #connectionSock.send(test.encode('utf-8'))
    print('메시지를 보냈습니다.')

if __name__ == '__main__':
    main()
