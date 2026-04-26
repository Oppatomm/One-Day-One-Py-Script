class MultiplicationTable() :
    def __init__(self):
        pass
    def run(self) :
        print("== Multiplication table ==")
        while True :
            try :
                number = input("Enter a number (or 'q' to quit) : ")

                if number.lower() == 'q' :
                    break
                else : 
                    number = int(number)
                    for i in range(1, number+1) :
                        print(f"-- multiplication table {i} --")
                        for j in range(1, 13) :
                            print(f"{i} x {j:2d} = {i*j}")

            except ValueError :
                print("Please enter the numbers.")

app = MultiplicationTable()
app.run()