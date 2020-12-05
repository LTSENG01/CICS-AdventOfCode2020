with open('day5data.txt', 'r') as f:
	data = [line.split('\n')[0] for line in f.readlines()]

seat_ids = []
for seat in data:
	remaining_rows = range(128)
	remaining_columns = range(8)
	for char in seat:
		if char == 'B':
			remaining_rows = remaining_rows[int(len(remaining_rows)/2):]
		if char == 'F':
			remaining_rows = remaining_rows[:int(len(remaining_rows)/2)]
		if char == 'R':
			remaining_columns = remaining_columns[int(len(remaining_columns)/2):]
		if char == 'L':
			remaining_columns = remaining_columns[:int(len(remaining_columns)/2)]

	seat_ids += [(remaining_rows[0] * 8) + remaining_columns[0]]

seat_ids.sort()

for id_num in range(len(seat_ids)):
	if seat_ids[id_num + 1] != seat_ids[id_num] + 1:
		print(seat_ids[id_num] + 1)
		exit()
