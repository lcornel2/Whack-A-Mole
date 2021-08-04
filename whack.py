from Tkinter import *
import sys
import time
import random
import RPi.GPIO as GPIO
import threading

class Whack:
  moles = [0, 1, 2, 3]
  currentMole = -1
  #boolean value signifies state of game
  gameIsRunning = False 
  #start and end times will get/set in threads
  startTime = 0
  currentTime = 0
  score = 0
  
  GPIO.setmode(GPIO.BOARD)
  
  pins = [12, 16, 18]
  pin_led_states = [
    [1, 0, -1], #A
    [0, 1, -1], #B
    [-1, 1, 0], #C
    [-1, 0, 1], #D
  ]
  
  
