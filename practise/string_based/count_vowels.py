#count the number of vowels in a user input(input x='python')

string = 'python'

count = 0
for char in string:
    if char in "aeiou":
        count += 1
print(count)

