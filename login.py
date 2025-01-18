import time

user_name = 'raja'
password = 'secret'

username_input = input(" Enter UserName: ")
password_input = input("Enter Password: ")

if username_input == user_name and password_input == password:
    print("Access granted")
    print("Please Wait")
    time.sleep(5)
    print("Ok... Loading....")
    time.sleep(1)
    print('.......')
    time.sleep(1)
    print('.....')
    print("Alright, you have security clearance. Pulling up the secret mainframe")
elif username_input == user_name and password_input != password:
    print('Password is incorrect..')
elif username_input != user_name and password_input == password:
    print('UserName is incorrect..')
else:
    print('you need to check the both fields..')
