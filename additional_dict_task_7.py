# Вивести всі автомобілі, у яких заданий номер (не None).
cars = {
    'Tesla Model 3': {'Власник': 'Ігор', 'Рік': 2020, 'Номер': 'AA1234BB', 'Продано': False},
    'BMW X5': {'Власник': 'Олена', 'Рік': 2018, 'Номер': None, 'Продано': True},
    'Audi A4': {'Власник': 'Сергій', 'Рік': 2019, 'Номер': 'BB5678CC', 'Продано': False}
}
cars_with_num = [car for car, info in cars.items() if info['Номер'] is not None]
for name in cars_with_num:
    print(name)
