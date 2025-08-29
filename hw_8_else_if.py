user_login = input('Write your login >>> ')
user_password = input('Write your password >>> ')

if user_login.isalpha() and user_password.isalnum():
    user_password_confirmation = input('Confirm your password >>> ')
    if user_password_confirmation == user_password:
        print('You are logged in')
        print('You are not logged because of the teacher')
        user_login_recheck = input('Write your login again >>> ')
        user_password_recheck = input('Write your password again >>> ')
        if user_login_recheck == user_login and user_password_recheck == user_password:
            print('You are logged in')
        else:
            print('Login or Password does not match')
    else:
        print('Login or Password does not match')
else:
    print('Login or Password does not match')
