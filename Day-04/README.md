# Day 4 - Even odd checker

> **One Day One Py Script** · Phase 1 : Python Foundations

## Code

```python
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
```

## Output 1 

```
== Even odd checker ==
Enter a number : 0
0 is Even number
```

## Output 2

```
== Even odd checker ==
Enter a number : 1
1 is Odd number
```

## Output 3

```
== Even odd checker ==
Enter a number : a
Please enter an integer
```

## Concept

| Concept | อธิบาย |
| --- | --- |
| `modulo(mod)` | modulo คือการหารเพื่อเอาเศษ นิยมใช้เมื่อต้องการตรวจสอบตัวเลขคู่หรือเลขคี่ |
| `condition` | การตั้งเงื่อนไข เพื่อคัดกรองผลลัพธ์ของการ mod ถ้าผลลัพธ์เป็น True ให้แสดงข้อความ is Even number แต่ถ้าผลลัพธ์เป็น False ให้แสดงข้อความ is Odd number |

## วันพรุ่งนี้

Day 5 -> BMI calculator