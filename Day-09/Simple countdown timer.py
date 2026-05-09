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