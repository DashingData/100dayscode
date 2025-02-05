# Program to shuffle a deck of card

import random , itertools
deck = list(itertools.product(range(1 , 14) , ["Spade" , "Club" , "heart" , "diamond"]))
print(deck)

random.shuffle(deck)

print(deck)

for i in range(5):
    print()


for i in range(5):
    print(deck[i][0] , "of" , deck[i][1])