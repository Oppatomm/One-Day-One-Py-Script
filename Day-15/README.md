# Day 15 - Factorial finder

> **One Day One Py Script** · Phase 1 : Python Foundations

## Code

```python
class FactorialFinder :
    def __init__(self) :
        pass

    def findFactorial(self, n) :
        if n <= 1 :
            return 1
        else :
            return n * self.findFactorial(n-1)
    
    def run(self) :
        try :
            print("== Factorial finder ==")
            n = int(input("Type the number : "))

            result = self.findFactorial(n)

            print(f"{n}! = {result}")
        except ValueError :
            print("Please type the number.")


if __name__ == "__main__" :
    app = FactorialFinder()
    app.run()
```

## Output 1

```
== Factorial finder ==
Type the number : 5
5! = 120
```

## Output 2

```
== Factorial finder ==
Type the number : a
Please type the number.
```

## Concept

| Concept | อธิบาย |
| --- | --- |
| `recursion` |  recursion ใน code นี้ มีหลักการง่ายๆคือ ตรง if ที่เป็น base-case เขียนเงื่อนไขไว้ว่า เมื่อใดที่ n น้อยกว่าหรือเท่ากับ 1 ให้ส่งค่า 1 ออกมาเลย และตรง else มี logic ว่า ให้ส่งค่า n * findFactorial(n-1)  |

## วันพรุ่งนี้

Day 16 -> Shopping cart