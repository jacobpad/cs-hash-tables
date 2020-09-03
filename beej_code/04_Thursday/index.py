records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Carol", "Sales"),
    ("Dave", "Engineering"),
    ("Erin", "Engineering"),
    ("Frank", "Engineering"),
    ("Grace", "Marketing")
]

def add_to_index(name, dept):
	if dept not in dept_idx:
		dept_idx[dept] = []

	dept_idx[dept].append(name)

dept_idx = {}

# Build the index
for name, dept in records:
	add_to_index(name, dept)

def add_employee(name, dept):
	records.append((name, dept))

	add_to_index(name, dept)

# Do quick lookups
print(dept_idx["Sales"])

add_employee("Beej", "Sales")

print(dept_idx["Sales"])
