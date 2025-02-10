number = 1

while number < 25:

    # if number > 10 and number < 15:
    if 10 <= number <= 15:
        number += 1
        continue

    print(f'{number}')
    number += 1
