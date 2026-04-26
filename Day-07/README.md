# Day 7 - Multiplication table

> **One Day One Py Script** · Phase 1 : Python Foundations

## Code

```python
class MultiplicationTable() :
    def __init__(self):
        pass
    def run(self) :
        print("== Multiplication table ==")
        while True :
            try :
                number = input("Enter a number (or 'q' to quit) : ")

                if number.lower() == 'q' :
                    break
                else : 
                    number = int(number)
                    for i in range(1, number+1) :
                        print(f"-- multiplication table {i} --")
                        for j in range(1, 13) :
                            print(f"{i} x {j:2d} = {i*j}")

            except ValueError :
                print("Please enter the numbers.")

app = MultiplicationTable()
app.run()
```

## Output

```
== Multiplication table ==
Enter a number (or 'q' to quit) : 4
-- multiplication table 1 --
1 x  1 = 1
1 x  2 = 2
1 x  3 = 3
1 x  4 = 4
1 x  5 = 5
1 x  6 = 6
1 x  7 = 7
1 x  8 = 8
1 x  9 = 9
1 x 10 = 10
1 x 11 = 11
1 x 12 = 12
-- multiplication table 2 --
2 x  1 = 2
2 x  2 = 4
2 x  3 = 6
2 x  4 = 8
2 x  5 = 10
2 x  6 = 12
2 x  7 = 14
2 x  8 = 16
2 x  9 = 18
2 x 10 = 20
2 x 11 = 22
2 x 12 = 24
-- multiplication table 3 --
3 x  1 = 3
3 x  2 = 6
3 x  3 = 9
3 x  4 = 12
3 x  5 = 15
3 x  6 = 18
3 x  7 = 21
3 x  8 = 24
3 x  9 = 27
3 x 10 = 30
3 x 11 = 33
3 x 12 = 36
-- multiplication table 4 --
4 x  1 = 4
4 x  2 = 8
4 x  3 = 12
4 x  4 = 16
4 x  5 = 20
4 x  6 = 24
4 x  7 = 28
4 x  8 = 32
4 x  9 = 36
4 x 10 = 40
4 x 11 = 44
4 x 12 = 48
Enter a number (or 'q' to quit) : q
```

## Concept

| Concept | อธิบาย |
| --- | --- |
| `nested-lopp` | ลูป 2 ชั้น โดยลูปชั้นที่ 1 มีหน้าที่ในการบอกว่า นี่คือสูตรคูณแม่อะไร ส่วนลูปชั้นที่ 2 มีหน้าที่ในการแสดงผลการคูณ  |

## วันพรุ่งนี้

Day 8 -> FizzBuzz