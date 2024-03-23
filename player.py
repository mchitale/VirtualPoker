from trick import Trick
"""

This may need to be modelled as an observer class.
With game being the subject. 

"""
class Player(object):
	"""docstring for ClassName"""
	def __init__(self, name, chip_stack):
		self.Name = name
		self.ChipStack = chip_stack
		self.Cards = []
		self.betPreFlop = 0
		self.betPostFlop = 0
		self.betPostTurn = 0
		self.betPostRiver = 0
		self.trick = Trick()
		self.isBigBlind = False
		self.isSmallBlind = False

	def bet(self, betting_round, amount):
		self.ChipStack -= amount
		if betting_round == "PreFlop":
			self.betPreFlop += amount
		elif betting_round == "PostFlop":
			self.betPostFlop += amount
		elif betting_round == "PostTurn":
			self.betPostTurn += amount
		elif betting_round == "PostRiver":
			self.betPostRiver += amount
		else:
			print("Invalid Bet")
		print(self.Name+" bets $"+str(amount))

	def call(self, betting_round, amount):

		if betting_round == "PreFlop":
			self.betPreFlop += amount
		elif betting_round == "PostFlop":
			self.betPostFlop += amount
		elif betting_round == "PostTurn":
			self.betPostTurn += amount
		elif betting_round == "PostRiver":
			self.betPostRiver += amount
		else:
			print("Invalid Bet")

		self.ChipStack -= amount
		print(self.Name+" calls")


	def check(self):
		print(self.Name+" checks")

	def fold(self):
		self.Cards = []
		self.betPreFlop = 0
		self.betPostFlop = 0
		self.betPostTurn = 0
		self.betPostRiver = 0

		print(self.Name+" folds.")

	def show_cards(self):
		print(self.Name+"'s cards are:")
		for card in self.Cards:
			print(card.value+" of"+ card.suit)
	
	def get_trick(self, community_cards):
		"""
		Args:
			communityCards (list): A list of Card objects representing the community cards.
		
		Returns:
			int: The trick value of the player's hand.
		"""
		return self.trick.get_trick(self.Cards, community_cards)

	def get_curr_bet(self, betting_round):
		if betting_round == "PreFlop":
			return self.betPreFlop
		elif betting_round == "PostFlop":
			return self.betPostFlop
		elif betting_round == "PostTurn":
			return self.betPostTurn
		elif betting_round == "PostRiver":
			return self.betPostRiver
		else:
			print("Invalid Bet")
		






		