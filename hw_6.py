import math


user_radius = float(input('Write the radius >>> '))
volume_result = (user_radius ** 3) * math.pi * 4 / 3

print(round(volume_result, 2))
