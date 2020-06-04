cipher = input("Your ascii cypher here: ")
length = len(cipher)
if length % 8 != 0:
    print("Whoops, something's not right, please try again")
split_strings = []
n = 8

for index in range(0, len(cipher), n):
    split_strings.append(cipher[index: index + n])
print(split_strings)


for string in split_strings:
    count = 0
    dec = 0
    for char in string:
        if char == '1':
            dec = dec + 2**(7-count)
        count += 1
    print(chr(dec), end="")
