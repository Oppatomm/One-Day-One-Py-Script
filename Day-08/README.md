# Day 8 - FizzBuzz

> **One Day One Py Script** · Phase 1 : Python Foundations

## Code

```python
class FizzBuzz() : 
    def __init__(self):
        pass
    def fizzbuzz(self,i) :
        if i % 3 == 0 and i % 5 == 0 :
            return f"{i:3d} = FizzBuzz"
        elif i % 3 == 0 :
            return f"{i:3d} = Fizz"
        elif i % 5 == 0 :
            return f"{i:3d} = Buzz"
        else :
            return f"{i:3d}"

    def run(self) :
        print("== FizzBuzz ==")
        for i in range(1, 101) :
            print(self.fizzbuzz(i))

if __name__ == "__main__" :
    app = FizzBuzz()
    app.run()
```

## Output

```
== FizzBuzz ==
  1
  2
  3 = Fizz
  4
  5 = Buzz
  6 = Fizz
  7
  8
  9 = Fizz
 10 = Buzz
 11
 12 = Fizz
 13
 14
 15 = FizzBuzz
 16
 17
 18 = Fizz
 19
 20 = Buzz
 21 = Fizz
 22
 23
 24 = Fizz
 25 = Buzz
 26
 27 = Fizz
 28
 29
 30 = FizzBuzz
 31
 32
 33 = Fizz
 34
 35 = Buzz
 36 = Fizz
 37
 38
 39 = Fizz
 40 = Buzz
 41
 42 = Fizz
 43
 44
 45 = FizzBuzz
 46
 47
 48 = Fizz
 49
 50 = Buzz
 51 = Fizz
 52
 53
 54 = Fizz
 55 = Buzz
 56
 57 = Fizz
 58
 59
 60 = FizzBuzz
 61
 62
 63 = Fizz
 64
 65 = Buzz
 66 = Fizz
 67
 68
 69 = Fizz
 70 = Buzz
 71
 72 = Fizz
 73
 74
 75 = FizzBuzz
 76
 77
 78 = Fizz
 79
 80 = Buzz
 81 = Fizz
 82
 83
 84 = Fizz
 85 = Buzz
 86
 87 = Fizz
 88
 89
 90 = FizzBuzz
 91
 92
 93 = Fizz
 94
 95 = Buzz
 96 = Fizz
 97
 98
 99 = Fizz
100 = Buzz
```

## Concept

| Concept | อธิบาย |
| --- | --- |
| `loop` | for-loop ทำหน้าที่ในการวนค่า ตั้งแต่ 1-100  |
| `condition` | เงื่อนไขได้กำหนดออกมาหลักๆทั้งหมด 3 เงื่อนไข 1.i % 3 == 0 and i % 5 == 0 แสดงผลลัพธ์ FizzBuzz 2.i % 3 == 0 แสดงผลลัพธ์ Fizz 3.i % 5 == 0 แสดงผลลัพธ์ Buzz และเงื่อนไขสุดท้าย แสดงผลลัพธ์เลขตัวนั้นๆอย่างเดียว  ทำเพื่อดักตัวเลขที่ไม่เข้าทั้ง 3 เงื่อนไข |

## วันพรุ่งนี้

Day 9 -> Simple countdown timer