playerChoice = []
turns = 0
gameEnd = 0

while gameEnd == 0:
    numLen = int(input("How many numbers would you like to choose (1-3): "))
    if numLen > 3 or numLen < 1:
        print("Invalid choice")
    else:
        choice = input(f"Enter up to {numLen} numbers in ascending order separated by commas e,g, 1,2,3 or 4,6,8: ")
        playerChoice = choice.split(",")
        playerChoice = [int(num) for num in playerChoice]
        if playerChoice != sorted(playerChoice):
            print("Invalid choice, not in ascending order")
        elif any(int(num) == 15 for num in playerChoice):
            if turns % 2 != 0:
                print("Player 1 wins")
            else:
                print("Player 2 wins")
                gameEnd = 1
        else:
            print("You have chosen " + str(playerChoice))
            turns += 1