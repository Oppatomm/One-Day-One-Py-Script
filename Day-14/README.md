# Day 14 - Palindrome checker

> **One Day One Py Script** · Phase 1 : Python Foundations

## Code

```python
class PalindromeChecker :
    def __init__(self) :
        pass
    
    def checkPalindrome(self, word) :
        n = len(word) // 2
        count1 = []
        count2 = []
        
        if len(word) %2 == 0 :
            for char in word[:n] :
                count1 += char
            if len(count1) == n :
                for char in word[n:] :
                    count2 += char
        elif len(word) %2 != 0 :
            for char in word[:n] :
                count1 += char
            if len(count1) == n :
                for char in word[n+1:] :
                    count2 += char
        
        count2.reverse()

        if count1 == count2 :
            return f"{word} is a palindrome."
        elif count1 != count2 :
            return f"{word} is not a palindrome."

    def run(self) :
        print("== Palindrome checker ==")
        word = input("Enter the string : ").lower().strip()

        result = self.checkPalindrome(word)

        print(result)


if __name__ == "__main__" :
    app = PalindromeChecker()
    app.run()
```

## Output 1

```
== Palindrome checker ==
Enter the string : abba
abba is a palindrome.
```

## Output 2

```
== Palindrome checker ==
Enter the string : abcba
abcba is a palindrome.
```

## Output 3

```
== Palindrome checker ==
Enter the string : abcd
abcd is not a palindrome.
```

## Concept

| Concept | อธิบาย |
| --- | --- |
| `string` |  input รับค่า string โดยใช้ `input()` ซึ่งใน python `input()` รับค่าเป็น string อยู่แล้ว   |
| `function` |  มีฟังก์ชัน checkPalindrome ใช้ในการคำนวณว่า ข้อความนั้นๆเป็น Palindrome หรือไม่   |

## สิ่งที่ค้นพบ 

- `.lower()` ทำให้ข้อความที่ป้อนเข้ามา เป็นตัวพิมพ์เล็ก
- `.strip()` ลบช่องว่างที่ผู้ใช้ป้อนเข้ามา หรืออาจจะบังเอิญกด spacebar

## วันพรุ่งนี้

Day 15 -> Factorial finder