# Day 13 - Tip calculator

> **One Day One Py Script** · Phase 1 : Python Foundations

## Code

```python
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
```

## Output 

```
== Tip calculator ==
Type the amount : 240
tip percentage (10%, 15%, 18%, 20%).
Example : 10 
Type the tip percentage : 10
Type the person : 2
Total price : 264.00
Price/person : 132.00
Total tip : 24.00
Tip/person : 12.00
```

## Concept

| Concept | อธิบาย |
| --- | --- |
| `function` |  ใน code นี้ มี function 2 ตัวหลักๆที่ทำให้ทำผลลัพธ์ออกมาอย่างถูกต้อง 1. calculateTip ทำหน้าที่คำนวณเงินทิป 2.calculateTotalMoney ทำหน้าที่คำนวณจำนวนเงินและทิปรวมกัน   |
| `float` |  Input ในการรับจำนวนเงิน ใช้ float เป็นชนิดของข้อมูลที่รับเข้ามา เพราะจำนวนเงิน อาจจะมีเศษก็ได้ การใช้ float จึงเหมาะสมที่สุด  |

## สิ่งที่ค้นพบ 

- Python สามารถใช้ `"""..."""` ในวงเล็บของ `print()` แทนการใช้ `\n` เพื่อสั่งให้ขึ้นบรรทัดใหม่

## วันพรุ่งนี้

Day 14 -> Palindrome checker