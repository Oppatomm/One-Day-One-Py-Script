# Day 12 - Area calculator

> **One Day One Py Script** · Phase 1 : Python Foundations

## Code

```python
import math

class AreaCalculator :
    def __init__(self):
        pass

    def run(self) :
        try :
            print("== Area Calculator ==")
            print("""Type 1 : Calculate the area of a square
Type 2 : Calculate the area of a rectangle
Type 3 : Calculate the area of a triangle
Type 4 : Calculate the area of a trapezoid
Type 5 : Calculate the area of a kite
Type 6 : Calculate the area of a circle
Type 7 : Calculate the area of a ellipse
Type 8 : Calculate the area of a regular hexagon
Example Input : 1""")
            choice = int(input("Type a number : "))

            if choice == 1 :
                side = float(input("Enter side (m) : "))
                print(f"Square = {side*side:.2f} square meters")
            elif choice == 2 :
                width = float(input("Enter width (m) : "))
                length = float(input("Enter length (m) : "))
                print(f"Rectangle = {width*length:.2f} square meters")
            elif choice == 3 :
                sideA = float(input("Please type side 1 length (m) : "))
                sideB = float(input("Please type side 2 length (m) : "))
                sideC = float(input("Please type side 3 length (m) : "))

                if (sideA + sideB > sideC ) and (sideA + sideC > sideB) and (sideB + sideC > sideA)  :

                    side = (sideA + sideB + sideC) / 2
                    
                    area = math.sqrt(side * (side - sideA) * (side - sideB) * (side - sideC))

                    print(f"Common triangle = {area:.2f} square meters")
                else :
                    print("Error: These lengths cannot form a valid triangle!")
                    
            elif choice == 4 :
                parallel_side1 = float(input("Please type length of parallel side 1 (m) : "))
                parallel_side2 = float(input("Please type length of parallel side 2 (m) : "))
                height = float(input("Please type the height (m) : "))

                print(f"Trapezoid = {0.5*(parallel_side1+parallel_side2)*height:.2f} square meters")
            elif choice == 5 :
                diagonal1 = float(input("Please type the first diagonal (m) : "))
                diagonal2 = float(input("Please type the second diagonal (m) : "))
                print(f"Kite-shaped square = {0.5*(diagonal1*diagonal2):.2f} square meters")
            elif choice == 6 :
                radius = float(input("Please type the radius (m) : "))
                print(f"Circle = {math.pi*(radius*radius):.2f} square meters")
            elif choice == 7 :
                longaxis = float(input("Please type the long axis radius (m) : "))
                shortaxis = float(input("Please type the short axis radius (m) : "))
                print(f"Ellipse = {math.pi*(longaxis*shortaxis):.2f} square meters")
            elif choice == 8 :
                side = float(input("Please type the side length (m) : "))
                area = (3 * math.sqrt(3) / 2) * (side**2)
                print(f"Hexagon on the same side = {area:.2f} square meters")
            else :
                print("Please type a number 1 - 8.")
        except ValueError :
            print("Error: Please enter a valid number for dimensions.")


if __name__ == "__main__" :
    app = AreaCalculator()
    app.run()
```

## Output 1

```
== Area Calculator ==
Type 1 : Calculate the area of a square
Type 2 : Calculate the area of a rectangle
Type 3 : Calculate the area of a triangle
Type 4 : Calculate the area of a trapezoid
Type 5 : Calculate the area of a kite
Type 6 : Calculate the area of a circle
Type 7 : Calculate the area of a ellipse
Type 8 : Calculate the area of a regular hexagon
Example Input : 1
Type a number : 1
Enter side (m) : 5
Square = 25.00 square meters
```

## Output 2

```
== Area Calculator ==
Type 1 : Calculate the area of a square
Type 2 : Calculate the area of a rectangle
Type 3 : Calculate the area of a triangle
Type 4 : Calculate the area of a trapezoid
Type 5 : Calculate the area of a kite
Type 6 : Calculate the area of a circle
Type 7 : Calculate the area of a ellipse
Type 8 : Calculate the area of a regular hexagon
Example Input : 1
Type a number : 9
Please type a number 1 - 8.
```

## Output 3

```
== Area Calculator ==
Type 1 : Calculate the area of a square
Type 2 : Calculate the area of a rectangle
Type 3 : Calculate the area of a triangle
Type 4 : Calculate the area of a trapezoid
Type 5 : Calculate the area of a kite
Type 6 : Calculate the area of a circle
Type 7 : Calculate the area of a ellipse
Type 8 : Calculate the area of a regular hexagon
Example Input : 1
Type a number : abc
Error: Please enter a valid number for dimensions.
```

## Concept

| Concept | อธิบาย |
| --- | --- |
| `math` |  ใน code นี้ใช้โมดูล math 2 ตัวคือ `1.math.pi` `2.math.sqrt` `math.pi` คือค่า π (3.141592) นำไปใช้ในการหาพื้นที่วงกลมและการหาพื้นที่วงรี `math.sqrt` คือการหารากที่ 2 ของเลขนั้นๆ โดยใช้เลขที่เหมือนกัน คูณกันให้ได้ เลขนั้นๆที่รับเข้ามา โดยได้นำมาใช้ในการหาพื้นที่สามเหลี่ยมทั่วไปและการหาพื้นที่หกเหลี่ยมด้านเท่า  |

## สิ่งที่ค้นพบ 

- Python สามารถใช้ `"""..."""` ในวงเล็บของ `print()` แทนการใช้ `\n` เพื่อสั่งให้ขึ้นบรรทัดใหม่

## วันพรุ่งนี้

Day 13 -> Tip calculator