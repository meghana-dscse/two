def encrypt(text, key):
    rails = [[] for i in range(key)]

    row = 0
    direction = 1

    for ch in text:
        rails[row].append(ch)

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    result = ""

    for rail in rails:
        for ch in rail:
            result += ch

    return result


def decrypt(cipher, key):
    pattern = []
    row = 0
    direction = 1

    for i in range(len(cipher)):
        pattern.append(row)

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    rails = [[] for i in range(key)]

    index = 0
    for r in range(key):
        count = pattern.count(r)
        rails[r] = list(cipher[index:index + count])
        index += count

    result = []
    positions = [0] * key

    for r in pattern:
        result.append(rails[r][positions[r]])
        positions[r] += 1

    return ''.join(result)


text = input("Enter message: ")
key = int(input("Enter key: "))

encrypted = encrypt(text, key)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)

