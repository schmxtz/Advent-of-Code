import time

if '__main__' == __name__:
    with open('./data/day11.txt') as file:
        stones = file.read().split(' ')

    start = time.perf_counter()
    for i in range(25):
        j = 0
        k = len(stones)
        while j < k:
            if '0' == stones[j]:  # 1st rule: replace 0 with
                stones[j] = '1'
            elif len(stones[j]) % 2 == 0:  # 2nd rule: split into two stones if even #digits -> 99 => 9 9
                old_stone = stones[j]
                stones[j] = old_stone[:len(old_stone)//2]
                stones.insert(j+1, str(int(old_stone[len(old_stone)//2:])))
                j += 1
            else:
                stones[j] = str(int(stones[j])*2024)
            j += 1
            k = len(stones)
    end = time.perf_counter()

    duration_ns = (end-start)
    print(f"It took {duration_ns}s to calculate {len(stones)}")
