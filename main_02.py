# Napisite program koji ce korisniku ispisati izbornik s opcijama aplikacije.


while True:
    print()
    print('Izbornik')
    print('1. Novi zadatak')
    print('2. Ispis svih zadataka')
    print('3. Izlaz')
    print()
    choice = input('Upisite broj ispred akcije koju zelite pokrenuti: ')
    print()

    if choice == '3':
        break

print()
print('Kraj izvrsavanja aplikacije')
print()
