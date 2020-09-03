# Plaintext:  HELLOWORLD
# Ciphertext: DOGGEBEUGW

encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

decode_table = {value:key for key, value in encode_table.items()}

decode_table = {}

for key, value in encode_table.items():
	decode_table[value] = key

def encrypt(s):
	result = ''

	for c in s:
		c = c.upper()

		if c.isalpha():
			result += encode_table[c]
		else:
			result += c

	return result

def decrypt(s):
	result = ''

	for c in s:
		c = c.upper()

		if c.isalpha():
			result += decode_table[c]
		else:
			result += c

	return result


print(encrypt("Hello, world!"))
print(decrypt("DOGGE, BEUGW!"))

