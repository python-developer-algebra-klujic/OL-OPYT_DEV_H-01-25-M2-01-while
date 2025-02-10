# Napisite program koji omogucava korisniku unos kontakata (ime i prezime; email; telefon),
# koliko god to korisnik zeli.

while True:
    # forma za unos kontakta
    print("Unos novog kontakta:")
    name = input("Ime i prezime: ")
    email = input("Email: ")
    phone = input("Telefon: ")

    print(f"Ime i prezime: {name}, Email: {email}, Telefon: {phone}")

    # contact = {"Ime i prezime": name, "Email": email, "Telefon": phone}
    # contacts.append(contact)

    # odluka unosa novog kontakta
    choice = input("Unesite još jedan kontakt? (da/ne): ")
    if choice != "da":
        break


# Odjavna poruka

# print("\n kontakti:")
# for contact in contacts:
#     print(f"Ime i prezime: {contact['Ime i prezime']}, Email: {contact['Email']}, Telefon: {contact['Telefon']}")

print('Fin!')
print('Vege!')
