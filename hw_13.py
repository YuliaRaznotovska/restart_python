# # є url https://dummyjson.com/users (100 сторінок)
# #
# # вивести в консоль середній вік чоловіків з Brown волоссям,
# # а також сформувати список людей, що проживають в місті Louisville
import requests

url = 'https://dummyjson.com/users?limit=100'

response = requests.get(url)

users_data = response.json()

users_clean_data = users_data['users']

brown_hair_men_number = 0
brown_hair_men_age_list = []
louisville_citizens_list = []

for man in users_clean_data:
    if man['hair']['color'] == 'Brown' and man['gender'] == 'male':
        brown_hair_men_number += 1
        man_age = man['age']
        brown_hair_men_age_list.append(man_age)

for person in users_clean_data:
    if person['address'].get('city') == 'Louisville':
        person_info = f"{person['firstName']} {person['lastName']}"
        louisville_citizens_list.append(person_info)

average_age_brown_hair_men = sum(brown_hair_men_age_list) / brown_hair_men_number
print(int(average_age_brown_hair_men))
print(louisville_citizens_list)

# import requests
#
# url = 'https://dummyjson.com/users?limit=100'
# response = requests.get(url)
#
# users_data = response.json()
# users_clean_data = users_data['users']
#
# brown_hair_men_number = 0
# brown_hair_men_age_list = []
# louisville_citizens_list = []
#
# for man in users_clean_data:
#     if man['hair']['color'] == 'Brown' and man['gender'] == 'male':
#         brown_hair_men_number += 1
#         brown_hair_men_age_list.append(man['age'])
#
# for person in users_clean_data:
#     if person['address'].get('city') == 'Louisville':
#         person_info = f"{person['firstName']} {person['lastName']}"
#         louisville_citizens_list.append(person_info)
#
# if brown_hair_men_number > 0:
#     average_age_brown_hair_men = sum(brown_hair_men_age_list) / brown_hair_men_number
#     print("Average age of brown-haired men:", int(average_age_brown_hair_men))
# else:
#     print("No brown-haired men found")
#
# print("Louisville citizens:", louisville_citizens_list)
