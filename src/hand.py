class Hand(object):
    """Represents a hand in a poker game.

    Attributes:
        Small Blind (int): The small blind amount.
        Big Blind (int): The big blind amount.
    """

    def __init__(self, small_blind, big_blind, num_hands):
        self.smallBlind = small_blind 
        self.bigBlind = big_blind
        self.communityCards = []
        self.currentBet = 0
        self.Pot = self.smallBlind + self.bigBlind
        self.players_in_hand = []
        self.smallBlindIndex = 0 + num_hands
        self.bigBlindIndex = 1 + num_hands
        self.trick_dict = {9: "Straight Flush", 8: "Four of a Kind", 7: "Full House", 6: "Flush", 5: "Straight", 4: "Three of a Kind", 3: "Two Pair", 2: "Pair", 1: "High Card"}
                           
	
    def start_hand(self, players, deck):
        """
        Starts a new hand in the poker game.

        Args:
            players: A list of players participating in the hand.
            deck: The deck of cards used in the game.
            stakes: A list of the stakes for the hand.

        Returns:
            None
        """
        self.players_in_hand = players
        deck.shuffle()
        self.currentBet = self.bigBlind
        self.set_blinds(players)

        self.deal_cards(players, deck)

        betting_rounds = ["PreFlop", "PostFlop", "PostTurn", "PostRiver"]
        
        for betting_round in betting_rounds:
            # Reset current bet if new round
            if betting_round != "PreFlop":
                self.currentBet = 0

            # Run betting round and deal community cards
            if len(self.players_in_hand) > 1 and len(self.communityCards) < 5:
                self.run_betting_round(betting_round)
                
                if betting_round == "PreFlop":
                    self.communityCards += deck.pick_n_cards(3)
                else:
                    self.communityCards += deck.pick_n_cards(1)
                print("Community Cards: ", self.communityCards)
            
            # one betting round after the river card is dealt i.e 5 community cards on the table
            elif betting_round == "PostRiver":
                self.run_betting_round(betting_round)

            # If only one player left in the hand, end the hand
            else:
                self.end_hand()
                return

        self.end_hand()

    def one_player_left(self):
        """
        Checks if only one player is left in the hand.

        Args:
            None

        Returns:
            bool: True if only one player is left in the hand, False otherwise.
        """
        return len(self.players_in_hand) == 1

    def end_hand(self):
        """
        Ends the current hand in the poker game.

        Args:
            None

        Returns:
            None
        """
        # Determine winner
        if self.one_player_left():
            winner = self.players_in_hand[0]
        else:
            winner = self.determine_winner()
        print(winner.Name + " wins the hand with a " + self.trick_dict[winner.trick] + " and wins " + self.Pot + " chips!")
        winner.ChipStack += self.Pot
        self.Pot = 0
        self.communityCards = []
        self.currentBet = 0
        self.players_in_hand = []
        
    
    def determine_winner(self):
        """
        Determines the winner of the current hand in the poker game.

        Args:
            None

        Returns:
            Player: The player who won the hand.
        """
        # Determine winner
        winner = self.players_in_hand[0]
        winner.get_hand_rank(self.communityCards)
        for player in self.players_in_hand:
            player.trick = player.get_hand_rank(self.communityCards)
            if player.trick > winner.trick:
                winner = player
        return winner


    def run_betting_round(self, betting_round):
        players = [p for p in self.players_in_hand]
        for player in players:
            print("Pot: ", self.Pot)
            print("Current Bet: ", self.currentBet)
            print("Your Chip Stack: ", player.ChipStack)
            print("Your Bet: ", player.get_curr_bet(betting_round))

            move = input(player.Name + ", what would you like to do? (check, fold, call, bet) ")
            
            while self.check_invalid_move(player, move, betting_round):
                print("Invalid move, please try again: ")
                move = input(player.Name + ", what would you like to do?")

            if move not in ["check", "fold", "call"]:
                mv = move.split(" ")
                amount = mv[1]
                self.currentBet = amount
                player.bet(betting_round, int(amount))
                self.Pot += amount
            elif move == "call":
                self.Pot += (self.currentBet - player.get_curr_bet(betting_round))
                player.call(betting_round, self.currentBet)
            elif move == "check":
                player.check()
            elif move == "fold":
                player.fold()
                self.players_in_hand.remove(player)
	

    def check_invalid_move(self, player, move, betting_round):
        moves = ["check", "call", "fold", "bet"]
        move_amt = move.split(" ")
        
        if len(move_amt) == 2:
            move = move_amt[0]
            amount = move_amt[1]

        return move not in moves or \
                (self.currentBet > player.get_curr_bet(betting_round) and move == "check") or \
                    (move == "call" and player.ChipStack < self.currentBet) or \
                        (move == "bet" and (player.ChipStack < self.currentBet or int(amount) < self.currentBet)) or \
                            (move == "call" and player.isBigBlind == True and betting_round == "PreFlop")


    def set_blinds(self, players):
        """
        Assigns small blind and big blind to two players and reduces the amount from their stacks.

        Args:
            players: A list of players participating in the hand.

        Returns:
            None
        """
        # Assign small blind
        small_blind_player = players[self.smallBlindIndex]
        small_blind_player.ChipStack -= self.smallBlind
        small_blind_player.isSmallBlind = True
        small_blind_player.bet("PreFlop", self.smallBlind)

        # Assign big blind
        big_blind_player = players[self.bigBlindIndex]
        big_blind_player.ChipStack -= self.bigBlind
        big_blind_player.isBigBlind = True
        big_blind_player.bet("PreFlop", self.bigBlind)

    def deal_cards(self, players, deck):
        """
        Deals two cards to each player participating in the hand.

        Args:
            players: A list of players participating in the hand.
            deck: The deck of cards used in the game.

        Returns:
            None
        """
        for player in players:
            player.Cards = deck.deal_cards(player)