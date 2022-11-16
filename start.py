# import pakiet.funcdef
#
# print(pakiet.funcdef.square(10))
# print(pakiet.funcdef.cube(10))

import pakiet.funcdef as p

a = p.square(10)
b = p.cube(10)

with open('test.log', 'w', encoding='utf-8') as f:
    f.write(str(a))
    f.write(str(b))

input("Wciśnij ENTER aby zakończyć...")

from pakiet.funcdef import square, cube

# print(square(10))
# print(cube(10))

# from .first import godziny
