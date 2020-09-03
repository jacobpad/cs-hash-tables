encode_table = {
    "A": "H",
    "B": "Z",
    "C": "Y",
    "D": "W",
    "E": "O",
    "F": "R",
    "G": "J",
    "H": "D",
    "I": "P",
    "J": "T",
    "K": "I",
    "L": "G",
    "M": "L",
    "N": "C",
    "O": "E",
    "P": "X",
    "Q": "K",
    "R": "U",
    "S": "N",
    "T": "F",
    "U": "A",
    "V": "M",
    "W": "B",
    "X": "Q",
    "Y": "V",
    "Z": "S",
    " ": " ",
}

# Reverse encode_table
decode_table = {value: key for key, value in encode_table.items()}


def encrypt(s):
    s = s.upper()

    result = ""

    for i in s:
        result += encode_table[i]

    return result


def decrypt(s):
    s = s.upper()

    result = ""

    for i in s:
        result += decode_table[i]

    return result


print(encrypt("Jacob is cool"))
print(decrypt("thyez pn yeeg"))
print(decrypt("Jacob is cool"))
