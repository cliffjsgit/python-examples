from random import shuffle

class Card():
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "{} of {}".format(Card.rank_names[self.rank], Card.suit_names[self.suit])
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

class Deck():
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(suit, rank))
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    def pop_card(self):
        return self.cards.pop()
    def add_card(self, card):
        self.cards.append(card)
    def shuffle(self):
        shuffle(self.cards)
    def sort(self):
        self.cards.sort()
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return self.label + '\n' + '\n'.join(res)

##############################################################3
h1 = Hand('Hand 1')
h2 = Hand('Hand 2')
h3 = Hand('Hand 3')
h4 = Hand('Hand 4')
d1 = Deck()
print("\nBefore shuffle deck d1 =\n", d1)
d1.shuffle()
print("\nAfter shuffle deck d1 =\n", d1)

d1.move_cards(h1, 5)
print("\nMoved 5 cards from d1 to h1:\n", h1)
d1.move_cards(h2, 5)
print("\nMoved 5 cards from d1 to h2:\n", h2)
d1.move_cards(h3, 5)
print("\nMoved 5 cards from d1 to h3:\n", h3)
d1.move_cards(h4, 5)
print("\nMoved 5 cards from d1 to h4:\n", h4)

print("\nRemaining cards in deck, after deal of deck d1:\n", d1)