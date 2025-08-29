# 🔹 Task 2. ATM PIN Check
#
# Створити програму-банкомат:
#
# Користувач вводить свій PIN (4 цифри).
#
# Якщо PIN складається тільки з цифр і має довжину 4 → запитати повторний ввід.
#
# Якщо обидва рази збігається — "Access granted".
#
# Інакше — "Access denied".

user_pincode = input('Type your pincode >>> ')

if user_pincode.isdigit() and len(user_pincode) == 4:
    user_pincode_confirm = input('Confirm your pincode >>> ')
    if user_pincode_confirm == user_pincode:
        print('Access granted')
    else:
        print('Access denied')
else:
    print('Access denied')
