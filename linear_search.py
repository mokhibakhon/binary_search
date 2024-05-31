import random
import time
from datetime import datetime

data = []
for i in range(20):
    data.append(random.randint(1, 50))
print(data)
target = int(input("target = "))
count = 0
print(datetime.now())
for j in data:
    time.sleep(1)
    count += 1
    if j == target:
        print(target)
        break
print(count)
print(datetime.now())