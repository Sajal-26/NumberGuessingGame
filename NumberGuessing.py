import random
import json
import time
import os

class NumberGuessing:
    '''
        project link : https://roadmap.sh/projects/number-guessing-game
    '''

    def __init__(self) -> None:
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        self.__path = os.path.abspath(os.path.join(os.path.dirname(__file__), "hs.json"))
        if not os.path.exists(self.__path):
            with open(self.__path, 'w') as f:
                json.dump({
                    'high-score' : 0
                }, f, indent = 4)

        self.__chances = 10
        self.__score = 0
        self.__rand_num = random.randint(1, 100)

    def __switch_mode(self, mode : str) -> None:
        '''
            swicth to the mode (easy / medium / hard)

            Args:
                mode(str) : mode of the game

            Returns:
                None
        '''
        print(f"Great! You have selected the {mode.title()} difficulty level.")

        if mode == "easy":
            self.__chances = 10
        elif mode == "medium":
            self.__chances = 5
        elif mode == "hard":
            self.__chances = 3

        print(f"You have {self.__chances} chances to guess the correct number.\n")
        print("Let's start the game!\n")

    
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
                print("Wrong choice!\nTry again!\n")
                self.play()
                

        
        chances = 0
        t = time.time()

        while True:
            if chances == self.__chances:
                print("You're out of attempts!\nThe number was ", self.__rand_num)
                print(f"Time elapsed : {(time.time() - t):.2f} sec\n")
                break

            num = int(input("Enter your guess : "))
            chances += 1

            if num == self.__rand_num:
                self.__score += 1
                print(f"Congratulations! You guessed the correct number in {chances} attempts.")
                print(f"Total Score : {self.__score}")
                print(f"Guessed in : {(time.time() - t):.2f} sec\n")
                break

            if chances == self.__chances:
                print("You're out of attempts!\nThe number was ", self.__rand_num)
                print(f"Time elapsed : {(time.time() - t):.2f} sec\n")
                break

            if num > self.__rand_num:
                print(f"Incorrect! The number is less than {num}.")

            else:
                print(f"Incorrect! The number is greater than {num}.")

            print()


        while True:
            optn = input("Do you want to play more? (Y/N) : ").lower()
            if optn == 'y':
                self.__rand_num = random.randint(1, 100)
                self.play()

            elif optn == 'n':
                print("Thank you for playing!")
                with open(self.__path, 'r') as f:
                    hs = json.load(f)

                if hs.get('high-score') < self.__score:
                    hs['high-score'] = self.__score

                with open(self.__path, 'w') as f:
                    json.dump(hs, f, indent = 4)

                exit()

            else:
                print("Wrong Choive! Enter again!")


if __name__ == "__main__":
    game = NumberGuessing()
    game.play()
