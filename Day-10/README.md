# Day 10 - Rock paper scissors

> **One Day One Py Script** · Phase 1 : Python Foundations

## Code

```python
import random

class RockPaperScissors() :
    def __init__ (self) :
        pass
    def run(self) :
        print("== Rock Paper Scissors ==")
        print("1.Rock\n2.Paper\n3.Scissors\nExample Input : rock")
        choice = str(input("enter choice ")).lower().strip()
        print(f"Input : {choice}")

        words = ["rock" , "paper" , "scissors"]

        if choice in words :
            random_word = random.choice(words)
            
            if choice == 'rock' :
                if random_word == 'rock' :
                    print(f"You {choice} , Random {random_word} \nIt's a tie.")
                elif random_word == 'paper' :
                    print(f"You {choice} , Random {random_word} \nYou lost.")
                elif random_word == 'scissors' :
                    print(f"You {choice} , Random {random_word} \nYou win!!")

            elif choice == 'paper' :
                if random_word == 'paper' :
                    print(f"You {choice} , Random {random_word} \nIt's a tie.")
                elif random_word == 'scissors' :
                    print(f"You {choice} , Random {random_word} \nYou lost.")
                elif random_word == 'rock' :
                    print(f"You {choice} , Random {random_word} \nYou win!!")

            elif choice == 'scissors' :
                if random_word == 'scissors' :
                    print(f"You {choice} , Random {random_word} \nIt's a tie.")
                elif random_word == 'rock' :
                    print(f"You {choice} , Random {random_word} \nYou lost.")
                elif random_word == 'paper' :
                    print(f"You {choice} , Random {random_word} \nYou win!!")

        else :
            print("Please type a alphabet. example rock")


if __name__ == "__main__" :
    app = RockPaperScissors()
    app.run()
```

## Output 1

```
== Rock Paper Scissors ==
1.Rock
2.Paper
3.Scissors
Example Input : rock
enter choice  RoCk
Input : rock
You rock , Random scissors 
You win!!
```

## Output 2

```
== Rock Paper Scissors ==
1.Rock
2.Paper
3.Scissors
Example Input : rock
enter choice banana
Input : banana
Please type a alphabet. example rock
```

## Concept

| Concept | อธิบาย |
| --- | --- |
| `random` | ผมได้นำ library random เข้ามาเพื่อใช้สุ่ม rock , paper และ scissors  |

## วันพรุ่งนี้

Day 11 -> Mad libs generator