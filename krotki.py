ROK = 2022
zmienne = "Tomek", "Jacek", "Kasia"
print(zmienne[0])
print(zmienne[0:2])
print(type(zmienne))
# zmienne = 54, 433, 666, 234566
# print(zmienne[0])
# print(zmienne[0:2])
# print(type(zmienne))
krotka = (ROK, 43, "Tomek", 54.5, 54 / 3, (44, 55, 66))
print(krotka)
# imie = krotka[2]
# print(imie)
# imie1, imie2, imie3 = zmienne
imie1, *imie2 = zmienne
# *imie1, imie2 = zmienne
print(imie1)
print(imie2)
# print(imie3)
