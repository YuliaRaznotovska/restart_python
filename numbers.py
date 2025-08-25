import math

# first_number = int(input('Enter your number 1 '))
# second_number = int(input('Enter your number 2 '))

MSG_INPUT_NUMBER = 'Enter your number {position} (allowed numbers like 5 3.22)'
# first_number = float(input(MSG_INPUT_NUMBER.format(position=1)))
# second_number = float(input(MSG_INPUT_NUMBER.format(position=2)))

first_number = 0.2
second_number = 1.8

summa = first_number + second_number
print(summa)

multiplication = first_number * second_number
print(multiplication)

division_result = first_number / second_number
print(division_result)

print(round(multiplication, 2))
print(round(2.5, 0))
print(round(3.5, 0))
print(round(-3.5, 0))
print(round(-3.9))

print(abs(-3.555))
num_to_string = str(multiplication)
print(num_to_string)

milk_price = 40.35
milk_quanity = 0.125

# purchase = Decimal(5)
# purchase = Decimal(str(milk_quanity * milk_price))
# print(purchase)

PI = math.pi
print(PI)

mult_many = math.prod([5, 5, 5, PI])
print(mult_many)

powering_root = 25 ** 0.5
powering_root = math.sqrt(25)
print(powering_root)

round_floor = math.floor(-2.9)
print(round_floor)

round_ceil = math.ceil(-2.9)
print(round_ceil)
