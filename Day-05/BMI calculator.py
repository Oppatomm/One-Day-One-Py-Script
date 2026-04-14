class BMICalculator :
    def __init__(self):
        pass
    def calculate(self,weight,height) :
        height_m = height / 100
        r = weight / (height_m ** 2)
        if r >= 30 :
            return f"weight = {weight} kg height = {height} cm \BMI = {r:.2f} \nYou are... Obesity level 2"
        elif r <= 29.99 and r >= 25 :
            return f"weight = {weight} kg height = {height} cm \nBMI = {r:.2f} \nYou are... Obesity level 1"
        elif r <= 24.99 and r > 23 :
            return f"weight = {weight} kg height = {height} cm \nBMI = {r:.2f} \nYou are... Overweight"
        elif r <= 22.99 and r > 18.5 :
            return f"weight = {weight} kg height = {height} cm \nBMI = {r:.2f} \nYou are... Normal"
        elif r < 18.5 :
            return f"weight = {weight} kg height = {height} cm \nBMI = {r:.2f} \nYou are... Underweight or thin"

    def run(self) :
        print("== BMI calculator ==")
        try :
            weight = float(input("Enter a weight : "))
            height = float(input("Enter a height : "))
        except ValueError :
            print("Please enter the numbers")
        
        print(self.calculate(weight,height))

app = BMICalculator()
app.run()