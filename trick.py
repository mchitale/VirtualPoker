class Trick:
    def __init__(self):
        self.player_cards = []
        self.communityCards = []


    def get_trick(self, player_cards, community_cards):

        self.player_cards = player_cards
        self.communityCards = community_cards

        # Determine trick
        trick = 0
		# Add player's cards to community cards
        all_cards = self.player_cards + self.communityCards
        # Sort cards by value
        all_cards.sort(key=lambda x: x.value)
        # Check for straight flush
        if self.check_straight_flush(all_cards):
            trick = 9
        # Check for four of a kind
        elif self.check_four_of_a_kind(all_cards):
            trick = 8
        # Check for full house
        elif self.check_full_house(all_cards):
            trick = 7
        # Check for flush
        elif self.check_flush(all_cards):
            trick = 6
        # Check for straight
        elif self.check_straight(all_cards):
            trick = 5
        # Check for three of a kind
        elif self.check_three_of_a_kind(all_cards):
            trick = 4
        # Check for two pair
        elif self.check_two_pair(all_cards):
            trick = 3
        # Check for pair
        elif self.check_pair(all_cards):
            trick = 2
        # High card
        else:
            trick = 1
        return trick

    def check_straight_flush(self, all_cards):
        # Check for straight flush
        if self.check_flush(all_cards) and self.check_straight(all_cards):
            return True
        return False
    
    def check_four_of_a_kind(self, all_cards):
        # Check for four of a kind
        for i in range(0, len(all_cards) - 3):
            if all_cards[i].value == all_cards[i + 1].value == all_cards[i + 2].value == all_cards[i + 3].value:
                return True
        return False
    
    def check_full_house(self, all_cards):
        # Check for full house
        if self.check_three_of_a_kind(all_cards) and self.check_pair(all_cards):
            return True
        return False
    
    def check_flush(self, all_cards):
        # Check for flush
        suits = [card.suit for card in all_cards]
        for suit in suits:
            if suits.count(suit) >= 5:
                return True
        return False
    
    def check_straight(self, all_cards):
        # Check for straight
        for i in range(0, len(all_cards) - 4):
            if all_cards[i].value == all_cards[i + 1].value - 1 == all_cards[i + 2].value - 2 == all_cards[i + 3].value - 3 == all_cards[i + 4].value - 4:
                return True
        return False
    
    def check_three_of_a_kind(self, all_cards):
        # Check for three of a kind
        for i in range(0, len(all_cards) - 2):
            if all_cards[i].value == all_cards[i + 1].value == all_cards[i + 2].value:
                return True
        return False
    
    def check_two_pair(self, all_cards):
        # Check for two pair
        pairs = 0
        for i in range(0, len(all_cards) - 1):
            if all_cards[i].value == all_cards[i + 1].value:
                pairs += 1
        if pairs >= 2:
            return True
        return False
    
    def check_pair(self, all_cards):
        # Check for pair
        for i in range(0, len(all_cards) - 1):
            if all_cards[i].value == all_cards[i + 1].value:
                return True
        return False
    
        
    
