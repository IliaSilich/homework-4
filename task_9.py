class CardDeck:
    def __init__(self):
        self.length = 52
        self.suits = ['clubs', 'diamonds', 'hearts', 'spades']
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        self.cards = [(suit, rank) for suit in self.suits for rank in self.ranks]
        self.index = 0

    def __next__(self):
        if self.index < self.length:
            card = self.cards[self.index]
            self.index += 1
            return f"{card[0]} {card[1]}"
        else:
            raise StopIteration

    def __iter__(self):
        return self


deck = CardDeck()
while True:
    print(next(deck))
