import time

def countdown(seconds):
    if seconds < 0:
        return
    
    print(f"Time left: {seconds} sec")
    time.sleep(1)         
    countdown(seconds - 1) 



n = int(input("Enter seconds: "))
countdown(n)
print("Timer Finished!")
