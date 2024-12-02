with open('2020\day1.txt', 'r') as fd:
    nums = list(map(lambda x: int(x), fd.readlines()))

def part1(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == 2020:
                return nums[i] * nums[j]
            
def part2(nums):
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 2020:
                    return nums[i] * nums[j] * nums[k]
                
print(part1(nums), part2(nums))