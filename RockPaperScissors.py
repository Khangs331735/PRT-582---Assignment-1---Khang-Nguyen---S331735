import random


class RockPaperScissors(object):

    def __init__(self):

        # initialise the variables for the scoring purpose

        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.total_round = 0

        #create a list for player and computer choose

        self.options = ['rock', 'paper', 'scissors'] 

    def player_option(self):
        user_choice = input("Please Choose: rock, paper or scissors ?").lower()

        if user_choice not in self.options:
            print("Invalid input. Please choose again!")
            # return invalid if the input is not the same as self.options
        return user_choice

    def computer_choice(self):
        """
        Chooses a choice randomly from the keys in self.options.
        :returns: String containing the choice of the computer.
        """

        return random.choice(self.options)

    def counting_score(self):

        #take the input from player and choice from computer

        computer = self.computer_choice()
        player = self.player_option()

        #counting score starts here + number of rounds

        if player == computer:
            self.ties += 1
            self.total_round += 1
            print(f"You've chosen {player}, and the computer chose {computer}. The game is a tie!!!")

        elif player == "rock":
            if computer == "paper":
                self.losses += 1
                self.total_round += 1
                print(f"You've chosen {player}, and the computer chose {computer}. You Lose!!!")
            if computer == "scissors":
                self.wins += 1
                self.total_round += 1
                print(f"You've chosen {player}, and the computer chose {computer}. You Win!!!")

        elif player == "paper":
            if computer == "rock":
                self.wins += 1
                self.total_round += 1
                print(f"You've chosen {player}, and the computer chose {computer}. You Win!!!")
            if computer == "scissors":
                self.losses += 1
                self.total_round += 1
                print(f"You've chosen {player}, and the computer chose {computer}. You Lose!!!")

        elif player == "scissors":
            if computer == "paper":
                self.wins += 1
                self.total_round += 1
                print(f"You've chosen {player}, and the computer chose {computer}. You Win!!!")
            if computer == "rock":
                self.losses += 1
                self.total_round += 1
                print(f"You've chosen {player}, and the computer chose {computer}. You Lose!!!")

    def continue_game(self):

        #while loop to determine whether the players want to quit with condition

        while True:
            if self.wins < 5 and self.losses < 5:
                continue_prompt = input('\nDo you wish to play again? (y/n): ').lower()
                if continue_prompt == 'n':
                    print("You have Quit the game!")
                    exit()
                elif continue_prompt == 'y':
                    return False
                else:
                    print("Invalid input!\n")
                    continue
            elif self.wins == 5 or self.losses == 5:
                if self.wins == 5:
                    win_ask = input('\nYou have Won!!! Do you wish to restart the game? (y/n): ').lower()
                    if win_ask == "n":
                        print("You have Exit the game")
                        exit()
                    elif win_ask == "y":
                        return self.__init__()
                    else:
                        print("Invalid Input")
                        continue
                elif self.losses == 5:
                    lose_ask = input('\nYou have Lose!!! Do you wish to restart the game? (y/n):').lower()
                    if lose_ask == "n":
                        print("You have Exit the game")
                        exit()
                    elif lose_ask == "y":
                        return self.__init__()
                    else:
                        print("Invalid Input")
                        continue

    def print_score(self):
        
        #display the scores: wins, loses, ties and total number of rounds

        print(f"You have {self.wins} wins, {self.losses} losses, and {self.ties} ties. The total round: {self.total_round}")


if __name__ == "__main__":
    game = RockPaperScissors()
    while True:
        game.counting_score()
        game.print_score()
        game.continue_game()
