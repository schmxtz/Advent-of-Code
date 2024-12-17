import time

data = open('./data/day9.txt').read()
ids = []
for i in range(len(data)):
    if i % 2 == 0:
        for j in range(int(data[i])):
            ids.append(i//2)
    else:
        for j in range(int(data[i])):
            ids.append(-1)

left = 0
right = len(ids)-1
while not all(map(lambda x: x == -1, ids[left:])):
    if right <= left:
        right = len(ids)-1
    if ids[left] != -1:
        left+=1
    else:
        if ids[right] != -1:
            ids[left] = ids[right]
            ids[right] = -1
        right -= 1

i = 0
result = 0
while ids[i] != -1:
    result += i * ids[i]
    i += 1

print(result)



        