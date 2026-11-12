'''
Mutable datatypes
    List,set,dictionary

Immutable datatypes
    Integer,float,string,boolean,tuple

keywords
    Reserved meaningful words in python.Cannot be provided as a variable name

import keyword
print(keyword.kwlist)

output

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

Difference between keyword,identifier and variable?

1.variable declaration can be performed to store or assign values
2.var declaration eg: x=10,abcAB=30,_abc = 10,abc_bh =10,_=50,abc123 = 20,aa12_c=20
3.cannot start with digit
4.spaces are not allowed
5.must start with a letter or _,special characters are not allowed

Identifiers are variables which are meaningful in nature

name = 'siva'
age = 20
price = 2.6

case sensitivity in python

unicode represents a characters individual code of representation in normal english

'''


x=10
X=20
print(X)

a = 'PYTHON'
b = 'python'

print(a==b)#check both case and value and return a boolean response'''


#String methods

# str1 = 'pythonABC is a language'

# print(str1.upper())

# x=str1.lower()

# print(str1.capitalize())#first letter of first word got upper keys

# print(str1.title()) #first letter of all words get uppercase

# print(str1.swapcase())#swap the cases

# print(str1.find("is")) #returns first position of substring

# print(str1.index("is")) #returns first position of substring

# print(str1.count('a'))

# print(str1.isupper())

# print(str1.isdigit())

# print(x)

# print(f"The original string is: {str1}")

#List Methods

list1 = [2,5,'python']

list1.append('hai')
print(list1)

list1.pop()
print(list1)

list2 = [5,2.5,'siva','python']

list1.extend(list2)#To add element elements from one to another list list2 is added to list1
print(list1)

list1.insert(1,'alpy')
print(list1)

# list1.remove('python')#Removes only the first occurence of element
# print(list1)

print(list1.count('python'))

# list1.clear()
# print(list1)

list1.reverse()
print(list1)

list3 = list1.copy()
print(list3)

list4 = [19,10,2.5,0,-10,100,0.5]
list4.sort() #To convert in ascending order
print(list4)
list4.sort(reverse=True)#descending order
print(list4)

list5 = ['book','pen','Z','K','d','BOOK','PEN','Apple','aPPLE']
list5.sort()#convert to alphabetical order first prefernce for uppercase
print(list5)

#Methods-append,pop,insert,extend,clear,copy,sort,sort(reverse=True),remove

#Builtin methods in python list

num = [20,10,19,2,78]
print(len(num))
print(max(num))
print(min(num))
print(sum(num))

#Interview questions

list6 = [10,20,30,40]
name = 'siva'
#Expected output [10,20,'siva',30,40]

list6.insert(2,name)
print(list6)
#------------------------------------------------------------

#tuple methods

num_tup = (2,3,4,5,2,10)

print(num_tup.count(2))
print(num_tup.index(5))

#Create a tuple and add a new element in its 2nd last index psoition








