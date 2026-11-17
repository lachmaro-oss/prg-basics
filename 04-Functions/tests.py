import converters

print(f"5 m = {converters.m_to_cm(5)} cm")
print(f"10 ft = {converters.feet_to_cm(10)} cm")

# Sposób 2: import konkretnych funkcji (wywołujesz bezpośrednio po nazwie)
from converters import cm_to_m, cm_to_inch

print(f"250 cm = {cm_to_m(250)} m")
print(f"10 cm = {cm_to_inch(10):.2f} inches")
