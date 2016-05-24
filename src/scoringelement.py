#COPYRIGHT 2016 RYAN MARTEN
'''Program Description: 
Contains class ScoringElement, which controls the display and highlighting for a single poker hand score. 
ScoringSheet contains the follow methods: draw, undraw, highlight, and unhighlight
'''
from graphics import *
class ScoringElement(object):
	def __init__(self, centerpoint, text):
		'''Contains text and a highlight'''
		self.text = Text(centerpoint, text)
		self.text.setSize(10)
		self.point1 = Point(centerpoint.getX() - 150/2, centerpoint.getY() - 20/2)
		self.point2 = Point(centerpoint.getX() + 150/2, centerpoint.getY() + 20/2) 
		self.highlightBox = Rectangle(self.point1, self.point2)
		self.highlightBox.setWidth(0)
		self.highlightBox.setFill("yellow")
		self.isDrawn = False
		self.isHighlight = False

	def draw(self, window):
		'''Displays the text on the window'''
		self.window = window
		self.text.draw(self.window)
		self.isDrawn = True

	def undraw(self):
		'''Removes the text and highlight from the window'''
		self.text.undraw()
		if self.isHighlight:
			self.unhighlight()
		self.isDrawn = False

	def highlight(self):
		'''Adds the highlight to the window'''
		self.text.undraw()
		self.highlightBox.draw(self.window)
		self.isHighlight = True
		self.text.draw(self.window)

	def unhighlight(self):
		'''Removes the highlight from the window'''
		if self.isHighlight:
			self.highlightBox.undraw()
			self.isHighlight = False

#Test Code
if __name__ == "__main__":
	win = GraphWin("scoringelement class test", 600, 500)
	royalFlush = ScoringElement(Point(140,225), "Royal Flush-----[250xBet]")
	facePair = ScoringElement(Point(460,275), "Face Pair----------[1xBet]")
	royalFlush.draw(win)
	facePair.draw(win)
	win.getMouse()
	royalFlush.highlight()
	win.getMouse()
	facePair.highlight()
	win.getMouse()
	royalFlush.unhighlight()
	win.getMouse()
	royalFlush.unhighlight()
	win.getMouse()
	royalFlush.undraw()
	facePair.undraw()
	win.getMouse()
