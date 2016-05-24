#COPYRIGHT 2016 RYAN MARTEN
'''Program Description: 
Contains class GameOver, which controls the graphical elements and variables that relate to a game over screen.
GameOver contains the follow methods: draw, undraw, isClicked. 
With these, you can control the visibility and what happens when you click a Play Again Button. 
'''
from button import * 
from graphics import *
class GameOver(object):

	def __init__(self):
		'''Contains a white box, a game over message, and a play again button'''
		self.noGold = Text(Point(300,200),"You ran out of gold")
		self.gameOverText = Text(Point(300,240),"Game Over")
		self.gameOverText.setSize(36)
		self.gameOverBox = Rectangle(Point(0,0),Point(600, 500))
		self.gameOverBox.setFill("white")
		self.playAgainButton = Button(Point(360,300),"Play Again?")
		self.isDrawn = False

	def draw(self, window):
		'''Displays all the graphical elements to the window'''
		self.window = window
		self.gameOverBox.draw(self.window)
		self.noGold.draw(self.window)
		self.gameOverText.draw(self.window)
		self.playAgainButton.draw(self.window)
		self.isDrawn = True

	def undraw(self):
		'''Removes all the graphical elements from the window'''
		self.gameOverText.undraw()
		self.gameOverBox.undraw()
		self.noGold.undraw()
		self.playAgainButton.undraw()
		self.isDrawn = False

	def isClicked(self, click):
		'''Returns whether the play again button is clicked'''
		if self.playAgainButton.isDrawn and self.playAgainButton.isClicked(click):
			return True

#Test Code
if __name__ == "__main__":
	win = GraphWin("gameover class test", 600, 500)
	over = GameOver()
	over.draw(win)
	for i in range(5):
		click = win.getMouse()
		if over.isClicked(click):
			over.undraw()
