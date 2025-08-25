import math
from decimal import Decimal

user_radius = float(input('Write radius >>>'))

surface = 4 * math.pi * (user_radius ** 2)

surface_result = Decimal(str(surface)).quantize(Decimal('0.01'))

print(surface_result)
