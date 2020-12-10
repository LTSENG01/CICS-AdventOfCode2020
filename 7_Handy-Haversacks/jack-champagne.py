import re

file = open('7.txt')
fchars = file.read()

rules = []
for elem in fchars.split('\n'):
    rules.append(elem)

rules.remove('')

rule_match = re.compile(r'(.+ )(?:bag(?:s)?) (?:contain) (?:(.+)|no other bags)\.')
bag_match = re.compile(r'([1-5])?((?:[^\d,])+) (?:bag(?:s)?)')

bag_dict = {}
for rule in rules:
    match = rule_match.match(rule)
    try:
        if match[2] is None:
            raise IndexError
        sub_bags = bag_match.findall(match[2])
        bag_key = match[1].strip()

        for i in range(0, len(sub_bags)):
            if sub_bags[i] == ('', 'no other'):
                sub_bags[i] = ('', 0)
                continue
            sub_bags[i] = (str(sub_bags[i][1]).strip(), int(sub_bags[i][0]))


        bag_dict.setdefault(bag_key, sub_bags)
    except TypeError as e:
        bag_dict.setdefault(match[1].strip(), [])
    except IndexError as ie:
        bag_dict.setdefault(match[1].strip(), [])
    

def get_bags_from_tuples(tuple_list):
    bags = []
    for i in range(0, len(tuple_list)):
        bags.append(tuple_list[i][0])
    return bags

def bfs(graph, initial):
    visited = []
    
    queue = [initial]
 
    while queue:
        node = queue.pop(0)
        if node == '':
            continue
        if node not in visited:
            
            visited.append(node)
            neighbours = get_bags_from_tuples(graph[node])

            if 'shiny gold' in neighbours:
                return True
            
            for neighbour in neighbours:
                queue.append(neighbour)
    return False

def get_bags(list_of_tuples):
    ret_dict = {}
    for i in range(0, len(list_of_tuples)):
        ret_dict.setdefault(list_of_tuples[i][0], list_of_tuples[i][1])
    return ret_dict

counter = 0
for bag in bag_dict.keys(): 
    if bfs(bag_dict, bag):
        counter += 1

print(counter)

def dfs(graph, source,path = []):
    bags_on_level = 0
    bags_in_bag = 0
    if source == '':
        return (path, 1)

    if source not in path:
        path.append(source)
        if source not in graph:
           return (path, 1)
        for (neighbour, num) in graph[source]:
            (path, bags_in_bag) = dfs(graph, neighbour, path)
            if bags_in_bag == 0:
                bags_on_level += num
            else:
                bags_on_level += num*bags_in_bag

    return (path, bags_on_level)


def size(bag_dict, bag):
    ans = 1
    for (bag, n) in bag_dict[bag]:
        if bag == '':
            continue
        ans += n*size(bag_dict, bag)
    return ans


print(size(bag_dict, 'shiny gold')-1)

