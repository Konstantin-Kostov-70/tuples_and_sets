count = int(input())
elements = set()

for _ in range(count):

    current_elements = input().split()
    elements = elements.union(current_elements)

[print(x) for x in elements]
