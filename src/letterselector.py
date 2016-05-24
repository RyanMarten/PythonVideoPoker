#COPYRIGHT 2016 RYAN MARTEN
'''Program Description: 
Contains class letterselector, which lets the user iterate up and down the alphabet, to select a letter. 
This class has the methods draw, undraw, isClicked, getLetter, and setLetter. 
'''
from graphics import *
import string


class LetterSelector(object):
	def __init__(self, centerpoint):
		'''A letter selector contains two arrows and the current letter'''
		centerY = centerpoint.getY()
		centerX = centerpoint.getX()
		self.currentIndex = 0
		self.upPoint1 = Point(centerX-10, centerY-35)
		self.upPoint2 = Point(centerX+10, centerY-35)
		self.upPoint3 = Point(centerX, centerY-45)
		self.upSelect = Polygon(self.upPoint1, self.upPoint2, self.upPoint3)
		self.upSelect.setFill("black")
		self.selectionList = string.ascii_uppercase
		self.currentSelection = Text(centerpoint, self.selectionList[0])
		self.currentSelection.setSize(36)
		self.downPoint1 = Point(centerX-10, centerY+30)
		self.downPoint2 = Point(centerX+10, centerY+30)
		self.downPoint3 = Point(centerX, centerY+40)
		self.downSelect = Polygon(self.downPoint1, self.downPoint2, self.downPoint3)
		self.downSelect.setFill("black")


	def draw(self, window):
		'''Displays the selector to a window'''
		self.window = window
		self.upSelect.draw(self.window)
		self.downSelect.draw(self.window)
		self.currentSelection.draw(self.window)

	def undraw(self):
		'''Removes the selector from the window'''
		self.upSelect.undraw()
		self.downSelect.undraw()
		self.currentSelection.undraw()

	def isClicked(self, click):
		'''Returns whether the selector has been clicked and changes the current letter based on which arrow was clicked'''
		if self.upPoint1.getX() <= click.getX() <= self.upPoint2.getX() and \
		   self.upPoint3.getY() <= click.getY() <= self.upPoint2.getY():
		   	self.currentIndex += 1
			self.currentSelection.setText(self.selectionList[self.currentIndex])
			return True
		elif self.downPoint1.getX() <= click.getX() <= self.downPoint2.getX() and \
		   self.downPoint2.getY() <= click.getY() <= self.downPoint3.getY():
		    self.currentIndex -= 1
		    self.currentSelection.setText(self.selectionList[self.currentIndex])
		    return True
		else: 
			return False

	def getLetter(self):
		'''Returns the current selection letter'''
		return self.currentSelection.getText()

	def setLetter(self, letter):
		'''Sets the current selection letter and updates the display'''
		self.currentSelection.setText(self.selectionList[self.selectionList.index(letter)])

#Test Code
if __name__ == "__main__":
	win = GraphWin("LetterSelector class Test", 500,400)
	youAre = Text(Point(250,90),"You are now rank 1!")
	youAre.draw(win)
	enterYour = Text(Point(250,110),"Enter you name below to be displayed on the leaderboard")
	enterYour.setSize(10)
	enterYour.draw(win)
	newHighest = Text(Point(250,40),"New Highest Score")
	newHighest.setSize(36)
	newHighest.draw(win)
	select1 = LetterSelector(Point(250,200))
	select1.draw(win)
	win.getMouse()
	select1.undraw()
	win.getMouse()
	select1.draw(win)
	for i in range(20):
		click = win.getMouse()
		select1.isClicked(click)