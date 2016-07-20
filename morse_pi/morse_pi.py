#!/usr/bin/python
import RPi.GPIO as GPIO
import fileinput
import time
import os

PIN_NUMBER = 14

ALPHABET = {
	"A" : ".-",
	"B" : "-...",
	"C" : "-.-.",
	"D" : "-..",
	"E" : ".",
	"F" : "..-.",
	"G" : "--.",
	"H" : "....",
	"I" : "..",
	"J" : ".---",
	"K" : "-.-",
	"L" : ".-..",
	"M" : "--",
	"N" : "-.",
	"O" : "---",
	"P" : ".--.",
	"Q" : "--.-",
	"R" : ".-.",
	"S" : "...",
	"T" : "-",
	"U" : "..-",
	"V" : "...-",
	"W" : ".--",
	"X" : "-..-",
	"Y" : "-.--",
	"Z" : "--..",
	" " : "/"
}

DOT_TIME = 0.2
DASH_TIME = 0.8

SIGN_SPACE = 0.5
LETTER_SPACE = 0.8
WORD_SPACE = 1.2

def turn_diode_on_for(interval):
	GPIO.output(PIN_NUMBER,GPIO.HIGH)
	os.system('play --no-show-progress --null --channels 1 synth {0} sine 2500'.format(interval))
	GPIO.output(PIN_NUMBER, GPIO.LOW)

def message_start():
	for i in range(0,10):
		turn_diode_on_for(0.1)
		time.sleep(0.1)

def play_in_morse(msg):
        
        for letter in msg:
                for sign in ALPHABET[letter]:
                        if sign == ".":
                                turn_diode_on_for(DOT_TIME)
                        if sign == "-":
                                turn_diode_on_for(DASH_TIME)
                        time.sleep(SIGN_SPACE)
                time.sleep(SIGN_SPACE * 2) #  Letter space is 3x SIGN_SPACE
                if letter == " ":
                        time.sleep(SIGN_SPACE * 2) #  Word space is 5x SIGN_SPACE

def main():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(PIN_NUMBER, GPIO.OUT)
	
	messages = []
	for line in fileinput.input():
		messages.append(line.rstrip())

	msg = " ".join(messages)

	while True:
		message_start()
		time.sleep(1)
		play_in_morse(msg.upper())

main()
