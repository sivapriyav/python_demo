
lis = [5, 10, 5, 10, 5, 3, 2]

most_repeated = lis[0]
max_count = 0

for num in lis:
    count = lis.count(num)

    if count > max_count:
        max_count = count
        most_repeated = num

print(most_repeated)

