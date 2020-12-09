import math

with open('day3data.txt', 'r') as f:
	data = [line.split('\n')[0] * (73) for line in f.readlines()] # 73 as my data was 31 chars long, and max right dist was 7, and file size was 323 lines. 323 * 7 = 2261 / 31 = 72.9 

def next_step(right, down, _coords):
	_coords[0] += right
	_coords[1] += down

	hit = data[math.trunc(_coords[1])][math.trunc(_coords[0])] == '#'

	return _coords, hit

file_len = 322

def travel_trajectory(right, down):
	count = 0
	coords = [0, 0]
	for line in range(int(file_len/down)):
		coords, hit = next_step(right, down, coords)
		if hit:
			count += 1
	return count

a = travel_trajectory(1, 1)
b = travel_trajectory(3, 1)
c = travel_trajectory(5, 1)
d = travel_trajectory(7, 1)
e = travel_trajectory(1, 2)
i = 1

[print(f'Path {elem[1]}: {elem[0]} bonks') for elem in [[a, 1], [b, 2], [c, 3], [d, 4], [e, 5]]]
print(a * b * c * d * e)
