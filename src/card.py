#COPYRIGHT 2016 RYAN MARTEN
'''Program Description: 
Contains class Card, which controls the graphical elements and variables that relate to card from a standard 52 card deck.
Card contains the follow methods: draw, undraw, setInactive, setActive, toggleActive, and isClicked.
'''
from graphics import *
class Card(object):
	'''Creates a graphical version of a card. Has two states: neutral and active. Detects clicks'''
	def __init__(self, cardName, centerpoint):
		'''Creates a card from a name creates a highlight box (default not visibile) and image'''
		self.name = cardName
		#gets card image from cards directory
		self.image = Image(centerpoint, '../cards/%s.gif'%(cardName))
		self.point1 = Point(centerpoint.getX() - 40, centerpoint.getY() - 52)
		self.point2 = Point(centerpoint.getX() + 40, centerpoint.getY() + 52)
		self.box = Rectangle(self.point1, self.point2)
		self.box.setWidth(0)
		self.isActive = False

	def draw(self, window):
		'''Draws the card image and to the window'''
		self.window = window
		self.image.draw(self.window)

	def undraw(self):
		'''Removes the card image and its highlight from the window'''
		self.image.undraw()
		self.box.undraw()

	def setInactive(self):
		'''Removes the highlight from the window'''
		self.box.undraw()
		self.isActive = False

	def setActive(self):
		'''Adds the highlight to the window'''
		self.image.undraw()
		self.box.undraw()
		self.box.setFill("Yellow")
		self.box.draw(self.window)
		self.image.draw(self.window)
		self.isActive = True

	def toggleActive(self):
		'''Makes the card active/inactive if the card is inactive/active'''
		if self.isActive:
			self.setInactive()
		else:
			self.setActive()

	def __repr__(self):
		'''Card is represented by its name and its state'''
		return  "Name: %s, Active: %s" %(self.name,self.isActive)

	def isClicked(self,click):
		'''Returns whether the card has been clicked'''
		if self.point1.getX() <= click.getX() <= self.point2.getX() and  self.point1.getY() <= click.getY() <= self.point2.getY():
			return True
		else: 
			return False

#Test Code
if __name__ == "__main__":
	win = GraphWin("card class test", 300,300)
	card1 = Card('ah', Point(60,100))
	card2 = Card('2d', Point(150,100))
	card3 = Card('tc', Point(240,100))
	card1.draw(win)
	card2.draw(win)
	card3.draw(win)
	for i in range(10):
		click = win.getMouse()
		if card1.isClicked(click):
			card1.toggleActive()
		elif card2.isClicked(click):
			card2.toggleActive()
		elif card3.isClicked(click):
			card3.toggleActive()
		print card1, card2, card3
	card1.undraw()
	card2.undraw()
	card3.undraw()
	win.getMouse()



