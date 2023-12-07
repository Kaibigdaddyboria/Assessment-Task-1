
while True:
    play = input("Would you like me to sing the song '99 bottle of beer on the wall'? ")
    #Processes the users response and responds accordingly
    if play == "yes":
        bottles = 100
        #Prints the correct amount of lyrics
        while bottles > 2:            
            icons = bottles + 1
            #Prints the correct amount of 🍺
            while icons > 1:
                print("🍺", end="")
                icons = icons - 1
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            bottles = bottles - 1
            print (f"Take one down, pass it around, {bottles} bottles of beer on the wall")
            continue
        #Prints the rest of the lyrics
        print("🍺🍺2 bottles of beer on the wall, 2 bottles of beer.")
        print("Take one down pass it around 1 bottle of beer on the wall")
        print("🍺1 bottle of beer on the wall, one bottle of beer. ")
        print("Take one down pass it around no more bottles of beer on the wall.")    
    else:
        print("Are you sure?")
        continue
