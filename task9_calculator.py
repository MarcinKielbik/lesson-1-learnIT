number1 = float(input("Podaj pierwszą liczbę: "))
number2 = float(input("Podaj drugą liczbę: "))

symbol = input("Podaj znak działania (+, -, *, /): ")

if symbol == "+":
    print(number1 + number2)
elif symbol == "-":
    print(number1 - number2)
elif symbol == "*":
    print(number1 * number2)
elif symbol == "/":
    if number2 != 0:
        print(number1 / number2)
    else:
        print("Nie można dzielić przez zero!")
else:
    print("Nieprawidłowy znak działania!")