'''Error

A problem in a program that prevents it from working as intended

Reasons

1.Incorrect syntax
2.Incorrect program logic
3.Invalid operations'''

# if 10>5
#    print("Hello")

'''Example for SyntaxError

# print(name)     - NameError

# list1 = [10,20,30]
# print(list1[5])    - IndexError

# number  = int("Hello")   - ValueError

# print(10/0)        - ZeroDivisionError

# dict1 = {"name":"siva","age":28}      - KeyError
# print(dict1["location"])'''


'''Exception

Its an error that occurs during program execution and interrupts the normal flow of a program

        #try:
        #   #code that may cause an exception
        #except:
        #   #code to handle exception
        #else:
            #executes when no exception occurs
        #finally:
            #execute irrespective of exception'''


try:
    n = int(input("Enter a number: "))
    result = 100/n
    print(result)

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Please enter a non zero number")

print("Hello")

#with finally and else

try:
    n = int(input("Enter a number: "))
    result = 100/n


except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Please enter a non zero number")

else:
    print(result)
    print("No exception occured")

finally:
    print("Execution completed")

'''Raising exceptions using Raise keyword

#If want to intentionally generate an exception when a particular condition occurs'''

age = 17
if age<18:
    raise ValueError("Age must be 18 or above")
print("Eligible")



def withdraw(balance,amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    else:
        return balance-amount

x = withdraw(10000,1000)
print(x)
y = withdraw(100,1000)
print(y)

'''Exception handling in playwright

element not found
locator takes too long to become actionable
browser get closed unexpectedly'''







