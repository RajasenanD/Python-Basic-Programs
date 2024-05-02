import random
print("welcome to password generator")
randomchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!£$%^&*()"
pswrd = int(input("enter number of passwords to be generated : "))
pswrdlen = int(input("enter the length of passwords: "))

print("Here are the passwords:")

for x in range(pswrd):
    pwd =""
    for cha in range(pswrdlen):
        pwd = pwd + random.choice(randomchars)       

    print(pwd)

