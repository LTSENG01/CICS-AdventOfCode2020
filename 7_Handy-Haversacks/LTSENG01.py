# adjective color bags contain (__ adjective color bag(s),... | no other bags).

with open('7.txt', 'r') as fin:
    data = [line[:-1].split(" contain ") for line in fin]
    tokenized = [[entry[0], entry[1].split(", ")] for entry in data]


def recursive_outer_bag(start_bag):
    for bag in data:
        if bag[1].__contains__(start_bag):
            bag_set.add(bag[0])
            recursive_outer_bag(bag[0][:-4])    # cuts the pluralization of bags


# returns count of inner bags + itself (except for the first bag)
def recursive_inner_bags(start_bag):
    outer_bag = next(bag for bag in tokenized if bag[0].__contains__(start_bag))

    # base case
    if outer_bag[1][0].__contains__("no other"):
        return 0

    count_bags = 0
    for inner_bag in outer_bag[1]:
        count_bags += int(inner_bag[0]) * (recursive_inner_bags(inner_bag[2:-4]) + 1)

    return count_bags


bag_set = set()
recursive_outer_bag("shiny gold")
print(len(bag_set))

print(recursive_inner_bags("shiny gold"))
