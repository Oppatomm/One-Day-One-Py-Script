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