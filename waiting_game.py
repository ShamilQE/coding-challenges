import random
import time

print("Waiting game")
print("Your target time is 4 seconds")

print("---Press ENTER to begin---")
input()
waitingTime = random.randint(4,4)
start = time.time()
input("...Press Enter again after 4 seconds...")
end = time.time()
elapsed = round(end - start,3)
difference = round(waitingTime - elapsed,3)
print("\n" "Elapsed time: " + str(elapsed) + " seconds")

if difference < 0.1:
    print(str(difference) + " seconds too slow")
elif difference > 0.1:
    print(str(difference) + " seconds too fast")
else:
    print("You did it")




