def check_card(
    name_of_hand: str, hand_of_player: dict, rank_of_card: str, hand_of_opponent: dict
) -> bool:
    """Check if opponent_hand contains any cards of the
    specified rank, if it does, transfer them to player_hand.

    hand_name: A string with the name of player_hand
    player_hand: A hand dictionary, as described above
    card_rank: A string with the name of a
               card rank ("2" through "10", "J", "Q", "K, or "A")
    opponent_hand: A hand dictionary, as described above

    Returns: True if a card is transferred, False otherwise
    """

    if rank_of_card in hand_of_opponent:
        transfer_cards: list = hand_of_opponent[rank_of_card]
        # transfer_cards is a list!
        del hand_of_opponent[rank_of_card]
        if rank_of_card in hand_of_player:
            hand_of_player[rank_of_card].extend(transfer_cards)
        else:  # shouldn't happen, but handle it
            hand_of_player[rank_of_card] = transfer_cards

        if len(hand_of_player[rank_of_card]) == 4:
            print(f"{name_of_hand} lays down {rank_of_card}")
            del hand_of_player[rank_of_card]

            return True
        else:
            return False


hand_name = "HAND"
player_hand = {"5": ["spades", "hearts"]}
card_rank = "5"
opponent_hand = {"6": ["diamonds"], "10": ["clubs"]}

print(f"hand -> {player_hand}")
print(check_card(hand_name, player_hand, card_rank, opponent_hand))
print(f"hand -> {player_hand}")

