# Day 6 - Number guessing game

> **One Day One Py Script** · Phase 1 : Python Foundations

## Code

```python
import random

class NumberGuessingGame :
    def __init__(self):
        pass
    def start_game(self) :
        num = random.randint(1,100)

        print("== Number guessing game ==")
        while True :
            try :
                choice = int(input("Enter the numbers : "))

                if choice == num :
                    print("You guessed the number correctly.")
                    break
                elif choice < num :
                    print(f"{choice} Your guess is too low")
                elif choice > num :
                    print(f"{choice} Your guess is too high")
            except ValueError :
                print("Please enter the numbers.")

app = NumberGuessingGame()
app.start_game()
```

## Output

```
== Number guessing game ==
Enter the numbers : 43
43 Your guess is too low
Enter the numbers : 50
50 Your guess is too low
Enter the numbers : 60
60 Your guess is too high
Enter the numbers : 55
55 Your guess is too low
Enter the numbers : 58
58 Your guess is too low
Enter the numbers : 59
You guessed the number correctly.
```

## Concept

| Concept | อธิบาย |
| --- | --- |
| `random` | สร้างตัวเลขแบบสุ่ม  |
| `loop` | while-loop มีหน้าที่ในการบังคับให้ทุกๆinput ที่ผู้ใช้ป้อนเข้ามา เข้าที่ while-loop ทั้งหมด เพราะเรากำหนด True จึงทำให้ทุกๆinput ที่รับเข้ามา เข้า while-loop อย่างแน่นอน  |

## วันพรุ่งนี้

Day 7 -> Multiplication table