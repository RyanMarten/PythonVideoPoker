#COPYRIGHT 2016 RYAN MARTEN
'''Program Description: 
Contains class Deck, which creates standard 52 card deck and can be randomized and have cards removed.
Deck contains the follow methods: shuffle and deal.
'''
from random import *

class Deck(object):
	'''Represents a card deck with 52 cards. Can shuffle and deal the deck'''
	def __init__(self):
		self.ranks = ['a','k','q','j','t','9','8','7','6','5','4','3','2']
		self.suits = ['s','h','d','c']
		self.deck = []
		for suit in self.suits:
			for rank in self.ranks:
				self.deck.append(rank+suit)
	def shuffle(self):
		"""Shuffles the deck randomly using random.py"""
		shuffle(self.deck)
	def deal(self, numCards):
		"""Deals a hand of size numCards and removes it from the deck"""
		hand = []
		for i in range(numCards):
			hand.append(self.deck.pop(0))
		return hand
	def __repr__(self):
		"""Deck is represented as a list of its current cards"""
		return str(self.deck)

#Test Code
if __name__ == "__main__":
	seed(1)
	mydeck = Deck()    
	print mydeck           
	print mydeck.deal(5), "=['as', 'ks', 'qs', 'js', 'ts']"
	mydeck.shuffle()        
	print mydeck.deal(5), "=['3h', 'th', '7s', 'qc', '5c']"        
	print mydeck.deal(2), "=['5h', '9h']"

	print "Deck: ", mydeck
