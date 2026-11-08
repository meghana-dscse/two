key = input("Enter key: ")
text = input("Enter plaintext: ").upper().replace(" ", "")

n = len(key)

while len(text) % n != 0:
    text += 'X'

matrix = [list(text[i:i+n]) for i in range(0, len(text), n)]

print("Matrix:")
for row in matrix:
    print(row)

cipher = ""

for k in key:
    col = int(k) - 1
    for row in matrix:
        cipher += row[col]

print("Encrypted text:", cipher)
