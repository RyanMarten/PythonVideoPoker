#COPYRIGHT 2016 RYAN MARTEN
'''Program Description: 
Contains class Hand, which controls the graphical elements and variables that relate to hand of cards. 
Hand contains the follow methods: draw, undraw, discard, convertHand, handType, highCard, isClicked and highcardConversion.
'''
from graphics import *
from random import *
from deck import *
from card import *
import time

class Hand(object):
	'''Creates a graphical representation of a list of 5 cards and evalulates that list'''
	def __init__(self, hand):
		'''Takes a list of cards'''
		self.hand = hand
		self.isDrawn = False
		if not self.hand == ['b','b','b','b','b']:
			self.convertHand()

	def draw(self, window):
		'''Displays the hand on the window'''
		self.window = window
		width = window.getWidth()
		height = window.getHeight()
		#Display each card, moving each one to the right so they don't overlap
		self.cardGraphics = [] 
		for i, card in enumerate(self.hand):
			#set multiplier to 20 for nice stacked hand, 80 for spread out hand
			graphic = Card(card, Point(130+i*85,130))
			self.cardGraphics.append(graphic)
			graphic.draw(window)
		self.isDrawn = True

	def undraw(self):
		'''Removes the hand from the window'''
		if self.isDrawn:
			for graphic in self.cardGraphics:
				graphic.undraw()
			self.isDrawn = False

	def discard(self, Deck):
		'''Removes selected cards from the window and the hand. Deals new cards to make hand whole again'''
		removed = 0
		for card in self.cardGraphics:
			if card.isActive:	
				self.hand.remove(card.name)
				#TOOD IT can be out of range
				removed += 1
		if removed > 0:
			self.undraw()
			self.draw(self.window)
			for i in range(removed):
				time.sleep(.25)
				self.hand.append(Deck.deck.pop(0))
				self.undraw()
				self.draw(self.window)

	def __repr__(self):
		'''Represented by its hand list'''
		return str(self.hand)

	def convertHand(self):
		'''Takes a list of cards and changes card values to a list of an integer and its suit (ace is high)'''
		conversion = {
			'a': 14,
			'k': 13,
			'q': 12,
			'j': 11,
			't': 10
		}
		#TODO: Trouble converting q
		self.convertedHand = []
		for card in self.hand:
			self.convertedHand.append(card)
		for i in range(0,len(self.convertedHand)):
			for key in conversion:
				if self.convertedHand[i][0] == key:
					#replaces card containing a face card with a list of its corresponding integer value and its suit
					self.convertedHand[i] = [conversion[key], self.convertedHand[i][1]]
					break
			else:
				#replaces card containing a number with list of an integer of that number and its suit
				self.convertedHand[i] = [int(self.convertedHand[i][0]), self.convertedHand[i][1]]
		self.convertedHand.sort()

	def is_straight(self):
		'''Takes a hand and returns whether it contains a straight'''
		#For a hand to be a straight, each card needs to be 1 higher than the previous
		self.low_Ace()
		for i in range(0,4):
			if self.convertedHand[i][0] + 1 != self.convertedHand[i+1][0]:
				break
		else:
			return True
		for i in range(0,4):
			if self.aceconvertedHand[i][0] + 1 != self.aceconvertedHand[i+1][0]:
				break
		else:
			return True
		return False

	def is_flush(self):
		'''Takes a hand and returns whether it contains a flush'''
		#For a hand to be a flush, each card needs to have the same suit as the previous
		for i in range(0,4):
			if self.convertedHand[i][1] != self.convertedHand[i+1][1]:
				break
		else:
			return True
		return False

	def low_Ace(self):
		'''Takes a converted hand and a new convertedhand with the value of the high ace changed a low ace'''
		#replaces a integer value of 14 with 1 in a card
		self.aceconvertedHand = []
		for card in self.convertedHand:
			self.aceconvertedHand.append([card[0],card[1]])
		for i in range(0,len(self.convertedHand)):
			if self.convertedHand[i][0] == 14:
				self.aceconvertedHand[i][0] = 1
		self.aceconvertedHand.sort()


	def handType(self):
		'''
		Determines the type of poker hand and returns an interger representing this. 
			Hand			Type 		Notes										
			-straight flush	8			same suit, all 5 in ascending order			
			-4 of a kind	7			4 of the same number								
			-full house		6			all cards have a another of the same (pair + three of a kind)	
			-flush			5			same suit									 
			-straight		4			all 5 in ascending orders
			-3 of a kind	3			3 of the same number
			-2 pair			2			2x 2 of the same number						
			-pair			1			2 of the same number			
			-high card 		0			nothing	else
		'''			
		#make all cards of the same rank next to each other						
		self.convertHand()
		self.type = 0
		value = 0
		#give the hand a value based of how many pairs of ranks it has
		for i in range(0,4):
			if self.convertedHand[i][0] == self.convertedHand[i+1][0]:
				value += 2
		if value == 6:
			#3 pairs are either a full house or 4 of a kind: (full house: aabbb bbbaa // 4 of a kind: aaaax xaaaa)
			if self.convertedHand[1][0] == self.convertedHand[2][0] == self.convertedHand[3][0]:
				#if the middle three cards are the same rank, its a 4 of a kind
				self.type = 7
			else: 
				#if not its a full house
				self.type = 6
		elif value == 4:
			#2 pairs are either a 3 of a kind or two pair: (3 of a kind: aaaxy xaaay xyaaa // two pair: xaabb aaxbb aabbx)
			for i in range(0,3):
				if self.convertedHand[i][0] == self.convertedHand[i+2][0]:
					#if a card is the same rank as a card 2 cards away, its 3 of a kind
					self.type = 3
					break
			else:  
				#if not, its a two pair
				self.type = 2
		elif value == 2:
			#1 pair is a pair
			self.type = 1
			#no pairs means can still be a straight, flush, or straight flush 
		else: 
			if self.is_straight():	
				if self.is_flush():
					#straight flush
					self.type = 8
					if self.convertedHand[0][0] == 10:
						#Royal Flush
						self.type = 9
				else:
					#just a straight
					self.type = 4
			elif self.is_flush():
				#flush
				self.type = 5
			else: 
				#if its nothing else, the hand is just a highcard
				self.type = 0
		return self.type

	def highCard(self):
		'''Returns the highcard (An Int) of the hand based off the hand type'''
		self.convertHand()
		self.highcard = 0
		self.handType()
		#each type of poker hand has its own way to find a highcard
		if self.type == 0 or self.type == 5 or self.type == 8 or self.type == 4 or self.type == 9:
			#if its a highcard,flush,straight, or straight flush its the highest card in the hand
			if (self.type == 8 or self.type == 4) and self.aceconvertedHand[4][0] == 5:
				#low ace straights and straight flushes have a highcard of 5
				self.highcard = 5
				return self.highcard
			else: 
				for card in self.convertedHand:
					if card[0] > self.highcard: 
						self.highcard = card[0]
				return self.highcard
		if self.type == 1 or self.type == 7 or self.type == 3:
			#if its a pair, three of a kind, or four of a kind, the highcard will be rank with >1 cards in the hand
			for i in range(0,4):
				if self.convertedHand[i][0] == self.convertedHand[i+1][0]:
					self.highcard = self.convertedHand[i][0]
					return self.highcard
		if self.type == 2:
			#if its a two pair, the highcard with be the rank of the higher pair
			for i in range(0,4):
				if self.convertedHand[i][0] == self.convertedHand[i+1][0] and self.convertedHand[i][0] > self.highcard:
					self.highcard = self.convertedHand[i][0]
			return self.highcard
		if self.type == 6:
			#if its a full house, the highcard is the rank of the 3 of a kind	
			for i in range(0,3):
				if self.convertedHand[i][0] == self.convertedHand[i+2][0]:
					self.highcard = self.convertedHand[i][0]
					return self.highcard

	def highcardConversion(self, card):
		'''Converts and returns a card with an interger value into its corresponding face value'''
		conversion = {
			11: "Jack",
			12: "Queen",
			13: "King",
			14: "Ace"
		}
		for key in conversion:
			if card == key:
				card = conversion[key]
				break
		return card


	def typeConversion(self, type):
		'''Coverts and returns the hand type interger value into a string description'''
		conversion = {
			9: "Royal Flush",
			8: "Straight Flush",
			7: "Four of a kind",
			6: "Full House",
			5: "Flush",
			4: "Straight",
			3: "Three of a kind",
			2: "Two pair",
			1: "Pair",
			0: "High Card"
		}
		for key in conversion:
			if type == key:
				type = conversion[key]
				break
		return type

	def isClicked(self, click):
		if self.cardGraphics[0].isClicked(click):
			self.cardGraphics[0].toggleActive()
		elif self.cardGraphics[1].isClicked(click):
			 self.cardGraphics[1].toggleActive()
		elif self.cardGraphics[2].isClicked(click):
			 self.cardGraphics[2].toggleActive()	
		elif self.cardGraphics[3].isClicked(click):
			 self.cardGraphics[3].toggleActive()
		elif self.cardGraphics[4].isClicked(click):
			 self.cardGraphics[4].toggleActive()

#Test Code
if __name__ == "__main__":
	
	win = GraphWin("hand class test", 600, 500)
	mydeck = Deck()

	myhand = Hand(['ts','ks','qs','as','js'])
	print myhand
	print myhand.typeConversion(myhand.handType()), '=Royal Flush  & ', myhand.type, '=8'
	myhand.highCard()
	print myhand.highcard, '=14  & ', myhand.highcardConversion(myhand.highcard), '=Ace'
	myhand.draw(win)
	win.getMouse()
	myhand.undraw()

	myhand = Hand(['as','ac','4s','ad','ah'])
	print myhand
	print myhand.typeConversion(myhand.handType()), '=Four of a kind  & ',myhand.type ,'=7'
	myhand.highCard()
	print myhand.highcard,  '=14  & ', myhand.highcardConversion(myhand.highcard), '=Ace'
	myhand.draw(win)
	win.getMouse()
	myhand.undraw()

	myhand = Hand(['as','ac','4s','ad','4c'])
	print myhand
	print myhand.typeConversion(myhand.handType()), '=Full House  & ',myhand.type ,'=6'
	myhand.highCard()
	print myhand.highcard,  '=14  & ', myhand.highcardConversion(myhand.highcard), '=Ace'
	myhand.draw(win)
	win.getMouse()
	myhand.undraw()

	myhand = Hand(['2s','4s','5s','ks','3s'])
	print myhand
	print myhand.typeConversion(myhand.handType()), '=Flush  & ',myhand.type ,'=5'
	myhand.highCard(), myhand.highcard,  '=13  & ', myhand.highcardConversion(myhand.highcard), '=King'
	myhand.draw(win)
	win.getMouse()
	myhand.undraw()

	myhand = Hand(['2s','4s','5s','ac','3s'])
	print myhand
	print myhand.typeConversion(myhand.handType()), '=Straight  & ',myhand.type ,'=4'
	print myhand.highCard(), '=5  & ', myhand.highcardConversion(myhand.highcard), '=5'
	myhand.draw(win)
	win.getMouse()
	myhand.undraw()
	
	myhand = Hand(['3s','ac','js','jd','jh'])
	print myhand
	print myhand.typeConversion(myhand.handType()), '=Three of a kind  & ',myhand.type ,'=3'
	print myhand.highCard(), '=11  & ', myhand.highcardConversion(myhand.highcard), '=Jack'
	myhand.draw(win)
	win.getMouse()
	myhand.undraw()

	myhand = Hand(['qs','qc','4s','4d','kh'])
	print myhand
	print myhand.typeConversion(myhand.handType()), '=Two Pair  & ',myhand.type ,'=2'
	print myhand.highCard(), '=12  & ', myhand.highcardConversion(myhand.highcard), '=Queen'
	myhand.draw(win)
	win.getMouse()
	myhand.undraw()

	myhand = Hand(['as','2s','4s','6s','2c'])
	print myhand
	print myhand.typeConversion(myhand.handType()), '=Pair  & ',myhand.type ,'=1'
	print myhand.highCard(), '=2  & ', myhand.highcardConversion(myhand.highcard), '=2'
	myhand.draw(win)
	win.getMouse()
	myhand.undraw()

	myhand = Hand(['7s','5c','4s','3s','2s'])
	print myhand
	print myhand.handType(), '=Highcard  & ',myhand.type ,'=0'
	print myhand.highCard(), '=7  & ', myhand.highcardConversion(myhand.highcard), '=7'
	myhand.draw(win)
	win.getMouse()
	myhand.undraw()

	myhand = Hand(['5s','tc','4s','3s','2s'])
	print myhand
	print myhand.typeConversion(myhand.handType()), '=Highcard  & ',myhand.type ,'=0'
	print myhand.highCard(), '=10  & ', myhand.highcardConversion(myhand.highcard), '=10'
	myhand.draw(win)
	win.getMouse()

	for i in range(6):
		click = win.getMouse()
		myhand.isClicked(click)
		

	myhand.discard(mydeck)
	win.getMouse()
	myhand.undraw()
	win.getMouse()
