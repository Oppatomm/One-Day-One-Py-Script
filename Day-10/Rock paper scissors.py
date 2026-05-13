import random

class RockPaperScissors() :
    def __init__ (self) :
        pass
    def run(self) :
        print("== Rock Paper Scissors ==")
        print("1.Rock\n2.Paper\n3.Scissors\nExample Input : rock")
        choice = str(input("enter choice ")).lower().strip()
        print(f"Input : {choice}")

        words = ["rock" , "paper" , "scissors"]

        if choice in words :
            random_word = random.choice(words)
            
            if choice == 'rock' :
                if random_word == 'rock' :
                    print(f"You {choice} , Random {random_word} \nIt's a tie.")
                elif random_word == 'paper' :
                    print(f"You {choice} , Random {random_word} \nYou lost.")
                elif random_word == 'scissors' :
                    print(f"You {choice} , Random {random_word} \nYou win!!")

            elif choice == 'paper' :
                if random_word == 'paper' :
                    print(f"You {choice} , Random {random_word} \nIt's a tie.")
                elif random_word == 'scissors' :
                    print(f"You {choice} , Random {random_word} \nYou lost.")
                elif random_word == 'rock' :
                    print(f"You {choice} , Random {random_word} \nYou win!!")

            elif choice == 'scissors' :
                if random_word == 'scissors' :
                    print(f"You {choice} , Random {random_word} \nIt's a tie.")
                elif random_word == 'rock' :
                    print(f"You {choice} , Random {random_word} \nYou lost.")
                elif random_word == 'paper' :
                    print(f"You {choice} , Random {random_word} \nYou win!!")

        else :
            print("Please type a alphabet. example rock")


if __name__ == "__main__" :
    app = RockPaperScissors()
    app.run()