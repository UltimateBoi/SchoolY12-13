"""
Write a game where there are 2 players that can input up to 3 numbers in ascending order separated by a , e.g. 1,2,3 and 4,5 and 6 and 7,8,9 etc.
each turn and will keep going until one person has to enter 15 or enters 
15 and then they will loose the game.
"""

def main():
    won = False
    turn = 1
    last_number = 0

    while not won:
        choice = input(f"Player {'2' if turn % 2 == 0 else '1'} enter up to 3 numbers in ascending order separated by a comma: ").split(",")
        choice = [int(num) for num in choice if num.isdigit()]

        if 0 < len(choice) <= 3 and all(choice[i] < choice[i + 1] for i in range(len(choice) - 1)) and choice[0] > last_number:
            last_number = choice[-1]
            if last_number == 15:
                print(f"Player {'2' if turn % 2 == 0 else '1'} loses!")
                won = True
            else:
                turn += 1
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()