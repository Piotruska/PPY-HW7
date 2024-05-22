import os

from HW7.AditionalMethodsForFun import display_loading_bar
from HW7.Task3 import time_execution


def require_auth(func):
    def wrapper(*args, **kwargs):
        user = kwargs.get('user')
        password = kwargs.get('password')
        if user in user_db and user_db[user] == password:
            return func(*args, **kwargs)
        else:
            return "Authentication Failed"
    return wrapper

def load_user_db():
    user_db = {}
    if os.path.exists('UserPasswordFile.txt'):
        with open('UserPasswordFile.txt', 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                user_db[username] = password
    return user_db

def save_user_db(user_db):
    with open('UserPasswordFile.txt', 'w') as file:
        for user, password in user_db.items():
            file.write(f'{user},{password}\n')

def add_or_update_user(username, password, **kwargs):
    user = kwargs.get('auth_user')
    user_password = kwargs.get('auth_password')
    if user == "admin" and user_db["admin"] == user_password:
        user_db[username] = password
        save_user_db(user_db)
        return "User added/updated successfully"
    else:
        return "Authentication required"

user_db = load_user_db()

@require_auth
@time_execution
def secure_function():
    display_loading_bar()
    print("")
    return "Secure Function Executed"

while True:
    print("\nAuthentication Test Menu")
    print("1. Test secure function")
    print("2. Add/Update user")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        user = input("Enter username: ")
        password = input("Enter password: ")
        result = secure_function(user=user, password=password)
        print(result)
    elif choice == '2':
        auth_user = input("Enter your username for authentication: ")
        auth_password = input("Enter your password for authentication: ")
        user = input("Enter username to add/update: ")
        password = input("Enter new password: ")
        print(add_or_update_user(user, password, auth_user=auth_user, auth_password=auth_password))
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
