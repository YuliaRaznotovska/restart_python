# Вивести список всіх email тих працівників, у кого є номер телефону.
employees = {
    'Анна Іванова': {'Відділ': 'Маркетинг', 'Email': 'anna@company.com', 'Телефон': '+380501112233', 'Стаж': 3},
    'Богдан Петренко': {'Відділ': 'IT', 'Email': 'bogdan@company.com', 'Телефон': None, 'Стаж': 5},
    'Ольга Коваленко': {'Відділ': 'HR', 'Email': 'olga@company.com', 'Телефон': '+380501223344', 'Стаж': 2}
}
employees_with_phone = [employee['Email'] for employee in employees.values() if employee['Телефон'] is not None]
print('Список працівників, у кого є номер телефону: ')
for email in employees_with_phone:
    print(email)
