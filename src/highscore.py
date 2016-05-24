#COPYRIGHT 2016 RYAN MARTEN
'''Program Description: 
Contains class highscore, which determines if the players current balance or hand is a top ten in the leaderboards. 
If her winnings continue to increase more, and/or she gets an even better hand, she moves up the list(s), 
but if they drop, she stays in her highest position. This class has the methods isTopScore and isTopHand. 
'''
from button import *
from highscorewindow import *
from hand import *
import ast
class HighScore(object):
	'''Highscore edits a file called 'topten.txt' and creates a entry window for a new highscoring session  '''
	def __init__(self):
		try: 
			f = open("topten.txt", "r+")
		except IOError:
			#Create the file if it doesn't exist, and add filler player scores
			f = open("topten.txt", "w")
			f.write('TOP TEN SCORERS: \n')
			for i in range(10):
				f.write("AAA..........0 \n")
			f.write("\n")
			f.write('TOP TEN HANDS: \n')
			for i in range(10):
				f.write("AAA..........['0h', '0c', '0s', '0c', '0h'] \n")
			f.close()
		else:
			f.close()
		self.winningScoreSession = False
		self.winningHandSession = False
		self.name = "AAA"


	def isTopScore(self, balance):
		'''Changes position of score topten.txt based on the current balance and the leaderboard'''
		#read what is currently in the file
		f = open("topten.txt", "r")
		rank = 11
		lines = f.readlines()
		f.close()
		#if you already are a winning game, don't prompt for name or make a new entry, just move the current one
		if self.winningScoreSession:
			#increase rank if it is a greater balance than the one below it until in the correct spot
			while balance > int(lines[self.scoreRank][13:]):
				if self.scoreRank == 1:
					#if it is at the top, this is the highest it can go and rewrite the first line
					lines[1] = "%s..........%i \n" %(self.name, balance)
				else: 
					#other wise, move it up and move the smaller one down
					lines.pop(self.scoreRank)
					self.scoreRank -= 1
					lines.insert(self.scoreRank,"%s..........%i \n" %(self.name, balance))
			#submit these changes to the file
			f = open("topten.txt", "w")
			f.writelines(lines)
			f.close()
					

		#otherwise, prompt the user for a name to enter and create a new entry in the correct rank and delete lowest entry
		else:
			lines.reverse()
			#increase rank if its more than the rank above
			for i,line in zip(range(10),lines[12:22]):
				score = int(line[13:])
				if balance > score:
					rank -= 1
			#if it places on the leader board, create a new entry and asign this as a winning session
			if rank != 11:
				self.scoreRank = rank
				#Get the name to use on the leaderboard from the user
				highwin = HighScoreWindow("Score",rank)
				highwin.setName(self.name)
				self.name = highwin.getName()
				f = open("topten.txt", "r")
				lines = f.readlines()
				f.close()
				#insert the new score on the leaderboard and delete the 11th one (there are only 10 on the leaderboard)
				lines.insert(rank,"%s..........%i \n" %(self.name, balance))
				lines.pop(11)
				f = open("topten.txt", "w")
				f.writelines(lines)
				f.close()

				self.winningScoreSession = True

	def isTopHand(self, hand, type, highcard):
		'''Changes position of score topten.txt based on the current hand and the leaderboard'''

		f = open("topten.txt", "r")
		rank = 11
		lines = f.readlines()
		f.close()
		#if you already are a winning game, don't prompt for name or make a new entry, just move it
		if self.winningHandSession: 
			#evaluate the hand above the current rank
			handScore = Hand(ast.literal_eval(lines[self.handRank+12][13:]))
			typeScore = handScore.handType()
			highcardScore = handScore.highCard()
			#increase rank until at top or less than the rank above
			while type > typeScore or (type == typeScore and highcard > highcardScore):
				if self.handRank == 1:
					lines[13] = "%s..........%s \n" %(self.name, str(hand))
					break
				else: 
					lines.pop(self.handRank+12)
					self.handRank -= 1
					lines.insert(self.handRank+12,"%s..........%s \n" %(self.name, str(hand)))
				handScore = Hand(ast.literal_eval(lines[self.handRank+12][13:]))
				typeScore = handScore.handType()
				highcardScore = handScore.highCard()
			f = open("topten.txt", "w")
			f.writelines(lines)
			f.close()
					


		else:
			lines.reverse()
			for i,line in zip(range(10),lines[0:10]):
				#evalulate the hand above the current rank, increase rank if it has a lower type or equal type and lower highcard
				handScore = Hand(ast.literal_eval(line[13:]))
				typeScore = handScore.handType()
				highcardScore = handScore.highCard()
				if type > typeScore:
					rank -= 1
				elif type == typeScore:
					if highcard > highcardScore:
						rank -= 1	

			if rank != 11:
				self.handRank = rank
				#get name for entry on the leaderboard
				highwin = HighScoreWindow("Hand",rank)
				highwin.setName(self.name)
				self.name = highwin.getName()
				f = open("topten.txt", "r")
				lines = f.readlines()
				f.close()
				#submit the changes to the file and assign this as a winning session
				lines.insert(12+rank,"%s..........%s \n" %(self.name, str(hand)))
				lines.pop(23)
				f = open("topten.txt", "w")
				f.writelines(lines)
				f.close()
				self.winningHandSession = True


#Test code
if __name__ == "__main__":
	high = HighScore()
	high.isTopScore(50)
	high.isTopHand(['4h','2c','5s','th','qd'], 0 , 12)
	high.isTopScore(50)
	high.isTopHand(['2s','4s','5s','7s','7s'], 1, 7)
	high.isTopScore(70)
	high.isTopHand(['2s','4s','5s','ks','ks'], 1, 13)
	high.isTopScore(140)
	high.isTopHand(['as','as','ah','ks','ks'], 6, 14)

	high = HighScore()
	high.isTopScore(120)
	high.isTopHand(['4h','2c','5s','th','qd'], 0 , 12)
	high.isTopScore(50)
	high.isTopHand(['2s','3s','4s','5s','6s'], 8, 6)
	high.isTopScore(70)
	high.isTopHand(['2s','4s','5s','ks','ks'], 1, 13)
	high.isTopScore(120)
	high.isTopHand(['as','as','ah','ks','ks'], 6, 14)








		
			
