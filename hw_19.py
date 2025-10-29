# # code 1
# with open('airport-codes_csv.csv', mode='r', encoding='utf-8') as my_file:
#     content = my_file.readlines()
#     for line in content:
#         airport = line.strip().split(';')
#         airport_iso_country = airport[5]
#         airport_name = airport[2]
#         if airport_iso_country == 'UA':
#             print(airport_name)
#
#
# # code 2
# import csv
#
# with open('airport-codes_csv.csv', mode='r', encoding='utf-8') as file:
#     reader = csv.DictReader(file, fieldnames=['ident', 'type', 'name', 'elevation_ft', 'continent', 'iso_country'],
#                             delimiter=';')
#     for airport in list(reader)[1:]:
#         if airport['iso_country'] == 'UA':
#             print(airport['name'])

# Task 1 — cities.csv
#
# Goal: Print names of cities in France (FR)
# with open('cities.csv', mode='r', encoding='utf-8') as my_file:
#     content = my_file.readlines()[1:]  # skip header
#     for line in content:
#         city_info = line.strip().split(';')
#         iso_country = city_info[2]
#         city_name = city_info[0]
#         if iso_country == 'FR':
#             print(city_name)

# Task 2 — employees.csv
#
# Goal: Print names of employees with salary > 5000
# with open('employees.csv', mode='r', encoding='utf-8') as my_employees:
#     content = my_employees.readlines()[1:]
#     for line in content:
#         employee_info = line.strip().split(';')
#         employee_name = employee_info[0]
#         employee_salary = float(employee_info[2])
#         if employee_salary > 5000:
#             print(employee_name)

# Task 3 — students.csv
#
# Goal: Print names and grades of students with grade ≥ 90
# with open('students.csv', mode='r', encoding='utf-8') as students_file:
#     content = students_file.readlines()[1:]
#     for line in content:
#         student_info = line.strip().split(';')
#         student_name = student_info[0]
#         student_grade = float(student_info[1])
#         if student_grade >= 90:
#             print(f'{student_name} - {student_grade}')

# # Task 4 — products.csv
# #
# # Goal: Print product names in category “Electronics”
# with open('products.csv', mode='r', encoding='utf-8') as products_file:
#     content = products_file.readlines()[1:]
#     for line in content:
#         product_info = line.strip().split(';')
#         product_name = product_info[0]
#         product_category = product_info[1]
#         if product_category == 'Electronics':
#             print(product_name)

# Task 5 — airport-codes_csv.csv
#
# Goal: Count airports per iso_country
with open('airport-codes_csv_2.csv', mode='r', encoding='utf-8') as airports_file:
    content = airports_file.readlines()[1:]
    airport_counter = {}
    for line in content:
        airport_info = line.strip().split(';')
        airport_iso_country = airport_info[5]
        airport_counter[airport_iso_country] = airport_counter.get(airport_iso_country, 0) + 1


for country, count in airport_counter.items():
    print(f'{country} - {count}')



