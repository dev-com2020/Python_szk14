# slownik = {}
# slownik[1] = "Tomek"
# slownik[2] = "Tomek2"
# slownik[3] = "Tomek3"
# slownik['__imie'] = "Kasia"
# slownik[3] = "Łukasz"
# print(slownik.keys())
# print(slownik.values())
# print(slownik.items())
# slownik.pop(1)
# print(slownik['__imie'])
# # print(slownik['imie2'])
# print(slownik)
# print(slownik.get('__imie'))
# print(slownik.get('imie2'))

customers = [
    dict(id=1, total=2000, code=43333),
    dict(id=2, total=12000, code=4335553),
    dict(id=3, total=22000, code=43344433)
]

for customer in customers:
    print(customer['id'], customer['total'], customer['code'])

wynik = customers[0]['total']
print(wynik)

