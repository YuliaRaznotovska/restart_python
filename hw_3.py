# отримати від користувача стрічку, і опрацювати її, і утворити нову стрічку, яка складається тільки із літер в
# апперкейсі, які отримані у вхідному аргументі
# (наприклад, отримавши від користувача стрічку "олдварпоОРПлдоролр5656 321!!!.юб," на вихід отримаємо "ОРП")
user_line = input('Write your message >>>> ')
user_line.split()
new_user_line = []
for char in user_line:
    if char.isupper():
        new_user_line.append(char)
    else:
       continue
print(''.join(new_user_line))

