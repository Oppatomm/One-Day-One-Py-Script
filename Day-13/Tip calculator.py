class TipCalculator :
    def __init__(self) :
        pass

    def calculateTip(self, money, tip_percen) :
        tip = (money * tip_percen) / 100
        return tip

    def calculateTotalMoney(self, money, tip) :
        total_money = money + tip
        return total_money

    def run(self) :
        print("== Tip calculator ==")
        money = float(input("Type the amount : "))
        tip_percen = int(input("""tip percentage (10%, 15%, 18%, 20%).
Example : 10 
Type the tip percentage : """))
        person = int(input("Type the person : "))

        total_price = self.calculateTotalMoney(money ,self.calculateTip(money, tip_percen))
        total_tip = self.calculateTip(money, tip_percen)

        price_person = self.calculateTotalMoney(money, self.calculateTip(money, tip_percen))/person
        tip_person = self.calculateTip(money, tip_percen)/person

        print(f"Total price : {total_price:.2f}")
        print(f"Price/person : {price_person:.2f}")
        print(f"Total tip : {total_tip:.2f}")
        print(f"Tip/person : {tip_person:.2f}")

if __name__ == "__main__" :
    app = TipCalculator()
    app.run()