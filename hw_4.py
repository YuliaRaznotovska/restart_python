# отримати від користувача чисельне значення температури по цельсію і вивести в
# консоль значення вирахуваної температури по фаренгейту (точність - 1 знак після крапки) (ви ж хотіли математики)
from decimal import Decimal


user_temperature = float(input('Write the temperature >>> '))
user_temperature_fahrenheit = user_temperature * 9/5 + 32
user_temperature_fahrenheit_decimals = Decimal(user_temperature_fahrenheit).quantize(Decimal('0.1'))
print(user_temperature_fahrenheit_decimals)
