friends = ["Aditya", "Riya", "Samar", "Neha", "Pranav"]

friends_with_lengths = [(name, len(name)) for name in friends]

print("Friends and their name lengths:")
for friend in friends_with_lengths:
    print(friend)
# Your expenses
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

# Partner's expenses
partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate total expenses
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("\nYour total expenses:", your_total)
print("Partner's total expenses:", partner_total)

if your_total > partner_total:
    print("You spent more overall.")
elif partner_total > your_total:
    print("Your partner spent more overall.")
else:
    print("Both spent the same amount.")

max_diff = 0
significant_category = ""

for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])
    if diff > max_diff:
        max_diff = diff
        significant_category = category

print(f"\nCategory with the most difference: {significant_category}")
print(f"Difference in spending: {max_diff}")
