# 🔹 Task 3. Simple Quiz Login
#
# Зробити міні-квіз з входом:
#
# Користувач вводить ім’я (тільки літери).
#
# Користувач вводить пароль (букви + цифри).
#
# Якщо логін і пароль підходять — починається квіз:
#
# Запитати: "What is 2+2?"
#
# Якщо відповідь 4, вивести "Correct, you are logged in!".
#
# Інакше — "Wrong answer, access denied".

user_name = input('Type your name >>> ')
user_password = input('Type your password >>> ')

if user_name.isalpha() and user_password.isalnum():
    quiz_question = input('What is 2+2?')
    if quiz_question == '4':
        print('Correct, you are logged in!')
    else:
        print('Wrong answer, access denied')
else:
    print('Wrong login or password')
