import os
lst = os.listdir('users')
print(lst)

# придумать логин
login = input('What is your login? ')
while login + '.txt' in lst or len(login) < 5:
    if login + '.txt' in lst:
        print('Try again', 'Этот пользователь уже есть')
    if len(login) < 5:
        print('Very few simbols')
    login = input('What is your login? ')

# пароль
password = input('What is your password? ')
while len(password) < 8 or '0' not in password and '1' not in password and '2' not in password and '3' not in password and '4' not in  password and '5' not in password and '6' not in password and '7' not in password and '8' not in password and '9' not in password:
    if len(password) < 8:
        print('Very few simbols')
    if '0' not in password and '1' not in password and '2' not in password and '3' not in password and '4' not in  password and '5' not in password and '6' not in password and '7' not in password and '8' not in password and '9' not in password:

        print('Must  be number')
    password = input('What is your password? ')
# password = str(password.encode('utf - 32'))

# name's user
name = input('What is your name? ')
while not name.isalpha():
    print('Only letter')
    name = input('What is your name? ')

# last name
surname = input('What is your surname? ')
while not surname.isalpha():
    print('Only letter')
    surname = input('What is your surname? ')

# mail
mail = input('What is your E-mail?')
while '@' not in mail and '.' not in mail:
    print('It can not be')
    mail = input('What is your E-mail? ')

file = open('users/' + login + '.txt', 'w')
file.write(login + '\n')
file.write(password + '\n')
file.write(name + '\n')
file.write(surname + '\n')
file.write(mail + '\n')



# What is your login? serena
# What is your password? fut567890

# What is your login? hilopa
# What is your password? 123456789






























