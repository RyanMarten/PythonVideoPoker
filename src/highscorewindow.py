#COPYRIGHT 2016 RYAN MARTEN
'''Program Description: 
Contains class highscorewindow, which displays if the players current balance or hand is a top ten in the leaderboards. 
It stops gameplay and allows the user to select a name to display on the leaderboard until the enter button is clicked, 
which closes the window. This class has the methods getName and setName. 
'''
from graphics import *
from button import *
from letterselector import *
class HighScoreWindow(object):
	def __init__(self, high, rank):
		'''A highscorewindow consists of a window containing 3 letter selectors, Title, instructions, and an enter button'''
		self.window = GraphWin("New Highscore!", 500,350)
		self.youAre = Text(Point(250,90),"You are now rank %i!" %(rank))
		self.youAre.draw(self.window)
		self.enterYour = Text(Point(250,110),"Enter you name below to be displayed on the leaderboard")
		self.enterYour.setSize(10)
		self.enterYour.draw(self.window)
		self.newHighest = Text(Point(250,40),"New Highest %s" %(high))
		self.newHighest.setSize(36)
		self.newHighest.draw(self.window)
		self.enterButton = Button(Point(250,310),"Enter")
		self.enterButton.draw(self.window)
		self.firstLetter = LetterSelector(Point(210,200))
		self.firstLetter.draw(self.window)
		self.secondLetter = LetterSelector(Point(250,200))
		self.secondLetter.draw(self.window)
		self.thirdLetter = LetterSelector(Point(290,200))
		self.thirdLetter.draw(self.window)
		self.name = "AAA"

	def getName(self):
		'''Returns a string containing the three letters from the selectors'''
		click = self.window.getMouse()
		while not self.enterButton.isClicked(click):	
			self.firstLetter.isClicked(click)
			self.secondLetter.isClicked(click)
			self.thirdLetter.isClicked(click)
			click = self.window.getMouse()
		name = self.firstLetter.getLetter() + self.secondLetter.getLetter() + self.thirdLetter.getLetter()
		self.window.close()
		return name

	def setName(self, name):
		'''Sets the three letter selectors to display three characters'''
		self.firstLetter.setLetter(name[0])
		self.secondLetter.setLetter(name[1])
		self.thirdLetter.setLetter(name[2])

#Test Code
if __name__ == "__main__":
	hsWin = HighScoreWindow("Score", 8)
	print hsWin.getName()
