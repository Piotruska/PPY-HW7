from AditionalMethodsForFun import display_loading_bar
from Task3 import time_execution

user_db = {
    'PiotrRutkowski': 'PiotrRutkowski1234!',
    'PiotrDebski': 'PiotrDebski1234!',
    'P': 'P'

}


@time_execution
def require_auth(func):
    def wrapper(*args, **kwargs):
        user = kwargs.get('user')
        password = kwargs.get('password')
        if user in user_db and user_db[user] == password:
            return func(*args)
        else:
            return "Authentication Failed"

    return wrapper


@require_auth
@time_execution
def secure_function():
    display_loading_bar()
    print("")
    return "Secure Function Executed"


while True:
    print("\nAuthentication Test Menu")
    print("1. Test secure function")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        user = input("Enter username: ")
        password = input("Enter password: ")
        result = secure_function(user=user, password=password)
        print(result)
    elif choice == '2':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
