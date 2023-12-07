import random
# A function that prints the actual card
def printcard(suite, number):
    if int(number) < 10:
        print(f" _______")
        print(f"|{number}      |")
        print(f"|       |")
        print(f"|   {suite}   |")
        print(f"|       |")
        print(f"|______{number}|")
    else:
        print(f" _______")
        print(f"|{number}     |")
        print(f"|       |")
        print(f"|   {suite}   |")
        print(f"|       |")
        print(f"|_____{number}|")

suite = ["♥", "♦", "♣", "♠"]
number = [1,2,3,4,5,6,7,8,9,10,11,12,13]

cards = list()
for s in suite:
    for n in number:
        cards.append(f"{n} of {s}")
# The range function requires a range
shuffle = random.shuffle(cards)

for i in range(5):
    # print(cards[i])
    x = cards[i].split(" ")
    printcard(x[2],x[0])

