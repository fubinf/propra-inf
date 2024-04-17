import random


def draw_card(name: str, deck: list, player_hand: dict) -> None:
    """Draw a new card from the deck and add it to
    hand. If the hand now holds the rank in all four
    suits, then remove them from the hand.

    name: A string with the name of player_hand, used
          only for display purposes.
    deck: A deck as described above.
    hand: A hand dictionary as described above.

    Returns: None.
    """


def check_card(
    hand_name: str, player_hand: dict, card_rank: str, opponent_hand: dict
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


def do_turn(
    hand_name: str, deck: list[tuple], player_hand: dict, opponent_hand: dict
) -> None:
    """Play one turn of 'Go Fish'. A rank in player_hand is chosen,
    and if any cards of that rank exist in opponent_hand, they are transferred.
    This continues until no cards are transferred,
    at which point a new card is drawn from the deck into player_hand.

    hand_name: A string with the name of player_hand.
    deck: The current deck, a list of two-element tuples of the form (rank, suit).
    player_hand: A hand dictionary.
    opponent_hand: A hand dictionary.

    Returns: None.
    """

    """ Loop unless the player_hand is empty. Normally this loop exits via the break statement,
        when check_card() returns false meaning a card was not transferred.
    """

    while len(player_hand):
        """Pick a random index within the current hand..."""
        index = int(len(player_hand) * random.random())

        """ ...and use the rank of the card at that index as the one to ask for.
        """
        rank_to_check = list(player_hand.keys())[index]
        found = check_card(hand_name, opponent_hand, rank_to_check, player_hand)

        if not found:
            break

    # no transfer, so "go fish"
    draw_card(hand_name, deck, player_hand)


ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["spades", "hearts", "diamonds", "clubs"]


def play_go_fish() -> None:
    """Initialization and loop of the game 'Go Fish'."""

    deck: list[tuple] = []
    hand1 = {}
    hand2 = {}

    for i in range(52):
        deck.append((ranks[i % 13], suits[i % 4]))

    for i in range(7):
        draw_card("HAND1", deck, hand1)
        draw_card("HAND2", deck, hand2)

    while True:
        do_turn("HAND1", deck, hand1, hand2)
        do_turn("HAND2", deck, hand2, hand1)

        if len(hand1) == 0 and len(hand2) == 0:
            break
