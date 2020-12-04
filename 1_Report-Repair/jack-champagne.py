my_file = open('1.txt')

line_list = my_file.read().split('\n')
line_list.remove('')

i_list = [];
for elem in line_list:
  i_list.append(int(elem))

sub_list = []
for elem in i_list:
  sub_list.append(2020 - elem)

ans = []

for elem in sub_list:
  if elem in i_list:
    ans.append(elem)

print(ans[0] * ans[1])


