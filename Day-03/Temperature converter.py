class Temperature_converter() :
    def __init__(self):
        pass
    def celsiusTofahrenheit(self,celsius) :
        return (celsius * 9/5) + 32
    def fahrenheitTocelsius(self,fahrenheit) :
        return (fahrenheit - 32) * 5/9
    
    def run(self) :
        print("== Temperature converter ==")
        try : 
            choice = int(input("convert Celsius to Fahrenheit. type 1 \n" \
                            "convert Fahrenheit to Celsius. type 2 \n"
                            "type a choice : "))
            if choice > 2 :
                raise ValueError()
        except ValueError :
            print("Please enter only 1 or 2.")
            return
        
        if choice == 1 : 
            try :
                celsius = float(input("Type a celsius : "))
            except :
                print("Please type a number.")
                return
            r = self.celsiusTofahrenheit(celsius)
            print(f"{celsius} ํC = {r} ํF ")
        elif choice == 2 :
            try :
                fahrenheit = float(input("Type a fahrenheit : "))
            except :
                print("Please type a number.")
                return
            r = self.fahrenheitTocelsius(fahrenheit)
            print(f"{fahrenheit} ํF = {r} ํC ")

app = Temperature_converter()
app.run()