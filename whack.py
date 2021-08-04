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
  
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.count = 60
    
    Button(frame, text = 'Start Game',
          command = self.runGame,
          font = ("Times", "20"),
          width = 10,
          height = 4,
          fg = 'DarkOliveGreen4').grid(row = 6, column = 0)
    Button(frame, text = 'Help',
          command = self.showHelpMenu,
          font = ("Times", "20"),
          width = 10,
          height = 4,
          fg = 'DarkOliveGreen4').grid(row = 6, column = 1)
    Button(frame, text = 'Get Score',
          command = self.show_score,
          font = ("Times", "20"),
          width = 10,
          height = 4,
          fg = 'DarkOliveGreen4').grid(row = 6, column = 2)
    Button(frame, text = 'Exit Game',
          command = self.cleanPi,
          font = ("Times", "20"),
          width = 10,
          height = 4,
          fg = 'DarkOliveGreen4').grid(row = 6, column = 3)
    
     
    def show_score(self):
      window = Tk()
      window.title( ' Your Score! ')
      window.geometry('675x150+325+325')
      
			Label(window, text = ' Your Score is {}! Play Again?'.format(self.score),
            font = ("Times", "40"),
            bg = 'DarkOliveGreen4',
            fg = 'white').grid(row = 0, column = 1)
      Button(window, text = 'Exit',
            command = window.quit,
            font = ("Times", "12"),
            bg = 'DarkOliveGreen4',
            fg = 'white').grid(row = 2, column = 1)
      Button(window, text = 'Play Again!',
            command = window.destroy,
            font = ("Times", "12"),
            bg = 'DarkOliveGreen4',
            fg = 'white').grid(row = 3, column = 1)
      
			window.configure(background = 'DarkOliveGreen4')
      window.mainloop()
    
    def set_pin(self, pin_index, pin_state):
      moles = [0, 1, 2, 3]
			pins = [12, 16, 18]
			pin_led_states = [
				[1, 0, -1], #A
    		[0, 1, -1], #B
    		[-1, 1, 0], #C
    		[-1, 0, 1], #D
			]
			
			if pin_state == -1:
				GPIO.setup(self.pins[pin_index], GPIO.IN)
				else:
					GPIO.setup(self.pins[pin_index], GPIO.OUT)
					GPIO.output(self.pins[pin_index], pin_state)
					
		def light_led(self, led_number):
			for pin_index, pin_state in enumerate(self.pin_led_states[led_number]):
				self.set_pin(pin_index, pin_state)
		
		def cleanPi(self):
			GPIO.cleanup()
			root.quit()
			
		def quit(self):
			window.destroy()
			
		def showHelpMenu(self):
			#Display initial menu to player with options to begin game, learn how to play, or change difficulty
			window = Tk()
			window.title('Instructions')
			window.geometry('625x125+325+350')
			
			Label(window, text = "Here's how to play...",
						font = ("Times", "12"),
						background = 'DarkOliveGreen4',
						fg = 'white').grid(row = 0, column = 1)
			Label(window, text = "You have 1 minute to whack the buttons right under the light when it turns on.",
						font = ("Times", "12"),
						background = 'DarkOliveGreen4',
						fg = 'white').grid(row = 1, column = 1)
			Label(window, text = "Whack as many as you can! Good luck!",
						font = ("Times", "12"),
						background = 'DarkOliveGreen4',
						fg = 'white').grid(row = 2, column = 1)
			
			Button(window, text = "OK",
						command = window.destroy,
						font = ("Times", "12"),
						bg = 'DarkOliveGreen4',
						fg = 'white').grid(row = 3, column = 1)
			
			window.configure(background = 'DarkOliveGreen4')
			window.mainloop()
			
		def setStartTime(self, t):
			self.startTime = t
						
		def getStartTime(self):
			return self.startTime
		
		def setCurrentTime(self, t):
			self.currentTime = t
			
		def getCurrentTime(self):
			return self.currentTime
		
		def runGame(self):
			#Start game process
			#Inputs are button presses and time control
			#Outputs are light and feedback sound
			
			self.gameIsRunning = True
			
			t = threading.Thread(target = self.timeTracker)
			t.start()
			
			while(self.gameIsRunning):
				self.selectRandomMole()
				time.sleep(0.3)
				
		def selectRandomMole(self):
			led = random.choice(self.moles)
			
			self.light_led(led)
			self.currentMole(led)
			
			time.sleep(0.05)
			
			return self.currentMole
		
		def checkingPlayerWhack(self):
			#In a loop, check if input matches current mole
			GPIO.setmode(GPIO.BOARD)
			GPIO.setup(self.pins, GPIO.OUT)
			
			self.set_pin(0, -1)
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
