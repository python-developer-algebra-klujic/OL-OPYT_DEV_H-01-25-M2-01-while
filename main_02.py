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

    if choice == '1':
        print('Kreiranje novog zadatka')
        task = input('Upisite tekst novog zadatka: ')
        print()
        print(f'Kreirali ste zadatak:\n\t{task}')
        print()

    elif choice == '2':
        # TODO Napraviti funkcionalnost dohvata i prikaza svih zadataka
        # Implementirati ovaj dio koda tako da se ispise 10 zadataka na nacin:
        # Zadatak 1. - Ovo je tekst 1. zadatka!

        # Golubovic - for petlja
        # for i in range(1, 11):
        #     print(f'Zadatak {i}. - Ovo je tekst {i}. zadatka!')

        # Vojic - while petlja
        i = 1
        while i < 11:
            print(f'Zadatak {i}. - Ovo je tekst {i}. zadatka!')
            # i = i + 1
            i += 1 # Ovo je identicno liniji iznad, ali je kraci zapis.

        # pass

    elif choice == '3':
        break

    else:
        print('Upisali ste nepostojecu opciju iz izbornika! Pokusajte ponovno!')


print()
print('Kraj izvrsavanja aplikacije')
print()
