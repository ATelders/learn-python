import random

deck = []

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

for  suit in suits:
    for rank in ranks:
      deck.append(f'{rank} of {suit}')

print('There are', len(deck), 'cards in the deck')

deal = []
selected_card = 0

print('Dealing...')
while len(deal) < 5:
    selected_card = random.choice(deck)
    deal.append(selected_card)
    deck.remove(selected_card)

print('There are', len(deck), 'cards in the deck')
print('Player has the following cards in their hand: ')
print(deal)
