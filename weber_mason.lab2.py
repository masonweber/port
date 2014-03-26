import random

class Element:
	_name = ""	#initializing class variable
	def __init__(self, name):	#class constructor
		self._name = name	#_name is inherited, accessed by self._name
		
	def name(self):	#returning class name for each object
		return self._name
	
	def compareTo(self, e):	#class to inherit that must be overwritten
		raise NotImplementedError("Not yet implemented")

class Rock(Element):	#class definition
	def __init__(self):	#constructor
		Element.__init__(self, "Rock")	#calling parent constructor method to assign val to _name
		
	def compareTo(self, e):	#base method to determine winner and phrasing
		if e.name() == "Rock":
			return("Rock equals Rock", "Tie")
		elif e.name() == "Paper":
			return("Paper covers Rock", "Lose")
		elif e.name() == "Lizard":
			return("Rock crushes Lizard", "Win")
		elif e.name() == "Spock":
			return("Spock vaporizes Rock", "Lose")
		elif e.name() == "Scissors":
			return("Rock crushes Scissors", "Win")
		else:
			print(e.name())
			return("Game broken!", "Tie")					
	
class Paper(Element):
	def __init__(self):
		Element.__init__(self, "Paper")

	def compareTo(self, e):
		if e.name() == "Paper":
			return("Paper equals Paper", "Tie")
		elif e.name() == "Scissors":
			return("Scissors cut Paper", "Lose")
		elif e.name() == "Rock":
			return("Paper covers Rock", "Win")
		elif e.name() == "Lizard":
			return("Lizard eats Paper", "Lose")
		elif e.name() == "Spock":
			return("Paper disproves Spock", "Win")
		else:
			return("Game broken!", "Tie")
			
class Scissors(Element):
	def __init__(self):
		Element.__init__(self, "Scissors")

	def compareTo(self, e):
		if e.name() == "Scissors":
			return("Scissors equals Scissors", "Tie")
		elif e.name() == "Paper":
			return("Scissors cut Paper", "Win")
		elif e.name() == "Spock":
			return("Spock smashes Scissors", "Lose")
		elif e.name() == "Lizard":
			return("Scissors decapitate Lizard", "Win")
		elif e.name() == "Rock":
			return("Rock crushes Scissors", "Lose")
		else:
			return("Game broken!", "Tie")
	
class Lizard(Element):
	def __init__(self):
		Element.__init__(self, "Lizard")

	def compareTo(self, e):
		if e.name() == "Lizard":
			return("Lizard equals Lizard", "Tie")
		elif e.name() == "Spock":
			return("Lizard poisons Spock", "Win")
		elif e.name() == "Rock":
			return("Rock crushes Lizard", "Lose")
		elif e.name() == "Scissors":
			return("Scissors decapitate Lizard", "Lose")
		elif e.name() == "Paper":
			return("Lizard eats Paper", "Win")
		else:
			return("Game broken!", "Tie")
	
class Spock(Element):
	def __init__(self):
		Element.__init__(self, "Spock")

	def compareTo(self, e):
		if e.name() == "Spock":
			return("Spock equals Spock", "Tie")
		elif e.name() == "Lizard":
			return("Lizard poisons Spock", "Lose")
		elif e.name() == "Scissors":
			return("Spock smashes Scissors", "Win")
		elif e.name() == "Paper":
			return("Paper disproves Spock", "Lose")
		elif e.name() == "Rock":
			return("Spock vaporizes Rock", "Win")
		else:
			return("Game broken!", "Tie")
	
rock = Rock()	#initializing instance of each class
paper = Paper()
scissors = Scissors()
lizard = Lizard()
spock = Spock()
moves = [rock, paper, scissors, lizard, spock]	#creating a list of moves

class Player:	#player superclass
	_name = ""	#defining class variable
	def __init__(self, name):
		self._name = name
	
	def name(self):
		return self._name
	
	def play():
		raise NotImplementedError("Not yet implemented")

class StupidBot(Player):	#aka SheldonBot
	def __init__(self):
		Player.__init__(self, "StupidBot")
	
	def play(self):
		return rock;
		
class RandomBot(Player):	#aka DarkHorseBot
	myMoves = list(moves)
	
	def __init__(self):
		Player.__init__(self, "RandomBot")
	
	def play(self):
		i = random.randint(0,4)
		move = self.myMoves.pop(i)
		self.myMoves.append(move)
		return move
		
class IterativeBot(Player):	#aka AllTheMovesBot
	myMoves = list(moves)
	count = False
	
	def __init__(self):
		Player.__init__(self, "IterativeBot")
		self.count = 0
		
	def play(self):
		if self.count < 5:	#should not need more than 5 moves, but safety
			self.count = self.count + 1	#no post-incrementation
			return self.myMoves.pop()
		else:
			self.myMoves = list(moves)	#refill myMoves from moves object
			self.count = 1	#combination of resetting and incrementing
			return self.myMoves.pop()
			
class LastPlayBot(Player):	#aka CopycatBot
	myMoves = list(moves)
	lastMove = False
	playerNum = 0
	
	def __init__(self, num):
		Player.__init__(self, "LastPlayBot")
		self.playerNum = num
	
	def play(self):
		if self.playerNum == 1 and len(p2Moves) > 0:
			move = p2Moves.pop()
			p2Moves.append(move)
			return move
		elif self.playerNum == 1 and len(p2Moves) == 0:
			i = random.randint(0,4)
			move = self.myMoves.pop(i)
			self.myMoves.append(move)
			return move
		elif self.playerNum == 2 and len(p1Moves) > 0:
			move = p1Moves.pop()
			p1Moves.append(move)
			return move
		else:
			i = random.randint(0,4)
			move = self.myMoves.pop(i)
			self.myMoves.append(move)
			return move
			
class MyBot(Player):	#aka MyDestructionBot
	playerNum = 0
	list = list(moves)
	def __init__(self, num):
		Player.__init__(self, "MyBot")
		self.playerNum = num
	
	def play(self):
		myMove = Element("")
		theirMove = Element("")
		newMove = Element("")
		
		if len(p1Moves) > 0:	#actually doesn't matter which player it is
			myMove = p1Moves.pop()
			p1Moves.append(myMove)
			theirMove = p2Moves.pop()
			p2Moves.append(theirMove)
			list = list(moves)
			list.remove(myMove)
			list.remove(theirMove)
			i = random.randint(0,2)
			myMove = list.pop(i)
			return myMove
		else:
			self.list = list(moves)
			i = random.randint(0,4)
			myMove = self.list.pop(i)
			return myMove			
		
class Human(Player):	#bring your best
	def __init__(self):
		Player.__init__(self, "Human")
	
	def play(self):	#might need self declared
		print("(1) : Rock\n(2) : Paper\n(3) : Scissors\n(4) : Lizard\n (5) : Spock")
		flag = True
		while flag:
			inputMove = input('Enter your move: ')	#get move from input
			flag = False
			if inputMove == '1':
				return rock
			elif inputMove == '2':
				return paper
			elif inputMove == '3':
				return scissors
			elif inputMove == '4':
				return lizard
			elif inputMove == '5':
				return spock
			else:
				print("Invalid move. Try again.")
				flag = True
		
p1Moves = []	#list of previous moves
p2Moves = []	#list of previous moves
		
class Main:
	p1Score = 0
	p2Score = 0

	def __init__(self):
		print("Welcome to Rock, Paper, Scissors, Lizard, Spock, implemented by Mason Weber./n")
		print("Please choose two players:\n\t(1) StupidBot\n\t(2) RandomBot\n\t" +
		"(3) IterativeBot\n\t(4) LastPlayBot\n\t(5) MyBot\n\t(6) Human Player\n")
		
		flagA = True
		p1 = Player("")
		p2 = Player("")
		while flagA:
			a = input("Select player 1:")
			flagA = False	#instead of adding to all if/elif
			if a == '1':
				p1 = StupidBot()
			elif a == '2':
				p1 = RandomBot()
			elif a == '3':
				p1 = IterativeBot()
			elif a == '4':
				p1 = LastPlayBot(1)
			elif a == '5':
				p1 = MyBot(1)
			elif a == '6':
				p1 = Human()
			else:
				print("Not a valid choice.  Try again.")
				flagA = True	#setting up to go through another input
				
		#mirroring code to get player 2 type		
		flagB = True
		
		while flagB:
			b = input("Select player 2:")
			flagB = False
			if b == '1':
				p2 = StupidBot()
			elif b == '2':
				p2 = RandomBot()
			elif b == '3':
				p2 = IterativeBot()
			elif b == '4':
				p2 = LastPlayBot(2)
			elif b == '5':
				p2 = MyBot(2)
			elif b == '6':
				p2 = Human()
			else:
				print("Not a valid choice.  Try again.")
				flagB = True		
				
		#on to the main game control loop
		print("\n" + p1.name() + " vs " + p2.name() + ". Go!\n")
		for i in range(5):	#round i, 1 to 5
			j = i + 1
			print("Round " + str(j) + ":")
			move1 = p1.play()
			move2 = p2.play()
			p1Moves.append(move1)
			p2Moves.append(move2)
			print("Player 1 chooses ")
			print("Player 2 chooses ")
			type, result = move1.compareTo(move2)
			print(type)
			if result == "Win":
				print("Player 1 won the round")
				self.p1Score = self.p1Score + 1
			elif result == "Lose":
				print("Player 2 won the round")
				self.p2Score = self.p2Score + 1
			else:
				print("Round was a tie")
		
		print("The score was " + str(self.p1Score) + " to " + str(self.p2Score) + ".")
		if self.p1Score > self.p2Score:
			print("Player 1 wins!")
		elif self.p1Score < self.p2Score:
			print("Player 2 wins!")
		else:
			print("Game was a draw.")
			
			
a = Main()	#to run main class

