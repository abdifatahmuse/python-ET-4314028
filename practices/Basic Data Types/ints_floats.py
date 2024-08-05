print("Ints and Floats")

print(20 / 4)

print(4+4.0)

print(4*4.0)

print(4**4.0)

print(int(4**4.0))

print(int(4.5))

print(int(10.9))

print(int(14/3))

print(round(12 / 3, 2))

print(1.2 - 1.0)

print(14 / 3)

print(round(1.2 - 1.0, 2))


# Python code​​​​​​‌​‌‌​‌‌‌​‌​​​​‌​‌‌‌‌‌‌​​‌ below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    round = 0
    for digt in hexNum:
        if digt not in hexNumbers:
            return None
        hex = hexNumbers[digt]
        print(f' hex: {hex}')
        round += (hex * 16)+(hex * 1)
        print(round)

print(hexToDec('2A'))
print(hexToDec('A2'))
print(hexToDec('spam spam spam'))