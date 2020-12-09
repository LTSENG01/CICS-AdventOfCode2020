with open('5.txt', 'r') as fin:
    data = [row[:-1] for row in fin]


def lower_half(collection):
    return collection[:int(len(collection)/2)]


def upper_half(collection):
    return collection[int(len(collection)/2):]


def seat_id(row, column):
    return row * 8 + column


seat_ids = []

for line in data:
    possible_rows = [row for row in range(0, 128)]
    possible_cols = [col for col in range(0, 8)]

    for row_char in line[:7]:
        if row_char == 'F':
            possible_rows = lower_half(possible_rows)
        else:
            # 'B'
            possible_rows = upper_half(possible_rows)

    row_id = possible_rows[0]

    for col_char in line[7:]:
        if col_char == 'L':
            possible_cols = lower_half(possible_cols)
        else:
            # 'R'
            possible_cols = upper_half(possible_cols)

    col_id = possible_cols[0]
    seat_ids.append(seat_id(row_id, col_id))

print(max(seat_ids))

seat_ids.sort()
starting_id = seat_ids[0]

for seat in range(0, len(seat_ids)):
    if seat_ids[seat] != seat + starting_id:
        print(seat_ids[seat] - 1)
        break
