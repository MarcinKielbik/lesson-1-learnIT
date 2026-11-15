print("Kantor")

dollar: float = 4.0

pln = float(input("Podaj kwotę w złotówkach: "))

exchange = round(pln / dollar, 2)

print(f"Kwota w dolarach wynosi: {exchange}")