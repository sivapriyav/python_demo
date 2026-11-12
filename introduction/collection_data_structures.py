#Collection data types/Data structures-Can store multiple values in a single variable
#List,Tuple,Set,Dictionary

#List

x=list()
print(x)

x = [10,10.5,True,'python',10]
print(x)

#List features-ordered,duplication allowed,mutable,indexing,slicing,can have collection data types

print(x[0])
print(x[2])
print(x[0:3]) #collect the element indexes 0,1,2
y=x[2:6]
print(y)
print(len(x))
print(x[0:])
print(x[:6])
print(x[:])
print(x[0:6:2]) #step
#slicing syntax:[starting index:ending index:step]

x = [10,10.5,True,'python',10]
#Negative indexing
print(x[-2])
print(x[-5:-2]) #collect the elements in indexes -5,-4,-3

#Tuples

#immutable collection data structure

x=tuple()
print(x)
print(type(x))

x=(10,10.5,True,'python',10,[2,4,6],(100,200))
print(x)

#tuple features-ordered,duplications allowed,indexing,slicing,multidata storage
#difference from list is tuple is immutable
#tuple is faster than list in case of large number of data as it is immutable

#Set

x= set()
print(x)
print(type(x))

x={10,10.5,True,'python',10} #empty curly brace denote dictionary atleast one value required to make it a set
print(x)
#set features-unordered,no duplication,no indexing,no slicing,mutable,cannot add list or tuples


#Dictionary

#The only named index data structure in python

x = dict()
x = {'name':'siva','age':30,'gender':'male','name':'sachin',"contact":[123,456,789] }
print(x)
print(x['age'])
print(x['contact'])
print(x['contact'][1])#accessing element in list inside dict














