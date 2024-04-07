# Unit tests for Hand class
def test_hand():
    # Initialize players
    player1 = Player("aurora", 2000)
    player2 = Player("charlie", 4500)
    player3 = Player("richard", 1500)
    player4 = Player("chloe", 2000)
    players = [player1, player2, player3, player4]

    # Initialize hand
    hand = Hand(5, 10, 0)

    # Test set_blinds
    hand.set_blinds(players)
    assert player1.isSmallBlind == True
    assert player2.isBigBlind == True
    assert player1.ChipStack == 1995
    assert player2.ChipStack == 4490

    # Test deal_cards
    deck = Deck()
    hand.deal_cards(players, deck)
    assert len(player1.Cards) == 2
    assert len(player2.Cards) == 2
    assert len(player3.Cards) == 2
    assert len(player4.Cards) == 2

    # Test one_player_left
    assert hand.one_player_left() == False

    # Test determine_winner
    winner = hand.determine_winner()
    assert winner == player2

    # Test run_betting_round
    hand.run_betting_round("PreFlop")
    assert player1.get_curr_bet("PreFlop") == 5
    assert player2.get_curr_bet("PreFlop") == 10
    assert player3.get_curr_bet("PreFlop") == 0
    assert player4.get_curr_bet("PreFlop") == 0

    # Test check_invalid_move
    assert hand.check_invalid_move(player1, "bet 3", "PreFlop") == True
    assert hand.check_invalid_move(player1, "call", "PreFlop") == True
    assert hand.check_invalid_move(player1, "fold", "PreFlop") == False
    assert hand.check_invalid_move(player1, "check", "PreFlop") == False

    print("All tests pass!")