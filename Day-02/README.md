# Day 2 - Simple calculator

> **One Day One Py Script** · Phase 1 : Python Foundations

## Code

```python
class Simple_calculator() :
    def __init__(self):
        pass
    def addition(self,a,b) :
        return a + b
    def subtraction(self,a,b) :
        return a - b
    def multiplication(self,a,b) :
        return a * b
    def division(self,a,b) : 
        return a / b

    def run(self) :
        print("== Calculator ==")
        try :
            a = int(input("Enter a first number : "))
            b = int(input("Enter a second number : "))
        except :
            print("Please enter the numbers. ")
            return
        
        try :
            choice = int(input("Enter a choice (+ , - , * , /) \n" \
                                "1 : Addition (+) \n" \
                                "2 : Subtraction (-) \n" \
                                "3 : Multiplication (*) \n" \
                                "4 : Divition (/) \n" \
                                "Example Input : 3 \n" \
                                "Enter your choice option : "))
        except :
            print("Enter only numbers 1-4.")
            return
        
        if choice == 1 :
            r = self.addition(a,b)
            print(f"result {a} + {b} = {r}")
        elif choice == 2 :
            r = self.subtraction(a,b)
            print(f"result {a} - {b} = {r}")
        elif choice == 3 :
            r = self.multiplication(a,b)
            print(f"result {a} * {b} = {r}")
        elif choice == 4 : 
            if b == 0 :
                print("It cannot be divided by 0.")
            else :
                r = self.division(a,b)
                print(f"result {a} / {b} = {r:.2f}")
        else :
            print("Invalid choice. Please select 1, 2, 3, or 4.")

app = Simple_calculator()
app.run()
```

## Output

```
== Calculator ==
Enter a first number : 1
Enter a second number : 2
Enter a choice (+ , - , * , /) :
1 : Addition (+)
2 : Subtraction (-)
3 : Multiplication (*)
4 : Division (/)
Example Input : 3
Enter your choice option : 1
result 1 + 2 = 3
```

## Concept

| Concept | อธิบาย |
| --- | --- |
| `def()` | method ที่ใช้เพื่อเก็บคำสั่งต่างๆที่เฉพาะ และตั้งชื่อให้ตรงกับคำสั่งเพื่อไปใช้งานอย่างถูกต้อง  |
| `class` | เป็นแม่แบบของโปรแกรม โดยมีการเก็บ Attribute และ method ต่างๆของ class นั้นๆเอาไว้ โดยชื่อ class มักเป็นชื่อโปรแกรมหรือชื่อที่แสดงถึงการทำงานของโปรแกรม  |
| `if` | กำหนดเงื่อนไข ถ้า input ตรงตามเงื่อนไขก็เข้าลูปของ if |
| `elif` | ทำเพื่อดักเงื่อนไขที่ 2 กรณีที่โปรแกรมมีหลายเงื่อนไข ถ้าเงื่อนไขที่ 2 ถูกต้องก็จะเข้าลูปนี้ |
| `else` | มีไว้เพื่อดักกรณีที่ไม่เข้าทั้ง if หรือ elif แล้วแจ้ง error ให้ user เข้าใจว่าทำไมโปรแกรม.ให้ผลลัพธ์ผิดพลาด |
| `try-except` | มีไว้เพื่อป้องกันไม่ให้โปรแกรมทำงานผิดพลาด โดยเริ่มจากการทำงานที่ try ก่อน ถ้า user กรอก input ที่ผิดพลาด except จะแจ้งสาเหตุของการ error ของโปรแกรม |
| `f-string` | การจัดการข้อความโดยเริ่มจาก f และมี `"..."` เป็นตัวกำหนดกรอบของ string โดย f-string จะเริ่มทำงานได้ก็ต่อเมื่อด้านในปีกกา มี variable หรือ ตัวเลข รวมถึงสามารถใช้ variable รวมกับ method ก็ได้ Example `name.upper()`    |

## สิ่งที่ค้นพบ 

- Python ไม่ต้องเริ่มเขียน `int, String, float, double, char, boolean` แบบภาษาอื่นๆ เริ่มเขียนชื่อตัวแปรได้เลย
- `:`  บอกว่ากำลังจะเริ่มรูปแบบข้อความ เช่น `{123.456789:.2f}` ผลลัพธ์ก็จะออกมาเป็น 1123.46 เพราะ `.2f` บอกว่าให้แสดงผลลัพธ์ออกเป็นทศนิยม 2 ตำแหน่ง่

## วันพรุ่งนี้

Day 3 -> Temperature converter