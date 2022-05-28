count = int(input())
first_set = set()
second_set = set()
super_intersection = set()

for _ in range(count):
    first, second = input().split('-')
    range_1 = [int(x) for x in first.split(',')]
    range_2 = [int(x) for x in second.split(',')]

    for x in range(range_1[0], range_1[1] + 1):
        first_set.add(x)

    for x in range(range_2[0], range_2[1] + 1):
        second_set.add(x)

    intersection = first_set & second_set

    if len(intersection) > len(super_intersection):
        super_intersection = intersection

    first_set = set()
    second_set = set()

print(f"Longest intersection is {list(super_intersection)} with length {len(super_intersection)}")
