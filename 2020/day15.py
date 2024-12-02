from collections import defaultdict

iterations = 10

#start = [2,20,0,4,1,17]
#start = [3,1,2]
start = [0, 3, 6]

spoken = defaultdict(int)
for i, x in enumerate(start):
    spoken[x] = i+1

last_spoken = start[-1]

for i in range(len(start), iterations):

    print(i+1, last_spoken)
    
    last_spoken = (i+1) - spoken[last_spoken]
    
    last_spoken = spoken[last_spoken]


print(last_spoken)
