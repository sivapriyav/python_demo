#write a python program to check whether a number is prime or not.prime
# numbers-2,3,5,7,11,13,17...(those numbers which are divisible by 1 and
# same number only)
#consider 7(find the remainder using 2,3,4,5,6 if remainder is 0 in any
# case the number is not prime)
#consider 9(2 to 8)

n = int(input('enter a number'))

if n<2:
    print('Not prime')
else:
    for i in range(2,n):
        if n % i == 0:
            print(f"{n} is Not prime")
            break
    else:
        print(f"{n} is Prime")

#find the prime numbers in a given range 10 to 30

prime=[]
for num in range(10,31):
    if num<2:
        print("not in prime range")
    else:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            prime.append(num)
print(prime)
#count of primes
print(len(prime))

#input a number from user and reverse it(input-541,output-145)

num = 541
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print(rev)
#in 1st iteration n=541,dig=1,rev=0*10+1=1,num=54
#in 2nd iteration n=54,dig=4,rev=1*10+4=14,num=5
#in 3rd iteration n=5,digit = 5 ,rev=14*10+5=145,num=0
#IN 4th iteration --condition False loop breaks


#input a number from user and find sum of digits of the number
#input=541 output=5+4+1

num = 541
sum = 0
n=num

while num > 0:
    digit = num % 10
    sum = sum+ digit
    num = num // 10
print(f"sum of digits of {n} is {sum}")

#input a string from user and remove all duplicate characters
#input='programming' output='progamin'

inp = 'programming'
res = ''

for i in inp:
    if i not in res:
        res += i
print(res)

#input 2 numbers from user and swap it
#a,b = 10,20
#output-a,b = 20,10
a,b = 10,20
print(f"a:{a}, b:{b}")

b,a = 10,20
print(f"a:{a}, b:{b}")
#with temp variable
c= 0
c=a
a=b
b=c
print(f"a:{a}, b:{b}")

#find the largest number in a list without using index position(withou sort)
#input - x=[100,10,-1,1200,11,3]
#output- 1200


x = [100, 10, -1, 1200, 11, 3]

largest = x[0]

for num in x:
    if num > largest:
        largest = num

print("Largest number:",largest)













