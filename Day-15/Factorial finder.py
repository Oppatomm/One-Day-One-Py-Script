class FactorialFinder :
    def __init__(self) :
        pass

    def findFactorial(self, n) :
        if n <= 1 :
            return 1
        else :
            return n * self.findFactorial(n-1)
    
    def run(self) :
        try :
            print("== Factorial finder ==")
            n = int(input("Type the number : "))

            result = self.findFactorial(n)

            print(f"{n}! = {result}")
        except ValueError :
            print("Please type the number.")


if __name__ == "__main__" :
    app = FactorialFinder()
    app.run()