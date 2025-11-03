# написати клас автомобіль
#
# має мати атрибути
#
# рік випуску (за замовчуванням 2020, в ініт ПЕРЕДАЄТЬСЯ)
# виробник
# марка
# пробіг (за замовчуванням 0, в ініт не передається)
# витрата палива (флоатове значення)
# перевизначити метод __str__ (значення на ваш вибір)
#
# написати проперті метод для визначення віку в роках (вираз datetime.today().year вам допоможе)
#
# створити кілька екземплярів автомобілів
# import datetime
#
#
# class Car:
#     def __init__(self, manufacturer: str, make: str, fuel_consumption: float, release_year: int = 2020) -> None:
#         self.release_year = release_year
#         self.manufacturer = manufacturer
#         self.make = make
#         self.__mileage = 0
#         self.fuel_consumption = fuel_consumption
#
#     def __str__(self):
#         return f'Car: Make - {self.make}, Manufacturer - {self.manufacturer}, Release Year - {self.release_year}, ' \
#                f'Fuel Consumption - {self.fuel_consumption}, Mileage - {self.__mileage}, Car age - {self.age}'
#
#     @property
#     def age(self):
#         car_age = datetime.date.today().year - self.release_year
#         return car_age
#
#
# car1 = Car('Nissan', 'Almera', 100.5)
# print(car1)


# Task 2
# написати клас Телефон
#
# має мати атрибути:
# виробник
# модель
# рік випуску (за замовчуванням 2022, в ініт передається)
# кількість SIM-карт (за замовчуванням 1, в ініт не передається)
# ємність батареї (флоатове значення)
#
# перевизначити метод __str__ для виведення повної інформації
#
# написати проперті метод для визначення віку телефону (у роках)
#
# створити кілька екземплярів телефонів
# import datetime
#
#
# class Phone:
#     def __init__(self, manufacturer: str, make: str, battery_capacity: float, release_year: int = 2022) -> None:
#         self.manufacturer = manufacturer
#         self.make = make
#         self.battery_capacity = battery_capacity
#         self.sim_number = 1
#         self.release_year = release_year
#
#     def __str__(self):
#         return f'Model: {self.make}, Manufacturer: {self.manufacturer}, Battery Capacity: {self.battery_capacity}. ' \
#                f'Released in {self.release_year}, Number of sims: {self.sim_number}, Phone age is {self.age} years'
#
#     @property
#     def age(self):
#         phone_age = datetime.date.today().year - self.release_year
#         return phone_age
#
#
# phone1 = Phone('Nokia A97', 'Nokia', 4500, 2005)
# phone2 = Phone('Samsung Galaxy A36', 'Samsung', 5000, 2019)
# print(phone1)
# print(phone2)

# Task 3
# написати клас Квиток
#
# має мати атрибути:
# пункт відправлення
# пункт призначення
# ціна (флоат)
# дата подорожі (в форматі 'YYYY-MM-DD', передається в ініт)
# номер місця (за замовчуванням None)
#
# перевизначити метод __str__ для гарного відображення інформації
#
# написати проперті метод, який повертає кількість днів до поїздки
# (використати datetime.date.today())
#
# створити кілька екземплярів квитків
# import datetime
#
#
# class Ticket:
#     def __init__(self, departure: str, arrival: str, price: float, trip_date: str) -> None:
#         self.departure = departure
#         self.arrival = arrival
#         self.price = price
#         self.trip_date = datetime.date.fromisoformat(trip_date)
#         self.seat_num = None
#
#     def __str__(self):
#         return f'Departure from {self.departure}, Arrival in {self.arrival}, Ticket Price is {self.price} Euro,' \
#                f' Trip date is {self.trip_date}, Days left {self.days_to_trip}, Seat num: {self.seat_num}'
#
#     @property
#     def days_to_trip(self):
#         days_left = (self.trip_date - datetime.date.today()).days
#         return days_left
#
#
# trip1 = Ticket('Berlin', 'Prague', 30, '2025-12-31')
# trip2 = Ticket('Paris', 'Kyiv', 50, '2026-03-07')
# print(trip1)
# print(trip2)

# Task 4
# написати клас Будинок
# має мати атрибути:
# адреса
# кількість поверхів
# рік побудови (за замовчуванням 2000, в ініт передається)
# площа (флоат)
# кількість мешканців (за замовчуванням 0, в ініт не передається)
# перевизначити метод __str__, щоб виводити короткий опис будинку
# написати проперті метод для визначення віку будинку
# створити кілька екземплярів будинків
# import datetime
#
#
# class House:
#     def __init__(self, address: str, floors_num: int, square: float, built_year: int = 2000) -> None:
#         self.address = address
#         self.floors_num = floors_num
#         self.square = square
#         self.built_year = built_year
#         self.tenant_num = 0
#
#     def __str__(self):
#         return f'Address: {self.address}, Number of floors: {self.floors_num}, Square: {self.square} m2,' \
#                f' Built in {self.built_year}, People living: {self.tenant_num}, House age: {self.age} years'
#
#     @property
#     def age(self):
#         house_age = datetime.date.today().year - self.built_year
#         return house_age
#
#
# house1 = House('Baker street, 15', 3, 65, 1956)
# house2 = House('Raven street, 30', 8, 124, 2012)
# print(house1)
# print(house2)

# task 5
# написати клас Книга
#
# має мати атрибути:
# назва
# автор
# рік видання (за замовчуванням 2010, в ініт передається)
# кількість сторінок
# рейтинг (флоатове значення, за замовчуванням 0)
#
# перевизначити метод __str__, щоб красиво виводити дані про книгу
#
# написати проперті метод для визначення віку книги (у роках)
#
# створити кілька екземплярів книг
import datetime


class Book:
    def __init__(self, name: str, author: str, page_num: int, publish_year: int = 2010) -> None:
        self.name = name
        self.author = author
        self.page_num = page_num
        self.publish_year = publish_year
        self.rating = 0

    def __str__(self):
        return f'Name: {self.name}, author: {self.author}, number of pages: {self.page_num}, ' \
               f'published in {self.publish_year}, rating: {self.rating}, book age: {self.age} years'

    @property
    def age(self):
        book_age = datetime.date.today().year - self.publish_year
        return book_age


book1 = Book('HP', 'JK Rowling', 365, 1998)
book2 = Book('LR', 'Tolkien', 1500, 1985)
print(book1)
print(book2)
