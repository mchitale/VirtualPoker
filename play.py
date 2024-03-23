from game import Game
from player import Player


# initialize all the players
player1 = Player("aurora", 2000)
player2 = Player("charlie", 4500)
player3 = Player("richard", 1500)
player4 = Player("chloe", 2000)

# initialize game
# stakes = 5/10
game = Game([5,10])	

# add all the players
game.add_player(player1)
game.add_player(player2)
game.add_player(player3)
game.add_player(player4)

# start the game with given players and stakes
game.start_new_game()