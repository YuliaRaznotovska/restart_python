# Написати програму, де:
# Користувач вводить email (повинен містити символ @).
# Користувач вводить пароль (мінімум 6 символів).
# Попросити підтвердити пароль.
# Якщо все вірно — вивести "Registration successful", інакше "Invalid email or password".
user_email = input('Enter your email >>> ')
at_symbol = '@'
user_password = input('Enter your password >>> ')
password_confirmation = input('Confirm your password >>> ')
password_length = len(user_password)
if at_symbol in user_email and password_length > 5 and password_confirmation == user_password:
    print('Registration successful')
else:
    print('Invalid email or password')
