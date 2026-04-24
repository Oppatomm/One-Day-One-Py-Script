import random

class NumberGuessingGame :
    def __init__(self):
        pass
    def start_game(self) :
        num = random.randint(1,100)

        while True :
            try :
                choice = int(input("Enter the numbers : "))

                if choice == num :
                    print("You guessed the number correctly.")
                    break
                elif choice < num :
                    print(f"{choice} Your guess is too low")
                elif choice > num :
                    print(f"{choice} Your guess is too high")
            except ValueError :
                print("Please enter the numbers.")

app = NumberGuessingGame()
app.start_game()