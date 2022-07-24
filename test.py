import OPi.GPIO as GPIO

import orangepi.pi4 as bd

BOARD = bd.BOARD

GPIO.setmode(BOARD)
GPIO.setup(5, GPIO.IN)
print(GPIO.input(5))