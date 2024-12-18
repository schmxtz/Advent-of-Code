import time

# precompute exponents
pre_exp = [10**i for i in range(30)]

def split_middle(x: int) -> tuple[int, int]:
    assert(x >= 0)
    ctr = 0
    y = 0
    while x >= 0:
        y += pre_exp[ctr]*(x % 10)
        x //= 10
        ctr += 1
        if abs(x-y) < pre_exp[ctr]: break
    return (x, y)

def length(x: int) -> int:
    assert(x >= 0)
    if x == 0:
        return 1
    ctr = 0
    while x > 0:
        x //= 10
        ctr += 1
    return ctr

if '__main__' == __name__:
    with open('./data/day11.txt') as file:
        stones = list(map(int, file.read().split(' ')))
    stones = {stone: stones.count(stone) for stone in stones}
    
    start = time.perf_counter()
    for i in range(75):
        changes = {}
        for stone in stones:
            count = stones[stone]
            if count == 0:
                continue
            stones[stone] = 0
            if stone == 0:
                changes[1] = count
            elif length(stone) % 2 == 0:
                x1, x2 = split_middle(stone)
                changes[x1] = changes.get(x1, 0)+count
                changes[x2] = changes.get(x2, 0)+count
            else:
                new_stone = stone*2024
                changes[new_stone] = changes.get(new_stone, 0)+count
        for change in changes:
            stones[change] = changes[change]
    result = sum(stones[s] for s in stones)                
    end = time.perf_counter()
    
    duration_ns = (end-start)
    print(f"It took {duration_ns}s to calculate {result}")
    