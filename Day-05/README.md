# Day 5 - BMI calculator

> **One Day One Py Script** · Phase 1 : Python Foundations

## Code

```python
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
```

## Output

```
== BMI calculator ==
Enter a weight : 64
Enter a height : 175
weight = 64.0 kg height = 175.0 cm 
BMI = 20.90
You are... Normal
```

## Concept

| Concept | อธิบาย |
| --- | --- |
| `formula` | สำหรับสูตรการคำนวณ BMI คือ น้ำหนัก/((ส่วนสูง/100)^2)  |
| `input` | input ที่รับ รับข้อมูลประเภท `float` เพราะว่าน้ำหนักอาจจะมีโอกาสที่จะไม่ได้เป็นจำนวนเต็ม ส่วนสูงนั้นก็มีโอกาสเช่นกัน ถ้าใช้เครื่องวัดส่วนสูงแบบดิจิตอล |

## สิ่งที่ค้นพบ 

- `and` ภาษา Python ใช้ and แทน && ต่างกับภาษาอื่นๆ เช่น Java , C ที่ใช้ && ในการแทนว่า `และ` 

## วันพรุ่งนี้

Day 6 -> Number guessing game