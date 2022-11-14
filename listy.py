lista = []
lista.append("Tomek")
lista.append(54)
lista.append(5.55)
lista.append(True)
lista.pop(1)
lista.remove(True)
lista[1] = "Jakub"
lista.insert(1, 654)
lista.clear()
lista.append(754)
lista.append(254)
# lista.append("Tomek")
lista.append(1254)
lista.append(54)
lista.sort()
lista.reverse()
print(lista)
imie = "Michał"
nowa_lista = list(imie)

nowa_lista.extend((1, 2, 3))
nowa_lista.extend("...")
print(nowa_lista)

liczby = [1, 3, 5, 7]
liczby2 = [2, 4, 6, 8]
suma = liczby + liczby2 * 2
suma.sort()
print(suma)
zbior = set(suma)
zbior2 = {7, 8, 9, 0}
print(zbior.difference(zbior2))
print(zbior2.difference(zbior))
print(zbior.intersection(zbior2))
print(zbior2.intersection(zbior))


# print(zbior)
# suma = list(zbior)
# print(suma)

# print(min(liczby))
# print(max(liczby))
# print(sum(liczby))
