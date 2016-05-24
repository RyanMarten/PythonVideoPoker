#COPYRIGHT 2016 RYAN MARTEN
'''Program Description: 
Deals hands and report the type and high card of the hand graphically. 
This loops again and again, each time from a new shuffled Deck. 
"Deal" and "Quit" buttons let the player continue or end gracefully.
The user can discard any or all of his cards to try to improve his hand once.  
All discards are made, and then replaced with that many new cards from the deck 
The user can't decide whether or not to discard again after an initial discard. 
The player is given some number of dollars, he can specify how many to bet.  
After discarding and drawing (if desired), he wins an amount multipled by his bet based off hand type.
The balance is kept track of on the screen - if it hits 0, the user is told the game is over, but he can play again.
Creates the file 'topten.txt' (in the same directory as your program) to record and display the top 10 winning amounts 
and a separate list for the best hand. This file is created if it doesn't exist, and read and modified.  
The user can add their name to the list as soon as her current winnings qualify her and/or 
best hand; their doesn't have to quit the game.  If her winnings continue to increase more, and/or she gets an even better 
hand, she moves up the list(s), but if they drop, she stays in her highest position.  Hint: use a fixed length line for 
each entry in the file.

'''
from graphics import *
from deck import *
from gameover import *
from scoringsheet import *
from player import *
from gamble import *
from button import *
from highscore import *
import time

class windowControl(object):
	def __init__(self, window):
		'''Creates graphic objects and draws them to the window'''
	
		self.window = window
		
		self.instructions = Text(Point(300, 20), "Enter a betting amount to get started")
		self.instructions.draw(self.window)

		self.quitButton = Button(Point(60,20),"Quit")
		self.quitButton.draw(self.window)

		self.gameover = GameOver()

		self.scoringsheet = ScoringSheet()
		self.scoringsheet.draw(self.window)

		self.mycards = Player("My")
		self.mycards.draw(self.window)

		self.mybet = Gamble()
		self.mybet.draw(self.window)

		self.highscore = HighScore()

	def respondInput(self,click):
		'''Takes a window and a point where the mouse has been click and changes the window based on where the click was. 
		Returns False if click should close window and True if window should be kept open'''
		if  self.quitButton.isClicked(click):
			return False
		else: 
			#If the click is in the Bet button area and its a valid bet, deal a hand and display its information
			if self.mybet.isClicked(click):	
				if self.mybet.validBet():
					self.deck = Deck()
					self.deck.shuffle()
					self.mycards.dealHand(self.deck)
					self.scoringsheet.unHighlightScores()
					self.instructions.setText("Select all, some, or none cards to discard")
			#If the click is in the Discard area (if its on a card toggle selecting it) discard and give winnings
			elif self.mycards.isClicked(click):
				self.mycards.discard(self.deck)
				type = self.mycards.type
				highcard = self.mycards.highcard
				#calculate winnings based off of bet amount
				winningAmount = self.mybet.winnings(type,highcard)
				#gameover if gold reaches zero
				if self.mybet.balance == 0:
					self.instructions.setText("You lost %s gold" %(str(self.mybet.bet)))
					time.sleep(1)
					self.mybet.undraw()
					self.gameover.draw(self.window)
					self.quitButton.undraw()
					self.quitButton = Button(Point(250,300), "Quit")
					self.quitButton.draw(self.window)
					self.mybet.setInactive()
				#tell the user what they have won
				else:
					if winningAmount > 0:
						self.scoringsheet.highlightScore(type, highcard)
						self.instructions.setText("You have won %s gold!" %(str(winningAmount-self.mybet.bet)))
					else:
						self.instructions.setText("You lost %s gold" %(str(self.mybet.bet)))
					self.mybet.setActive()
					#see if the balance or hand qualifies as a highscore, and add it if it does
					self.highscore.isTopScore(self.mybet.balance) 	
					self.highscore.isTopHand(self.mycards.hand, type, highcard)
			#if the gameover screen is up and playagain button is clicked, reset the game
			elif self.gameover.isClicked(click):
				self.quitButton.undraw()
				self.gameover.undraw()
				self.quitButton = Button(Point(60,20),"Quit")
				self.quitButton.draw(self.window)
				self.mybet.balance = 500
				self.mybet.draw(self.window)
				self.mybet.updateBalanceGraphic()
				self.mybet.setActive()
				self.instructions.setText("Enter a betting amount to get started")
				self.mycards.reset()
				self.highscore = HighScore()
			return True 




if __name__ == "__main__":
	#Draws the user interface on a window
	win = GraphWin('Video Poker',600,500)

	#Updates the window or closes the window based on where the user clicks
	control = windowControl(win)
	click = win.getMouse()
	while control.respondInput(click):
		click = win.getMouse()