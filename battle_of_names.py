count = int(input())
odd_set = set()
even_set = set()

counter = 0

for row in range(1, count + 1):

    current_list = [ord(x) for x in input()]
    current_num = int(sum(current_list) / row)

    if current_num % 2 == 0:
        even_set.add(current_num)

    else:
        odd_set.add(current_num)

if sum(odd_set) > sum(even_set):
    different = odd_set - even_set

elif sum(odd_set) < sum(even_set):
    different = odd_set ^ even_set

else:
    different = odd_set | even_set

result = [str(x) for x in different]
print(', '.join(result))

