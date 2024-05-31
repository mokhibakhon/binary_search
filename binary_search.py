import random
import time
from datetime import datetime

data = []

for i in range(20):
    data.append(random.randint(1, 50))

data.sort()
print("Sorted Data:", data)

target = int(input("Target: "))
low = 0
data_l = len(data) - 1
count = 0
print("Start Time:", datetime.now())

while low <= data_l:
    time.sleep(1)
    count += 1
    middle = (data_l + low) // 2
    if data[middle] < target:
        low = middle + 1
    elif data[middle] == target:
        print("Target Found:", target)
        print("Count:", count)
        break
    else:
        data_l = middle - 1

if low > data_l:
    print("Target not found in the list.")

print("End Time:", datetime.now())
