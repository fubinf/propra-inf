import random


def get_card(deck: list) -> tuple:
    """Randomly remove a single card from the deck and return it.
    Assumes the deck is not empty.

    deck: A deck as described above.

    Returns: a single card, which is a tuple with
    two elements, the rank and the suit.
    """

    index = int(len(deck) * random.random())
    new_card = deck[index]
    del deck[index]
    return new_card


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

    if len(deck) > 0:  # guard against an empty deck
        new_card = get_card(deck)
        card_rank, card_suit = new_card[0], new_card[1]

        if card_rank in player_hand:
            # append this suit to the list
            player_hand[card_rank].append(card_suit)
            if len(player_hand) == 4:
                print(f"{name} lays down {card_rank}")
                del player_hand[card_rank]
        else:
            # first of this suit, create a list with one element
            player_hand[card_rank] = [card_suit]
