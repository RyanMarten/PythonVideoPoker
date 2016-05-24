#COPYRIGHT 2016 RYAN MARTEN
'''Program Description: 
Contains class Player, which controls the graphical elements and variables that relate to a players cards in a video poker game. 
Player contains the follow methods: draw, undraw, dealHand, isClicked, discard, updateValues, and reset. 
With these, you can control the visibility and values/appearances of the elements.
This class uses the Hand class to evaluate the type of poker hand and the Deck class to add cards to the hand. 
'''
from button import * 
from graphics import *
from hand import *
from deck import *

class Player(object):

	def __init__(self, playerName):
		'''Player consists of a title, type/highcard value and lable, hand, and a button'''
		#Default hand drawn is 5 flipped over cards
		self.playerTitle = Text(Point(155,335), "%s Hand" %(playerName))
		self.hand = Hand(['b','b','b','b','b'])
		self.typeLable = Text(Point(105,375),"Type: ")
		self.typeValue = Text(Point(205,375),"None")
		self.highcardLable = Text(Point(105,400),"Highcard: ")
		self.highcardValue = Text(Point(205,400),"None")
		self.discardButton = Button(Point(155,465),"Discard")
		self.discardButton.setInactive()
		self.isDrawn = False
		
	def draw(self, window):
		'''Displays the title, hand, button, lables/values on a window'''
		self.window = window
		self.playerTitle.draw(self.window)
		self.hand.draw(self.window)
		self.discardButton.draw(self.window)
		self.highcardLable.draw(self.window)
		self.highcardValue.draw(self.window)
		self.typeLable.draw(self.window)
		self.typeValue.draw(self.window)
		self.isDrawn = True

	def undraw(self):
		'''Removes all graphical elements from the window'''
		self.playerTitle.undraw()
		self.discardButton.undraw()
		self.highcardLable.undraw()
		self.highcardValue.undraw()
		self.typeLable.undraw()
		self.typeValue.undraw()
		self.hand.undraw()
		self.isDrawn = False

	def dealHand(self, deck):
		'''Deals 5 cards, displays them on the window, and updates type and highcard charactistics'''
		self.hand.undraw()
		self.hand = Hand(deck.deal(5))
		self.hand.draw(self.window)
		self.highcard = self.hand.highCard()
		self.type = self.hand.handType()
		self.updateValues()
		self.discardButton.setActive()

	def isClicked(self, click):
		'''Returns whether the button has been clicked. If the hand is clicked, toggles selection of the card'''
		if self.discardButton.isActive and self.discardButton.isClicked(click):
		 	return True
		elif self.hand.isDrawn and self.discardButton.isActive: 
			self.hand.isClicked(click)
			return False

	def discard(self,deck):
		'''Removes selected cards from the hand and replaces them from cards from a deck, updating the graphics'''
		#When discard is clicked, remove the cards from window and replace them with new cards from the deck
		self.discardButton.setInactive()
		self.hand.discard(deck)
		self.hand.undraw()
		self.hand.draw(self.window)
		#update the highcard and type values
		self.highcard = self.hand.highCard()
		self.type = self.hand.handType()
		self.updateValues()		

	def updateValues(self):
		'''Updates type/highcard values on the window'''
		self.highcardValue.setText(self.hand.highcardConversion(self.highcard))
		self.typeValue.setText(self.hand.typeConversion(self.type))

	def reset(self):
		'''Draws a hand of flipped over cards and resets type and highcard to none'''
		self.undraw()
		self.hand = Hand(['b','b','b','b','b'])
		self.type = "None"
		self.highcard = "None"
		self.updateValues()
		self.draw(self.window)

#Test Code
if __name__ == "__main__":
	win = GraphWin("player class test", 600, 500)
	mydeck = Deck()
	player1 = Player("Player1")
	player1.draw(win)
	player1.dealHand(mydeck)

	for i in range(10):
		click = win.getMouse()
		if player1.isClicked(click):
			player1.discard(mydeck)
			win.getMouse()
			player1.reset()
			win.getMouse()
			player1.dealHand(mydeck)


	player1.undraw()
	win.getMouse()