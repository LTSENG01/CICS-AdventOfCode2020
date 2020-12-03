# Author: Walker Sorensen
# python3.8

with open('day1data.txt', 'r') as f:
	nums = [int(line.split('\n')[0]) for line in f.readlines()]

print(nums)

for num_1 in nums:
	for num_2 in nums:
		if num_1 + num_2 == 2020:
			print(num_1 * num_2)

		for num_3 in nums:
			if num_1 + num_2 + num_3 == 2020:
				print(num_1 * num_2 * num_3)