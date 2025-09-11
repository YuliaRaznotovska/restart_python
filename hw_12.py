# створити АРІ на базі гугл таблиці, містить поля "назва товару", "опис товару", "ціна" (інтова чи флоат),
# "залишок" (інтовий чи флоат), "містить глютен" (булеве тру чи фолс (виставляєте прапорцем, як добавити -
# дивіться в прикріпленому відеофайлі). заповнити мінімум 10 позицій
# за допомогою requests завантажити створені дані. порахувати вартість всіх товарів та товарів без глютена.
import requests

url = 'https://script.google.com/macros/s/AKfycbyZWhPyfux81ciZMR4hdgdyorlOoRy6O3wIgn3zyeBIIAG5wG8oGbLj-VLSTbcYf5Cj1Q/exec'

response = requests.get(url)

inner_data = response.json()

clean_data = inner_data['data']

product_total_cost_list = []

for product in clean_data:
    product_total_cost = product['in_stock'] * product['price']
    product_total_cost_list.append(product_total_cost)

print(f'вартість всіх товарів = {sum(product_total_cost_list)}')

gluten_free_total_cost_list = []

for product in clean_data:
    if product['contains_gluten'] is False:
        gluten_free_product_total_cost = product['in_stock'] * product['price']
        gluten_free_total_cost_list.append(gluten_free_product_total_cost)

print(f'вартість всіх товарів без глютена = {sum(gluten_free_total_cost_list)}')
