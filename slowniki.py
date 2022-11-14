slownik = {}
slownik[1] = "Tomek"
slownik[2] = "Tomek2"
slownik[3] = "Tomek3"
slownik['imie'] = "Kasia"
slownik[3] = "Łukasz"
print(slownik.keys())
print(slownik.values())
print(slownik.items())
slownik.pop(1)
print(slownik['imie'])
# print(slownik['imie2'])
print(slownik)
print(slownik.get('imie'))
print(slownik.get('imie2'))


