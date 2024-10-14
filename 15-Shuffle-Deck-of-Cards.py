# shuffle of deck of cards:
import random, itertools
deck=list(itertools.product((1,14),["spade","club","hearts","diamond"]))
print(deck)
random.shuffle(deck)
print(deck)
for i in range(5):
    print(deck[i][0],"of", deck[i][1])