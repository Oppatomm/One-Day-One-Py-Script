# Day 3 - Temperature converter

> **One Day One Py Script** · Phase 1 : Python Foundations

## Code

```python
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
            choice = int(input("convert Celsius to Fahrenhiet. type 1 \n" \
                            "convert Fahrenhiet to Celsius. type 2 \n"
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
```

## Output

```
== Temperature converter ==
convert Celsius to Fahrenheit. type 1
convert Fahrenheit to Celsius. type 2
type a choice : 1
Type a celsius : 0
0.0 ํC = 32.0 ํF
```

## Concept

| Concept | อธิบาย |
| --- | --- |
| `float` | การรับค่าตัวเลขเข้ามา เป็นประเภทตัวเลขแบบมีทศนิยม  |
| `formula` | สำหรับสูตรการแปลง  ํC ->  ํF คือ (celsius * 9/5) + 32
สำหรับสูตรการแปลง  ํF ->  ํC คือ (fahrenheit) |

## สิ่งที่ค้นพบ 

- `try-except` สามารถเช็ค ValueError ได้ โดย ValueError เป็นการเช็คเพิ่ม โดยเราเป็นคนสร้างเอง ตัวอย่างเช่น except ปกติ เช็คการป้อนตัวอักษร แต่ ValueError ที่ได้สร้างขึ้น เช็คการป้อนตัวเลขที่มากกว่า 2 เข้ามา 

## วันพรุ่งนี้

Day 4 -> Even odd checker