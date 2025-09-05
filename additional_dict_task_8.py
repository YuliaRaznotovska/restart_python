# Вивести штрих-коди всіх товарів, у яких вони заданні (не None).
products = {
    'iPhone 14': {'Ціна': 1200, 'Кількість': 10, 'Штрихкод': '111222333', 'Доступно': True},
    'Samsung Galaxy S22': {'Ціна': 1000, 'Кількість': 0, 'Штрихкод': None, 'Доступно': False},
    'MacBook Pro': {'Ціна': 2500, 'Кількість': 5, 'Штрихкод': '444555666', 'Доступно': True}
}
product_with_barcode = [product for product, info in products.items() if info['Штрихкод'] is not None]
for barcode in product_with_barcode:
    print(barcode)
