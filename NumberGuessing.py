import random

class NumberGuessing:

    def __init__(self) -> None:
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        print("You have 5 chances to guess the correct number.\n")

        self.__mode = "easy"
        self.__chances = 10
        self.__rand_num = random.randint(1, 100)

    def __switch_mode(self, mode : str) -> None:
        '''
            swicth to the mode (easy / medium / hard)

            Args:
                mode(str) : mode of the game

            Returns:
                None
        '''
        self.__mode = mode
        print(f"Great! You have selected the {mode.title()} difficulty level.")
        print("Let's start the game!\n")

        if mode == "easy":
            self.__chances = 10
        elif mode == "medium":
            self.__chances = 5
        elif mode == "hard":
            self.__chances = 3

    
    def play(self) -> None:
        '''
            Starts the game

            Args: None

            Returns: None
        '''
        print("Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n")
        ch = int(input("Enter your choice: "))

        match(ch):
            case 1:
                self.__switch_mode("easy")
            
            case 2:
                self.__switch_mode("medium")
            
            case 3:
                self.__switch_mode("hard")

            case _:
                print("Wrong choice!")
                exit()

        
        chances = 0

        while True:
            if chances == self.__chances:
                print("You're out of attempts!")
                exit()

            num = int(input("Enter your guess : "))
            chances += 1

            if num == self.__rand_num:
                print(f"Congratulations! You guessed the correct number in {chances} attempts.")
                exit()

            elif num > self.__rand_num:
                print(f"Incorrect! The number is less than {num}.")

            else:
                print(f"Incorrect! The number is greater than {num}.")
            
            print()


if __name__ == "__main__":
    game = NumberGuessing()
    game.play()
