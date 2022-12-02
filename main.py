import errno
# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/
#120

import time
import threading
from threading import Thread
import logging
import RPi.GPIO as GPIO

from server import *
from time import sleep
import math
stop_threads = True
in1 = 11
in2 = 13
in3 = 15
in4 = 16
in31 = 31
in33 = 33
temp1 =1
x = b'z'
distanceFront = 0

#GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#print(mode)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.output(in1 ,GPIO.LOW)
GPIO.output(in2 ,GPIO.LOW)

GPIO.setup(in31,GPIO.OUT)
GPIO.setup(in33,GPIO.OUT)
GPIO.output(in31 ,GPIO.LOW)
GPIO.output(in33 ,GPIO.LOW)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.output(in3 ,GPIO.LOW)
GPIO.output(in4 ,GPIO.LOW)


        # set GPIO Pins
GPIO_TRIGGER = 12
GPIO_ECHO = 24

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


#if (GPIO.input(16)):
#  print("good")

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.HIGH)
GPIO.output(in3, GPIO.LOW)

eventMode = threading.Event()
eventMode.clear()

def distance():
    #threading.Timer(2.0,distance).start()
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()

            # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()

            # time difference between start and arrival
            TimeElapsed = StopTime - StartTime
            # multiply with the sonic speed (34300 cm/s)
            # and divide by 2, because there and back
            distance = (TimeElapsed * 34300) / 2
            #print(distance)
    return distance

def test():
    threading.Timer(2.0,test).start()
    global distanceFront
    distanceFront = distance()
   # print(distanceFront)


def recoitCom():
    global x
    global eventMode
    while(True):
        x = recv_input()
        if(x != b'o'):
            eventMode.clear()
        if(x == b'o'):
            eventMode.set()

def manuel():
    #t_auto = threading.Thread(target=automatique())
    global x
    global eventMode
    while True:
        if (eventMode.is_set() is False):
                #x = recv_input()
                dist = distance()
                print("Measured Distance = %.1f cm" % dist)
                time.sleep(1)
                if x == b'r':
                    stop_threads = True
                    print("run")
                    if (temp1 == 1):
                        GPIO.output(in1, GPIO.LOW)
                        GPIO.output(in2, GPIO.HIGH)
                        GPIO.output(in3, GPIO.LOW)

                        x = b'z'
                    else:
                        GPIO.output(in1, GPIO.LOW)
                        GPIO.output(in2, GPIO.HIGH)
                        GPIO.output(in3, GPIO.LOW)

                        print("backward")
                        x = b'z'


                elif x == b'q':
                    stop_threads = True
                    print("stop")

                    # changer les pins ici pour mettre le signal a 2.5 volt (qui est notre neutre)
                    GPIO.output(in1, GPIO.LOW)
                    GPIO.output(in2, GPIO.HIGH)
                    GPIO.output(in3, GPIO.LOW)
                    # GPIO.output(in4, GPIO.LOW)
                    x = b'z'

                elif x == b's':
                    stop_threads = True
                    print("backward")

                    GPIO.output(in1, GPIO.HIGH)
                    GPIO.output(in2, GPIO.HIGH)
                    GPIO.output(in3, GPIO.HIGH)
                    # GPIO.output(in4, GPIO.HIGH)

                    # GPIO.output(in4, GPIO.LOW)

                    x = b'z'

                elif x == b'w':
                    stop_threads = True
                    print("forward")

                    GPIO.output(in1, GPIO.LOW)
                    GPIO.output(in2, GPIO.LOW)
                    GPIO.output(in3, GPIO.LOW)
                    # GPIO.output(in4, GPIO.HIGH)
                    # temp1 = 0

                    x = b'z'

                elif x == b'a':
                    stop_threads = True
                    print("left")
                    #GPIO.output(in1, GPIO.LOW)
                    #GPIO.output(in2, GPIO.LOW)
                    #GPIO.output(in3, GPIO.HIGH)
                    GPIO.output(in31, GPIO.HIGH)
                    GPIO.output(in33, GPIO.LOW)

                    x = b'z'



                elif x == b'd':
                    stop_threads=True
                    print("right")

                    #GPIO.output(in1, GPIO.LOW)
                    #GPIO.output(in2, GPIO.HIGH)
                    #GPIO.output(in3, GPIO.LOW)
                    GPIO.output(in31, GPIO.LOW)
                    GPIO.output(in33, GPIO.HIGH)

                    x = b'z'
                elif x == b'd':
                    stop_threads = True
                    print("right")

                    # GPIO.output(in1, GPIO.LOW)
                    # GPIO.output(in2, GPIO.HIGH)
                    # GPIO.output(in3, GPIO.LOW)
                    GPIO.output(in31, GPIO.LOW)
                    GPIO.output(in33, GPIO.HIGH)

                elif x == b'o':


                    print("manuel changement vers auto")

                    #t_auto.join()

                    x = b'z'
                    '''while (x!=b'o'):
                        x = recv_input()
                        print'''

                elif x == b'e':
                    stop_threads = True
                    GPIO.cleanup()
                    print("GPIO Clean up")
                    break

    print('sortie whileManu')

def commande():

    try:
        # x = toBinary(input())
        global x
        x = recv_input()

    except socket.error as error:
        err = error.args[0]
        if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
            sleep(1)
            print('pas de valeur envoyer')
        x = "invalide"

        # else:
        # print(error)

def automatique():

        global eventMode

        print("on est rendu en auto")
        print(eventMode.is_set())
        while True:
            if (eventMode.is_set() is True):

                dist = distance()
                time.sleep(1)
                print("auto :Measured Distance = %.1f cm" % dist)
                if 100 >= dist:
                    # elif x == b't':
                    # forward a environ 40%
                    print("backward 40%")
                    GPIO.output(in1, GPIO.LOW)
                    GPIO.output(in2, GPIO.LOW)
                    GPIO.output(in3, GPIO.HIGH)
                elif 100 < dist:
                    # elif x == b'y':
                    print("forward a environ 40%")
                    GPIO.output(in1, GPIO.HIGH)
                    GPIO.output(in2, GPIO.LOW)
                    GPIO.output(in3, GPIO.LOW)
                else:
                    print("unlucky")


# https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/


test()
initialisation()

t1 = threading.Thread(target=recoitCom)
t2 = threading.Thread(target=manuel)
t3 = threading.Thread(target=automatique)

t1.start()
t2.start()
t3.start()


#threading.Thread(target=commande(),args=(1,)).start()
#t1 = threading.Thread(target=manuel())
#t1.start()

#input = t1.join(timeout=1)

#t2 = threading.Thread(target=automatique(), args=input)