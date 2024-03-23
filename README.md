# Virtual Poker

This repository contains the implementation of a bare-bones version of the game logic for Virtual Poker. The purpose of this project is to help understand the rules and mechanics of poker by designing and implementing a simplified version of the game.

## Entities

### Card

- Properties:
	- `value`: Represents the value of the card (Ace to King)
	- `suit`: Represents the suit of the card (S, D, H, C)

### Deck

- Properties:
	- `deck`: Represents a collection of cards in the deck

- Methods:
	- `shuffle()`: Shuffles the deck in place
	- `dealCards(player)`: Deals 2 cards to a player
	- `burn_card()`: Burns a card before dealing turn/flop/river card
	- `pick(numCards)`: Draws a specified number of cards from the deck

### Player

- Properties:
	- `ChipStack`: Represents the number of chips the player has remaining
	- `Cards`: Represents the cards dealt to the player

- Methods:
	- `bet(amount)`: Places a bet with the specified amount
	- `call(amount)`: Calls a bet with the specified amount
	- `check()`: Checks without placing a bet
	- `fold()`: Folds the player's hand
	- `showCards()`: Shows the player's cards

### Hand

- Properties:
	- `Deck`: Represents the deck of cards
	- `Players`: Represents the players in the hand
	- `smallBlind`: Represents the small blind amount
	- `bigBlind`: Represents the big blind amount
	- `communityCards`: Represents the community cards
	- `Pot`: Represents the total pot amount

- Methods:
	- `start_hand()`: Starts a new hand
	- `preflop()`: Executes the preflop phase
	- `end_hand()`: Ends the current hand

### Game

- Properties:
	- `numHands`: Represents the number of hands played
	- `Players`: Represents the players in the game
	- `Deck`: Represents the deck of cards
	- `Ante`: Represents the ante amount

- Methods:
	- `Game()`: Constructor to initialize the game
	- `initializeDeck()`: Initializes the deck of cards
	- `newHand()`: Starts a new hand
	- `start_game()`: Starts the game
	- `incrementHands()`: Increments the number of hands played
	- `updateBlinds()`: Updates the blind amounts
