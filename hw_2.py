# з клавіатури вводяться прізвища (можуть вводитися як з малої, так і з великої літери) учнів. за допомогою
# split створити список учнів (всі прізвища строго з великої літери),
# упорядкувати за алфавітом та вивестив консоль за допомогою циклу for
surname = input('Write your surname >>>> ').title()
surname_list = surname.split()
surname_list.sort()

for student in surname_list:
   print(student)
