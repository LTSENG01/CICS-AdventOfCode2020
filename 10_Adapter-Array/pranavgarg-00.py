f = open('day10.txt')
s = f.read()
nums = list(s.split())
for i in range(len(nums)):
    nums[i] = int(nums[i])
nums.sort()
diffs = []
for i in range(len(nums) - 1):
    diffs.append(nums[i+1] - nums[i])
diffs.insert(0, 1)
print(diffs)


combs = []
temp = 0
for x in diffs:
    if x == 3:
        if not temp == 0: 
            combs.append(temp)
            temp = 0
    elif x == 1:
        temp+=1
if not temp == 0:
    combs.append(temp)
print(combs)
finalans = 1
for i in combs:
    if i == 2:
        finalans *= 2
    if i == 3:
        finalans *= 4
    if i == 4: 
        finalans *= 7
print(finalans)
