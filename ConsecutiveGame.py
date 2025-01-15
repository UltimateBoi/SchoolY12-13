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
        choice = input(f"Player {'2' if turn % 2 == 0 else '1'} enter up to 3 numbers in ascending order separated by a comma: ").split(",") # Logic for if statement is because turn starts at 1 and therefore player 1 will always have an odd turn number
        choice = [int(num) for num in choice if num.isdigit()] # convert the input into a list of integers

        if 0 < len(choice) <= 3 and all(choice[i] < choice[i + 1] for i in range(len(choice) - 1)) and choice[0] > last_number and all(num <= 15 for num in choice): # check if the input is valid by checking if the length of the input is between 1 and 3, if the numbers are in ascending order, if the first number is greater than the last number, and if all numbers are less than or equal to 15
            last_number = choice[-1] # set the last number to the last number in the input
            if last_number == 15:
                print(f"Player {'2' if turn % 2 == 0 else '1'} loses!") # player 1 will always have an odd turn number and player 2 even
                won = True # set won to True if a player loses so that the while loop will break
            else:
                turn += 1 # increment turn if the players turn is correctly iterated through
        else:
            print("Invalid input. Please try again.")

# if __name__ == "__main__":
    # main() # Disabled for now to test object oriented approach below \/ (not commented as in depth as it is the same as above)

class ConsecutiveGame:
    def __init__(self):
        self.won = False
        self.turn = 1
        self.last_number = 0

    def play_turn(self):
        choice = input(f"Player {'2' if self.turn % 2 == 0 else '1'} enter up to 3 numbers in ascending order separated by a comma: ").split(",")
        choice = [int(num) for num in choice if num.isdigit()] # convert the input into a list of integers by using list comprehension

        if 0 < len(choice) <= 3 and all(choice[i] < choice[i + 1] for i in range(len(choice) - 1)) and choice[0] > self.last_number and all(num <= 15 for num in choice):
            self.last_number = choice[-1]
            if self.last_number == 15:
                print(f"Player {'2' if self.turn % 2 == 0 else '1'} loses!")
                self.won = True
            else:
                self.turn += 1
        else:
            print("Invalid input. Please try again.")

    def start_game(self):
        while not self.won:
            self.play_turn()

if __name__ == "__main__":
    game = ConsecutiveGame()
    game.start_game() # begin game while loop



def short_main():
    won, turn, last_number = False, 1, 0
    while not won:
        choice = [int(num) for num in input(f"Player {'2' if turn % 2 == 0 else '1'} enter up to 3 numbers in ascending order separated by a comma: ").split(",") if num.isdigit()]
        if 0 < len(choice) <= 3 and all(choice[i] < choice[i + 1] for i in range(len(choice) - 1)) and choice[0] > last_number and all(num <= 15 for num in choice):
            last_number = choice[-1]
            if last_number == 15:
                print(f"Player {'2' if turn % 2 == 0 else '1'} loses!")
                won = True
            else: turn += 1
        else: print("Invalid input. Please try again.")