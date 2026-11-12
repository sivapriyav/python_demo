#count the number of vowels in a user input(input x='python is easy to learn')

string = 'python is easy to learn '

count = 0
for char in string:
    if char in "aeiou":
        count += 1
print(count)

