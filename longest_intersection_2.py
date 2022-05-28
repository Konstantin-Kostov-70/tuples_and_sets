def set_generator(range_info):
    start, end = [x for x in range_info.split(',')]
    current_set = set(range(int(start), int(end) + 1))
    return current_set


count = int(input())
longest_intersection = set()

for _ in range(count):
    info = input().split('-')

    first_set = set_generator(info[0])
    second_set = set_generator(info[1])

    intersection = first_set & second_set

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
