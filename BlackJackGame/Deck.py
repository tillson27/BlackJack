from random import shuffle

class Deck():

    def __init__(self, cards):
        self.cards = cards

    def new_deck(self):
        self.cards = ["King of Hearts", "Queen of Hearts", "Jack of Hearts", "Ace of Hearts",
                      "Two of Hearts", "Three of Hearts", "Four of Hearts", "Five of Hearts",
        "Six of Hearts", "Seven of Hearts", "Eight of Hearts", "Nine of Hearts", "Ten of Hearts",
        "King of Spades", "Queen of Spades", "Jack of Spades", "Ace of Spades",
                      "Two of Spades", "Three of Spades", "Four of Spades", "Five of Spades",
        "Six of Spades", "Seven of Spades", "Eight of Spades", "Nine of Spades", "Ten of Spades",
        "King of Diamonds", "Queen of Diamonds", "Jack of Diamonds", "Ace of Diamonds",
         "Two of Diamonds", "Three of Diamonds", "Four of Diamonds", "Five of Diamonds",
        "Six of Diamonds", "Seven of Diamonds", "Eight of Diamonds", "Nine of Diamonds", "Ten of Diamonds",
        "King of Clubs", "Queen of Clubs", "Jack of Clubs", "Ace of Clubs",
         "Two of Clubs", "Three of Clubs", "Four of Clubs", "Five of Clubs",
        "Six of Clubs", "Seven of Clubs", "Eight of Clubs", "Nine of Clubs", "Ten of Clubs"]

        shuffle(self.cards)

    def starting_cards(self):
        shuffle(self.cards)
        player_card1 = Card(value = self.cards.pop())
        player_card2 = Card(value = self.cards.pop())

        dealer_upcard = Card(value = self.cards.pop())
        dealer_downcard = Card(value = self.cards.pop())

    def hit(self):
        shuffle(self.cards)
        card = Card(value = self.cards.pop())
        return card
