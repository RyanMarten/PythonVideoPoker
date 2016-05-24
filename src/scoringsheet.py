#COPYRIGHT 2016 RYAN MARTEN
'''Program Description: 
Contains class ScoringSheet, which controls the graphical elements that explain the scoring of different poker hands. 
ScoringSheet contains the follow methods: draw, undraw, highlightScore, and unHighLightScore.
With these, you can control the visibility and highlighting of each poker hand score. 
'''
from graphics import *
from scoringelement import *
class ScoringSheet(object):

	def __init__(self):
		'''ScoringSheet contains a box, and an element for each type of winning poker hand'''
		self.rewardsBox = Rectangle(Point(60,200),Point(540,300))
		self.royalFlush = ScoringElement(Point(140,225), "Royal Flush-----[250xBet]")
		self.straightFlush = ScoringElement(Point(300,225), "Straight Flush---[50xBet]")
		self.fourKind = ScoringElement(Point(460,225), "4 of a kind------[25xBet]")
		self.fullHouse = ScoringElement(Point(140,250), "Full House----------[9xBet]")
		self.flush = ScoringElement(Point(300,250), "Flush-----------------[6xBet]")
		self.straight = ScoringElement(Point(460,250), "Straight------------[4xBet]")
		self.threeKind = ScoringElement(Point(140,275), "3 of a kind-----------[3xBet]")
		self.twoPair = ScoringElement(Point(300,275), "2 pair-----------------[2xBet]")
		self.facePair = ScoringElement(Point(460,275), "Face Pair----------[1xBet]")
		self.isDrawn = False
		
	def draw(self, window):
		'''Displays the box and the elements on the window'''
		self.window = window
		self.royalFlush.draw(self.window)
		self.straightFlush.draw(self.window)
		self.fourKind.draw(self.window)
		self.fullHouse.draw(self.window)
		self.flush.draw(self.window)
		self.straight.draw(self.window)
		self.threeKind.draw(self.window)
		self.twoPair.draw(self.window)
		self.facePair.draw(self.window)
		self.rewardsBox.draw(self.window)
		self.isDrawn = True

	def undraw(self):
		'''Removes all the elements from the window'''
		self.royalFlush.undraw()
		self.straightFlush.undraw()
		self.fourKind.undraw()
		self.fullHouse.undraw()
		self.flush.undraw()
		self.straight.undraw()
		self.threeKind.undraw()
		self.twoPair.undraw()
		self.facePair.undraw()
		self.rewardsBox.undraw()
		self.rewardsBox.undraw()
		self.isDrawn = False

	def highlightScore(self, type, highcard):
		'''Highlights an element based on matching type and highcard'''
		if type == 9:
			self.royalFlush.highlight()
		elif type == 8:
			self.straightFlush.highlight()
		elif type == 7:
			self.fourKind.highlight()
		elif type == 6:
			self.fullHouse.highlight()
		elif type == 5:
			self.flush.highlight()
		elif type == 4:
			self.straight.highlight()
		elif type == 3:
			self.threeKind.highlight()
		elif type == 2:
			self.twoPair.highlight()
		elif type == 1 and highcard >10:
			self.facePair.highlight()
		
	def unHighlightScores(self):
		'''Removes all highlights from each element'''
		self.royalFlush.unhighlight()
		self.straightFlush.unhighlight()
		self.fourKind.unhighlight()
		self.fullHouse.unhighlight()
		self.flush.unhighlight()
		self.straight.unhighlight()
		self.threeKind.unhighlight()
		self.twoPair.unhighlight()
		self.facePair.unhighlight()
		


#Test Code
if __name__ == "__main__":
	win = GraphWin("scoringsheet class test", 600, 500)
	scores = ScoringSheet()
	scores.draw(win)
	win.getMouse()
	scores.highlightScore("Straight Flush", 14)
	win.getMouse()
	scores.unHighlightScores()
	win.getMouse()
	scores.highlightScore("Straight Flush", 11)
	win.getMouse()
	scores.highlightScore("Four of a kind", 7)
	win.getMouse()
	scores.highlightScore("Full House", 4)
	win.getMouse()
	scores.highlightScore("Flush", 13)
	win.getMouse()
	scores.highlightScore("Straight", 5)
	win.getMouse()
	scores.highlightScore("Three of a kind", 8)
	win.getMouse()
	scores.highlightScore("Two pair",  5)
	win.getMouse()
	scores.highlightScore("Pair", 14)
	win.getMouse()
	scores.highlightScore("Pair", 8)
	win.getMouse()
	scores.unHighlightScores()
	win.getMouse()
	scores.undraw()
	win.getMouse()