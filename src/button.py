#COPYRIGHT 2016 RYAN MARTEN
'''Program Description: 
Contains class Button, which controls the graphical elements and states of a button that can be clicked.
Button contains the follow methods: draw, undraw, setInactive, setActive, and isClicked.
'''
from graphics import *
class Button(object):
	'''Creates a button using graphics.py. Detects clicks and has two states: active and inactive'''

	def __init__(self, centerpoint, text, width = 100, height = 30):
		'''Button consists of a box and a text object. Placement is calculated off centerpoint,height, and witdth'''
		self.point1 = Point(centerpoint.getX() - width/2, centerpoint.getY() - height/2)
		self.point2 = Point(centerpoint.getX() + width/2, centerpoint.getY() + height/2)
		self.box = Rectangle(self.point1,self.point2)
		self.text = Text (centerpoint,text)
		self.setActive()
		self.isDrawn = False

	def draw(self, window):
		self.window = window
		'''Draws the button on a window'''
		self.box.draw(self.window)
		self.text.draw(self.window)
		self.isDrawn = True

	def undraw(self):
		'''Removes the button from the window'''
		self.box.undraw()
		self.text.undraw()
		self.isDrawn = False

	def setInactive(self):
		'''Makes the button grayed out and non clickable'''
		self.box.setFill(color_rgb(204, 204, 204))
		self.box.setOutline("")
		self.box.setWidth(2)
		self.isActive = False


	def setActive(self):
		'''Makes the button clearly seen and clickable'''
		self.box.setFill(color_rgb(204, 204, 204))
		self.box.setOutline("black")
		self.box.setWidth(2)
		self.isActive = True

	def toggleActive(self):
		'''Makes the button active/inactive if the card is inactive/active'''
		if self.isActive:
			self.setInactive()
		else:
			self.setActive()

	def isClicked(self,click):
		'''Returns whether the button has been clicked'''
		if self.point1.getX() <= click.getX() <= self.point2.getX() and  self.point1.getY() <= click.getY() <= self.point2.getY():
			return True
		else: 
			return False

		


#Test Code
if __name__ == "__main__":
	win = GraphWin("button class test", 300, 300)
	button1 = Button(Point(60,30),"Test")
	button2 = Button(Point(30,70),":D",40,40)
	circle = Circle(Point(230,230),50)
	circle.draw(win)

	button1.draw(win)
	button2.draw(win)
	for i in range(5):
		click = win.getMouse()
		if button1.isClicked(click):
			button1.toggleActive()
		elif button2.isClicked(click):
			circle.setFill("green")

	button1.undraw()
	button2.undraw()
	win.getMouse()