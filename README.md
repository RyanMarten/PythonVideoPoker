# PythonVideoPoker
This is a final project for a Highschool Intro to CS Class, it is written in Python 2.7 and uses [graphics.py](http://mcsp.wartburg.edu/zelle/python/graphics.py). 

*Run vp6.py to play the game.*

##How to Run the Game
###1. Download:
Press the "Download Zip" Button at the top right corner of the project. 

Unzip the file on your computer. 

###2. Run the Python File:
Python 2.7 is needed to run this program. For Mac or Windows, you can get it [here](https://www.python.org/downloads/release/python-2710/). 

To run it, open the vp6.py file in IDLE and press f5 or select Run->Run Module. 

For linux, you can install python with ```sudo apt-get install python``` in the terminal

To run you change to the directory with the file using ```cd``` and run it using ```python vp6.py````

##How to Play the Game:
###Game Rules
In video poker, you are placing bets on [poker hands](https://en.wikipedia.org/wiki/List_of_poker_hands) and you get winnings based on how unlikely that hand is. 

The goal is to get your balance (in the right corner) to become as large as possible

1. To get started, enter a valid bet (greater than zero but less than your balance) and click bet. This will deal you a hand. 

2. After being delt a hand, the user has one chance to discard any number of cards from the hand to improve the type of the hand, and therefore the winnings. Click cards to highlight them and select them for discarding. 

3. Click the discard button to get the new cards and see your winnings. The line with the type of hand will be highlighted and the information of your hand can be viewed in the bottom right. 

4. Repeat the last two steps to earn more and more money. If your balance reaches 0, it is *Game Over* and you will be asked to play again

###Highscores
Local highscores for both the balance and the best hand can be viewed in the file topten.txt in the src folder after the game has been played at least once. 

##Contributions
You are welcome to improve upon this project! Thanks -- Ryan 
