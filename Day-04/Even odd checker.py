class EvenOddChecker :
    def __init__(self) :
        pass
    def check_even(self,number) :
        return number % 2 == 0

    def run(self) :
        print("== Even odd checker ==")
        try :
            number = int(input("Enter a number : "))
            if self.check_even(number) :
                print(f"{number} is Even number")
            else :
                print(f"{number} is Odd number")
        except ValueError :
            print("Please enter an integer")

app = EvenOddChecker()
app.run()