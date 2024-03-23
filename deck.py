import random


values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',\
'Jack', 'Queen', 'King']
suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']

class Card(object):
	"""docstring for ClassName"""
	def __init__(self, value, suit):

		self.value = value
		self.suit = suit
		
class Deck(object):
	"""Represents a deck of playing cards.

	Attributes:
		deck (list): A list of Card objects representing the deck of cards.
	"""

	def __init__(self):
		self.card_deck = [Card(value, suit) for value in values for suit in suits]

	def shuffle(self):
		"""Shuffles the deck of cards."""
		random.shuffle(self.card_deck)

	def deal_cards(self, player):
		"""Deals cards to a player.

		Args:
			player (Player): The player object to deal cards to.

		Returns:
			list: A list of cards dealt to the player.
		"""
		cards = []
		cards.append(self.card_deck.pop())
		cards.append(self.card_deck.pop())
		return cards

	def burn_card(self):
		"""Removes the top card from the deck."""
		self.card_deck.pop()

	def pick_n_cards(self, num_cards):
		"""Picks a specified number of cards from the deck.

		Args:
			numCards (int): The number of cards to pick.

		Returns:
			list: A list of picked cards.
		"""
		cards = []
		for _ in range(0, num_cards):
			cards.append(self.card_deck.pop())
		return cards





