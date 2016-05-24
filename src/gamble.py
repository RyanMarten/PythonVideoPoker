#COPYRIGHT 2016 RYAN MARTEN
'''Program Description: 
Contains class Gamble, which controls the graphical elements and variables that relate to betting in a video poker game. 
Gamble contains the follow methods: draw, undraw, setActive, setInactive, updateBalanceGraphics, isClicked, validBet, and winnings. 
With these you can control the visibility of the elements, set how they react to clicks, 
display the current balance, display if a bet is invalid, and return the winnings from the round. 
'''
from button import * 
from graphics import *
import math
class Gamble(object):

	def __init__(self):
		'''Gamble consists of a button, title, entry box, balance, and invalid message. The default initial balance is 500 gold'''
		self.betButton = Button(Point(445,465), "Bet")
		self.betTitle = Text(Point(445,335), "My Bet")
		self.balance = 500
		chars = math.floor(math.log(self.balance,10))
		self.balanceValue = Text(Point(555-chars*5,20), str(self.balance))
		self.balanceImage = Image(Point(580,20),"gold.gif")
		self.betEntry = Entry(Point(445,390),10)
		self.betEntry.setSize(20)
		self.invalidBetLable = Text(Point(445,420),"That is an invalid bet")
		self.invalidBetLable.setTextColor("red")
		self.invalidBetLable.setSize(10)
		self.valid = True

	def draw(self, window):
		'''Displays the button, balance, entry, and title in a window'''
		self.window = window
		self.betButton.draw(self.window)
		self.balanceValue.draw(self.window)
		self.balanceImage.draw(self.window)
		self.betEntry.draw(self.window)
		self.betTitle.draw(self.window)

	def undraw(self):
		'''Removes all graphical elements from the window it was drawn in'''
		self.betButton.undraw()
		self.balanceValue.undraw()
		self.balanceImage.undraw()
		self.betTitle.undraw()
		self.betEntry.undraw()
		if not self.valid:
			self.invalidBetLable.undraw()
			self.valid = True

	def setActive(self):
		'''Makes the bet button clickable and bet submittable'''
		self.betButton.setActive()

	def setInactive(self):
		'''Makes the bet button nonclickable and nonsubmittable'''
		self.betButton.setInactive()


	def updateBalanceGraphic(self): 
		'''Updates the value of the balance on the window'''
		if self.balance == 0:
			chars = 1
		else:	
			chars = math.floor(math.log(self.balance,10))
		self.balanceValue.undraw()
		self.balanceValue = Text(Point(555-chars*5,20), str(self.balance))
		self.balanceValue.draw(self.window)

	def isClicked(self, click):
		'''Detects whether the button has been clicked'''
		if self.betButton.isActive and self.betButton.isClicked(click):
			return True

	def validBet(self):
		'''Returns True if the bet is a positive integer that is less than the balance'''
		try:
			int(self.betEntry.getText())
		except ValueError:
			if self.valid:
				self.invalidBetLable.draw(self.window)
				self.valid = False
			return False
		else: 
			if 1 <= int(self.betEntry.getText())<= int(self.balanceValue.getText()):
				if not self.valid:
					self.invalidBetLable.undraw()
					self.valid = True
				self.bet = int(self.betEntry.getText())
				self.balance -= self.bet
				self.updateBalanceGraphic()
				self.betEntry.setText("")
				self.betButton.setInactive()
				return True
			else: 
				if self.valid:
					self.invalidBetLable.draw(self.window)
					self.valid = False
				return False

	def winnings(self, type, highcard):
		'''Returns winnings based on hand characteristics and bet amount'''
		if type == 9:
			winningAmount = 250*self.bet
		elif type == 8:
			winningAmount = 50*self.bet
		elif type == 7:
			winningAmount = 25*self.bet
		elif type == 6:
			winningAmount = 9*self.bet
		elif type == 5:
			winningAmount = 6*self.bet
		elif type == 4:
			winningAmount = 4*self.bet
		elif type == 3:
			winningAmount = 3*self.bet
		elif type == 2:
			winningAmount = 2*self.bet
		elif type == 1 and highcard >10:
			winningAmount = self.bet
		else:
			winningAmount = 0
		self.balance += winningAmount
		self.updateBalanceGraphic()
		return winningAmount

#Test Code
if __name__ == "__main__":
	win = GraphWin("gamble class test", 600, 500)
	betting = Gamble()
	betting.draw(win)
	for i in range(3):
		click = win.getMouse()
		if betting.isClicked(click):
			betting.validBet()
	betting.setInactive()
	if betting.isClicked(win.getMouse()):
		print "ERROR: This shouldn't show up"
	betting.setActive()
	for i in range(3):
		click = win.getMouse()
		if betting.isClicked(click):
			betting.validBet()
	betting.bet = 2
	print betting.winnings("Straight Flush", 14), '= 500'
	print betting.winnings("Straight Flush", 5), '= 100'
	print betting.winnings("Four of a kind", 1), '= 50'
	print betting.winnings("Full House", 11), '= 18'
	print betting.winnings("Flush", 4), '= 12'
	print betting.winnings("Straight", 13), '= 8'
	print betting.winnings("Three of a kind", 9), '= 6'
	print betting.winnings("Two pair", 6), "= 3"
	print betting.winnings("Pair", 11), "= 2"
	print betting.winnings("Pair", 3), "= 0"
	betting.undraw()
	win.getMouse()
