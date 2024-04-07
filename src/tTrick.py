# Write a unit test for the Trick class
class TestTrick(unittest.TestCase):
    def setUp(self):
        self.trick = Trick()
        self.player_cards = [Card('2', 'Hearts'), Card('3', 'Hearts')]
        self.community_cards = [Card('4', 'Hearts'), Card('5', 'Hearts'), Card('6', 'Hearts'), Card('7', 'Hearts'), Card('8', 'Hearts')]

    def test_get_trick(self):
        self.assertEqual(self.trick.get_trick(self.player_cards, self.community_cards), 9)

    def test_check_straight_flush(self):
        self.assertTrue(self.trick.check_straight_flush(self.player_cards + self.community_cards))

    def test_check_four_of_a_kind(self):
        self.assertFalse(self.trick.check_four_of_a_kind(self.player_cards + self.community_cards))

    def test_check_full_house(self):
        self.assertFalse(self.trick.check_full_house(self.player_cards + self.community_cards))

    def test_check_flush(self):
        self.assertTrue(self.trick.check_flush(self.player_cards + self.community_cards))

    def test_check_straight(self):
        self.assertTrue(self.trick.check_straight(self.player_cards + self.community_cards))

    def test_check_three_of_a_kind(self):
        self.assertFalse(self.trick.check_three_of_a_kind(self.player_cards + self.community_cards))

    def test_check_two_pair(self):
        self.assertFalse(self.trick.check_two_pair(self.player_cards + self.community_cards))

    def test_check_pair(self):
        self.assertFalse(self.trick.check_pair(self.player_cards + self.community_cards))

        
