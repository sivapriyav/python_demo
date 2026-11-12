'''
In file handling for testing purpose the most commonly used files are
txt,json,excel
'''

#using builtin open() function
#opening file in read mode

file = open("data.txt","r")
content = file.read()

print(content)

file1 = open("data.txt","r")
content = file1.readlines()

print(content)

file1 = open("data.txt","r")
content = file1.readline() #to retrieve single line
print(content)

#opening file in write mode

new_file = open("data.txt","w")
new_file.write('hello')

new_file = open("data1.txt","w")
new_file.write('name:siva')

#opening files in append mode

new_file  = open('data.txt','a')
new_file.write('contact:1234\n')
new_file.close()
print(new_file.closed)

#Methods applicable in existing file-read('r'),write('w'),append('a'),create('x')
#Methods applicable in non-existing file - write('w'),append('a'),create('x')

#File handling using with statement
#with statement automatically closes the file when the block finishes even if an exception occurs

with open('data.txt','r') as file1:
    content = file1.read()
    print(content)
    print(file1.closed)

print(file1.closed)




