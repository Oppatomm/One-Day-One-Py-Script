class FizzBuzz() : 
    def __init__(self):
        pass
    def fizzbuzz(self,i) :
        if i % 3 == 0 and i % 5 == 0 :
            return f"{i:3d} = FizzBuzz"
        elif i % 3 == 0 :
            return f"{i:3d} = Fizz"
        elif i % 5 == 0 :
            return f"{i:3d} = Buzz"
        else :
            return f"{i:3d}"

    def run(self) :
        print("== FizzBuzz ==")
        for i in range(1, 101) :
            print(self.fizzbuzz(i))

if __name__ == "__main__" :
    app = FizzBuzz()
    app.run()