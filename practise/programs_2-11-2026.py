#write a function to count vowels in a string
def count_vowels(word):
    count = 0
    for letter in word:
        if letter in "aeiouAEIOU":
            count += 1
    return count

print(count_vowels('python'))

#create a function to check whether a test case has passed or failed
def check_status(status):
    if 'passed' in status:
        print('passed')
    if 'failed' in status:
        print('Failed')

output_text1 = '12 test passed'
output_text2 = '10 text passed and 2 failed'

check_status(output_text1)
check_status(output_text2)


# create a function to check whether a username is valid [length more than 5]
username = input("enter username: ")
def check_valid_username(username):
    if len(username)>5:
        return True
    else:
        return False


result = check_valid_username(username)
print(result)
password = input("enter password: ")


#create a function to validate an email address(can include,char,digits,.com/in,gmail,@.Always start with characters)
email = input("Enter an email: ")

def check_email(email):
    if (email and email[0].isalpha()
        and '@' in email
        and "gmail" in email
        and " " not in email
        and (email.endswith(".com")
        or email.endswith(".in"))):

        print(f"{email} is valid")
    else:
        print(f"{email} is invalid")


check_email(email)

#method 2
email = input("Enter an email: ")

def check_email(email):
    firstchar = email[0]
    if ((not firstchar.isdigit())
         and '@' in email
         and "gmail" in email
         and " " not in email
         and (email.endswith(".com")
         or email.endswith(".in"))):

        print(f"{email} is valid")
    else:
        print(f"{email} is invalid")





#create a function to convert a browser name into lowercase
browser_name = input("enter browser_name: ")
def convert_browser_name(browser_name):
    print(browser_name.lower())

convert_browser_name(browser_name)

#in case of strict check,always use '=="
#in case of return statement check all conditions are fulfilled in prior
#always use return statements when we want to store the output
#execution continue after print but after return,function exit

