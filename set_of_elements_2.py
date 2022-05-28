n, m = [int(x) for x in input().split()]

first_set = set(input() for _ in range(n))
second_set = set(input() for _ in range(m))

result = first_set & second_set

[print(x) for x in result]




