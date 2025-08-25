import math
from decimal import Decimal

user_radius = float(input('Write radius >>> '))

square = math.pi * (user_radius ** 2)

square_result = Decimal(str(square)).quantize(Decimal('0.01'))

print(square_result)
