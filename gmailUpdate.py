#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import gmail

SDI   = 11
RCLK  = 12
SRCLK = 13

hexDec = [

	0x06, #1
	0x5b, #2
	0x4F, #3
	0x66, #4
	0x6d, #5
	0x7d, #6
	0x07, #7
	0x7f, #8
	0x67, #9
	0x3f, #0
	0x6d, #S
	0x39, #C
	0x77, #A
	0x54, #n
]

def printMessage():	#Console telling user program is running
	print "Running script"

def GPIOsetup(): #Naming locations
	GPIO.setmode(GPIO.BOARD) 
	GPIO.setup(SDI, GPIO.OUT)
	GPIO.setup(RCLK, GPIO.OUT)
	GPIO.setup(SRCLK, GPIO.OUT)
	GPIO.output(SDI, GPIO.LOW)
	GPIO.output(RCLK, GPIO.LOW)
	GPIO.output(SRCLK, GPIO.LOW)

def hc595_shift(dat):	#Shift register
	for bit in range(0, 8):
		GPIO.output(SDI, 0x80 & (dat << bit))
		GPIO.output(SRCLK, GPIO.HIGH)
		time.sleep(0.001)
		GPIO.output(SRCLK, GPIO.LOW)
	GPIO.output(RCLK, GPIO.HIGH)
	time.sleep(0.001)
	GPIO.output(RCLK, GPIO.LOW)

g = gmail.login('USERNAME', 'PASSWORD')
unreadMessages = g.inbox().mail(unread=True)
totalMessages = 0

for message in unreadMessages:

       totalMessages += 1

print("Number of Emails: " + str(totalMessages))

def update(): #Displays SCAn before updating number of emails

	hc595_shift(segCode[10])
	time.sleep(0.5)
	hc595_shift(segCode[11])
	time.sleep(0.5)
	hc595_shift(segCode[12])
	time.sleep(0.5)
	hc595_shift(segCode[13])
	time.sleep(0.5)

def emails():

    if totalMessages == 0:

        hc595_shift(segCode[9])

	elif totalMessages == 1:

		hc595_shift(segCode[0])

	elif totalMessages == 2:

		hc595_shift(segCode[1])

	elif totalMessages == 3:

        hc595_shift(segCode[2])

    elif totalMessages == 4:

        hc595_shift(segCode[3])

    elif totalMessages == 5:

        hc595_shift(segCode[4])

    elif totalMessages == 6:

        hc595_shift(segCode[5])

    elif totalMessages == 7:

        hc595_shift(segCode[6])

    elif totalMessages == 8:

        hc595_shift(segCode[7])

    elif totalMessages == 9:

        hc595_shift(segCode[8])

	elif totalMessges == 0:

		hc595_shift(segCode[9])

GPIO.setwarnings(False)

if __name__ == '__main__': #Runs script

	printMessage()
	GPIOsetup()

	try:

		update()
		emails()

	except KeyboardInterrupt:

		GPIO.cleanup()
