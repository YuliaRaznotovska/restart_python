# 🔹 Task 4. Website Login + Logout
#
# Користувач вводить логін і пароль (умови як у твоєму завданні: логін — тільки літери, пароль — букви/цифри).
#
# Попросити підтвердити пароль.
#
# Якщо пароль збігається → "Welcome, you are logged in".
#
# Потім автоматично вивести "You have been logged out".
#
# Запросити логін і пароль ще раз.
#
# Якщо все збігається з першим вводом → "You are logged in again", інакше "Try again".

user_login = input('Type your login >>> ')
user_password = input('Type your password >>> ')
user_password_confirm = input('Confirm your password >>> ')

if user_login.isalpha() and user_password.isalnum() and user_password_confirm == user_password:
    print('Welcome, you are logged in')
    print('You have been logged out')
    user_login_double_verification = input('Confirm your login again >>> ')
    user_password_double_verification = input('Confirm your password again >>> ')
    if user_login_double_verification == user_login and user_password_double_verification == user_password:
        print('You are logged in again')
    else:
        print('Try again')
else:
    print('Try again')
