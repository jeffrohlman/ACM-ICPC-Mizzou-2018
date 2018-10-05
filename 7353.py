code = "ABCZ"
cipher = "HAPPYBIRTHDAYCACEY"
counter = 0
found = "FAIL"

for i in range(len(cipher)):
    if cipher[i] == code[counter]:
        counter += 1
        if counter == len(code):
            found = "SUCCESS"
            break
    elif counter != 0 and cipher[i] == code[counter - 1]:
        break

print(found)
