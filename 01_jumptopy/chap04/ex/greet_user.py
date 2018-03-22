import sys

def greet_users(usernames):
    for i in usernames:
        print("Hello, " + i[0].upper()+i[1:]+"!")

usernames = sys.argv[1:]
greet_users(usernames)
