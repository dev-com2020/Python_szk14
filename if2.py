age = 120

if age > 90:
    print("Too old")
elif age < 0:
    print("Not yet be born")
elif age >= 18:
    print("party time")
else:
    "to young"

age = input("wprowadź wiek")

match age:
    case "90":
        print("too old")
    case "18":
        print("party time")
    case "0":
        print("Not yet be born")
    case _:
        print(":(")






