# people = ['Nick', 'Rick', 'Roger']
# ages = [23, 24, 23]
#
# pos = 0
# while pos < len(people):
#     person = people[pos]
#     age = ages[pos]
#     print(person, age)
#     pos += 1

liczby = []
while True:
    print("Wprowadz liczbę")
    liczba = input(":")
    liczby.append(liczba)
    if liczba == "stop":
        for i in liczby:
            print(i * 2)
        break
    print(liczby)
