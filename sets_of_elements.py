len_first, len_second = input().split()
len_first, len_second = int(len_first), int(len_second)
count = len_first + len_second

first_set = set()
second_set = set()

for x in range(1, count + 1):
    nums = input()
    if x <= len_first:
        first_set.add(nums)
    else:
        second_set.add(nums)

[print(x) for x in first_set & second_set]

