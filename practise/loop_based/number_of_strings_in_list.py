
lis = [5, 10, 'A', 'python', 'hello', 3.5, False]
count = 0

for item in lis:
    if type(item) == str:
        count += 1

print(count)
