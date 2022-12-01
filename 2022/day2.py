with open("_input/day1.txt", encoding='utf8') as f:
    lines = f.read().splitlines() 

acc = 0
nums = []
for num in lines:
    if (num == ''):
        nums.append(acc)
        acc = 0
        continue
    acc += int(num)
if (acc > 0):
    nums.append(acc)
    
print(f'part 1: {max(nums)}')
print(f'part 2: {sum(sorted(nums)[-3:])}')