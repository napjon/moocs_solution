"""
The Zebra Puzzle

There are five houses.
The Englishman lives in the red house.
The Spaniard owns the dog.
Coffee is drunk in the green house.
The Ukrainian drinks tea.
The green house is immediately to the right of the ivory house.
The Old Gold smoker owns snails.
Kools are smoked in the yellow house.
Milk is drunk in the middle house.
The Norwegian lives in the first house.
The man who smokes Chesterfields lives in the house next to the man with the fox.
Kools are smoked in the house next to the house where the horse is kept.
The Lucky Strike smoker drinks orange juice.
The Japanese smokes Parliaments.
The Norwegian lives next to the blue house.

Question:
Who drinks water? Who owns the zebra?
Each house is painted a different color,
and their inhabitants are of different nationalities, own different pets,
drink different beverages and smoke different brands of American cigarettes.
    """

starts = 0
import itertools
import time


def imright(h1, h2):
    "House h1 is immediately right of h2 if h1-h2 == 1."
    return h1-h2 == 1#this one assure that h2 is exaclty next to h1

def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h1-h2) == 1#no matter left one or right it should be next

def zebra_puzzle():
    """Return a tuple (WATER, ZEBRA) indicating their house numbers."""
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]#Replace string with number in a list
    print houses
    orderings = list(itertools.permutations(houses)) #make a list of unordered houses
    #print list(orderings)
    return next((WATER, ZEBRA)#We use generator expression, what it does is yield one value
                #that pass all conditions below

                #Uses refactor, from for-for-if-if, to for-if-for-if
                for (red, green, ivory, yellow, blue) in (orderings)
                if imright(green, ivory)
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in (orderings)
                if Englishman is red
                if Norwegian is first
                if nextto(Norwegian, blue)
                for (coffee, tea, milk, oj, WATER) in (orderings)
                if coffee is green
                if Ukranian is tea
                if milk is middle
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in (orderings)
                if Kools is yellow
                if LuckyStrike is oj
                if Japanese is Parliaments
                for (dog, snails, fox, horse, ZEBRA) in (orderings)
                if Spaniard is dog
                if OldGold is snails
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                )


def c(sequence):#this sequence will
    c.starts += 1
    for item in sequence:
        items += 1
        yield item

def instrument_fn(fn, *args):
    starts, items = 0, 0
    result = fn(*args)
    print('%s got %s with %5d iters over %7d items'%(
        fn.__name__, result, c.starts, c.items))

print zebra_puzzle()

#rint instrument_fn(zebra_puzzle())