# Day 9 - Simple countdown timer

> **One Day One Py Script** · Phase 1 : Python Foundations

## Code

```python
import time

class SimpleCountdownTimer() :
    def __init__(self):
        pass

    def countdown(self,minute,second) :
        while True :
            print(f"{minute:2d} minute {second:2d} second")

            if minute == 0 and second == 0 :
                break
        
            time.sleep(1)

            if second == 0 :
                minute -= 1
                second += 59
            else :
                second -= 1

    def run(self) :
        print("== Simple Countdown Time ==")
        try :
            minute = int(input("Enter minutes : "))
            second = int(input("Enter seconds : "))
            
            self.countdown(minute,second)

        except ValueError :
            print("Please enter the number")


if __name__ == "__main__" :
    app = SimpleCountdownTimer()
    app.run()
```

## Output

```
== Simple Countdown Time ==
Enter minute : 1
Enter second : 25
 1 minute 25 second
 1 minute 24 second
 1 minute 23 second
 1 minute 22 second
 1 minute 21 second
 1 minute 20 second
 1 minute 19 second
 1 minute 18 second
 1 minute 17 second
 1 minute 16 second
 1 minute 15 second
 1 minute 14 second
 1 minute 13 second
 1 minute 12 second
 1 minute 11 second
 1 minute 10 second
 1 minute  9 second
 1 minute  8 second
 1 minute  7 second
 1 minute  6 second
 1 minute  5 second
 1 minute  4 second
 1 minute  3 second
 1 minute  2 second
 1 minute  1 second
 1 minute  0 second
 0 minute 59 second
 0 minute 58 second
 0 minute 57 second
 0 minute 56 second
 0 minute 55 second
 0 minute 54 second
 0 minute 53 second
 0 minute 52 second
 0 minute 51 second
 0 minute 50 second
 0 minute 49 second
 0 minute 48 second
 0 minute 47 second
 0 minute 46 second
 0 minute 45 second
 0 minute 44 second
 0 minute 43 second
 0 minute 42 second
 0 minute 41 second
 0 minute 40 second
 0 minute 39 second
 0 minute 38 second
 0 minute 37 second
 0 minute 36 second
 0 minute 35 second
 0 minute 34 second
 0 minute 33 second
 0 minute 32 second
 0 minute 31 second
 0 minute 30 second
 0 minute 29 second
 0 minute 28 second
 0 minute 27 second
 0 minute 26 second
 0 minute 25 second
 0 minute 24 second
 0 minute 23 second
 0 minute 22 second
 0 minute 21 second
 0 minute 20 second
 0 minute 19 second
 0 minute 18 second
 0 minute 17 second
 0 minute 16 second
 0 minute 15 second
 0 minute 14 second
 0 minute 13 second
 0 minute 12 second
 0 minute 11 second
 0 minute 10 second
 0 minute  9 second
 0 minute  8 second
 0 minute  7 second
 0 minute  6 second
 0 minute  5 second
 0 minute  4 second
 0 minute  3 second
 0 minute  2 second
 0 minute  1 second
 0 minute  0 second
```

## Concept

| Concept | อธิบาย |
| --- | --- |
| `loop` | ผมใช้ while-loop ในการบังคับให้ทุกๆเคส เข้าไปยังลูป เพื่อแสดงเวลา และคำนวณเวลา  |
| `time` | ผมนำ time library มาใช้ใน code นี้  เพื่อให้เห็นจังหวะที่เวลาหยุดลงทุกๆ 1 วินาที หลังแสดงผลลัพธ์เวลาออกมา โดยใช้ `time.sleep(1)` 1 ในวงเล็บคือการบอกให้เวลาหยุดลง 1 วินาที  |

## สิ่งที่ค้นพบ 

- `time` time เป็น library ในภาษา python โดยที่ได้นำมาใช้ใน code นี้คือ time.sleep(seconds) เพื่อให้โปรแกรมหยุดการทำงาน

## วันพรุ่งนี้

Day 10 -> Rock paper scissors