# Python program to shuffle a deck of card

# importing modules
import itertools, random

# make a deck of cards... itertools.product cartesian product from given range with given list of cards item 
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards

# each player draws 13 cards
print("----------------GAME BEGINS------------------")
print("******PLAYER 1******")
print("You got:")
for i in range(13):
    random.shuffle(deck)
    print(deck[i][0], "of", deck[i][1])

print("******PLAYER 2******")
print("You got:")
for i in range(13):
    random.shuffle(deck)
    print(deck[i][0], "of", deck[i][1])
