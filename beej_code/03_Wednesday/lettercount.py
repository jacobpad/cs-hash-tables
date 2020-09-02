# Count the number of occurrences of a letter in a string
# "Hello there!"

def letter_count(s):
	d = {}

	for c in s:

		if c.isspace():
			continue

		c = c.upper()

		if c not in d:
			#d[c] = 0
			d[c] = 1
		else:
			d[c] += 1

	return d

print(letter_count("Hello there!"))
