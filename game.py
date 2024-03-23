from deck import Deck
from player import Player
from hand import Hand

"""

Game class can be modelled as the Subject with Player following
observer design pattern.

"""
class Game(object):
	"""Represents an instance of a poker game containing multiple hands
	Hands are defined in the hand.py class"""
	def __init__(self, stakes):
		self.numHands = 0
		self.Deck = self.initialize_deck()
		self.Players = []
		self.Stakes = stakes


	def initialize_deck(self):
		return Deck()
	
	def add_player(self, player):
		self.Players.append(player)

	def start_new_game(self):

		# initialize deck
		deck = Deck()
		
		while self.numHands < 10:

			# initialize players
			players = self.Players
			# start new hand
			hand = Hand(self.Stakes[0], self.Stakes[1], self.numHands)
			# assign dealer, smallBlind and bigBlind chips
			# logic of what goes on in each hand handled by Hand class
			hand.start_hand(players, deck)
			# end hand
			hand.end_hand()
			self.numHands += 1

			hand = None


		# initialize players
		# start new hand
		# assign dealer, smallBlind and bigBlind chips
		# logic of what goes on in each hand handled by Hand class
		# end hand
