import collections

Card = collections.namedtuple('Card', 'rank, suit')


class FrenchDeck:

    ranks = [r for r in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def rank_spades_high(self, card):
        rank_value = self.ranks.index(card.rank)
        derived_rank_value = rank_value * len(self.suit_values) + self.suit_values[card.suit]
        print(f'derived_rank_value={derived_rank_value}')
        return derived_rank_value

