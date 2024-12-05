from collections import deque
rules = {}
updates = []
parse_updates = False
with(open('./data/day5.txt') as file):
    while (line:= file.readline()):
        line = line.strip()
        if not line:
            parse_updates = True
            continue
        if not parse_updates:
            rule = list(map(int, line.split("|")))
            if rule[0] not in rules:
                rules[rule[0]] = set([rule[1]])
            else:
                rules[rule[0]].add(rule[1])
        else:
            update =list(map(int, line.split(",")))
            updates.append(update)
rules[13] = set()
middle_sum = 0
seen_numbers = set()
incorrect_updates = []
for update in updates:
    seen_numbers = set()
    is_correct = True
    for number in update:
        if len(rules[number] & seen_numbers) != 0:
            is_correct = False
            incorrect_updates.append(update)
            break
        seen_numbers.add(number)
    if is_correct:
        middle_sum += update[len(update)//2]      

print(f"Result: {middle_sum}")

middle_sum = 0
seen_numbers = deque()
analyzed_numbers = set()
for update in incorrect_updates:
    ordered_update = []
    seen_numbers = deque(update)
    while seen_numbers:
        number = seen_numbers.popleft()
        if (number in analyzed_numbers): break
        if (number not in rules):
            analyzed_numbers.add(number)
            seen_numbers.append(number)
            continue
        if len(rules[number] & set(seen_numbers)) != len(seen_numbers):
            seen_numbers.append(number)
        else:
            ordered_update.append(number)
    middle_sum += ordered_update[len(update)//2]   
   
print(f"Result: {middle_sum}")