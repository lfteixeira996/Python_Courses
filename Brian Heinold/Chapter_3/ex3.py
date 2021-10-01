"""
Some board games require you to reduce the number of cards you are holding by half, rounded
down. For instance, if you have 10 cards, you would reduce to 5 and if you had 11 cards you would
also reduce to 5. With 12 cards you would reduce to 6. Write a program that asks the user to enter
how many cards they have and print out what their hand would reduce to under this rule.
"""

cards = eval(input("How many cards: "))

print("Cards: ", int(cards/2))