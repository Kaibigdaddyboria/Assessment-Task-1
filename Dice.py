import random
#Makes the code repeatable
while True:
    dierolled = input("Would you like to roll 1 or 2 die? ")
    #Determines if the users input is valid
    if dierolled.isdigit:
        #Processes the users response and responds accordingly
        if dierolled == "1":
            result1 = random.randint(1, 6)
            print(f"You rolled a {result1}!")
        elif dierolled == "2":
            result1 = random.randint(1, 6)
            result2 = random.randint(1, 6)
            total = result1 + result2
            print(f"You rolled a {result1} and a {result2}! Which is a total of {total}")
        else:
            print("Invalid input")
            continue            
    else:
        print("Input number")
    #Presents an option to re-roll to the user
    reroll = input("Would you like to re-roll? (please answer yes or no) ")
    #Processes the users response and responds accordingly
    if reroll == "yes":
        continue
    else:
        print("Thanks for using this dice simulator")
        break
