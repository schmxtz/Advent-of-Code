import time

def is_in_order(page_order, rules):
    for i in range(len(page_order)-1):
        if page_order[i] in rules.get(page_order[i+1], set()):
            return False
    return True

# Parse data
file = open('./data/day5.txt')
data = file.read().split('\n\n')
rules = {}
for rule in data[0].split('\n'):
    rule = list(map(int, rule.split('|')))
    rules[rule[0]] = rules.get(rule[0], set()) | set([rule[1]])

page_orders = [list(map(int, order.split(','))) for order in data[1].split('\n')]

start = time.perf_counter()
result = 0
for page_order in page_orders:
    if is_in_order(page_order, rules): result+=page_order[len(page_order)//2]
end = time.perf_counter()

duration_ns = (end-start)
print(f"It took {duration_ns}s to calculate {result}")