
# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import os
import time
import RPi.GPIO as GPIO
from time import sleep


in1 = 11
in2 = 13
in3 = 15
in4 = 18
temp1 =1

#GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#print(mode)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.output(in1 ,GPIO.LOW)
GPIO.output(in2 ,GPIO.LOW)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.output(in3 ,GPIO.LOW)
GPIO.output(in4 ,GPIO.LOW)

#if (GPIO.input(16)):
#  print("good")

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")

while (1):

    x = input()

    if x == 'r':
        print("run")
        if (temp1 == 1):
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.HIGH)
            GPIO.output(in3, GPIO.LOW)

            x = 'z'
        else:
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.HIGH)

            print("backward")
            x = 'z'


    elif x == 'q':
        print("stop")

        #changer les pins ici pour mettre le signal a 2.5 volt (qui est notre neutre)
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.HIGH)
        GPIO.output(in3, GPIO.LOW)
        #GPIO.output(in4, GPIO.LOW)
        x = 'z'

    elif x == 'w':
        print("forward")

        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.HIGH)
        GPIO.output(in3, GPIO.HIGH)
        #GPIO.output(in4, GPIO.HIGH)

        #GPIO.output(in4, GPIO.LOW)

        x = 'z'

    elif x == 's':
        print("backward")

        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        #GPIO.output(in4, GPIO.HIGH)
        #temp1 = 0

        x = 'z'

    elif x == 'a':
        print("left")
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.HIGH)

        x = 'z'



    elif x == 'd':
        print("right")

        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        GPIO.output(in3, GPIO.LOW)

        x = 'z'



    elif x == 't':
        #forward a environ 40%
        print("forward 40%")
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.HIGH)

    elif x == 'y':
        #backward a environ 40%
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)


    elif x == 'e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")



        # set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)



#https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/

def distance():
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

    return distance


    if __name__ == '__main__':
            try:
                while True:
                    dist = distance()
                    print("Measured Distance = %.1f cm" % dist)
                    time.sleep(1)

                # Reset by pressing CTRL + C
            except KeyboardInterrupt:
                print("Measurement stopped by User")
                GPIO.cleanup()
