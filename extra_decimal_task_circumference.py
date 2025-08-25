import math
from decimal import Decimal

user_radius = float(input('Write radius >>> '))

circum = 2 * math.pi * user_radius

circum_result = Decimal(str(circum)).quantize(Decimal('0.01'))

print(circum_result)
