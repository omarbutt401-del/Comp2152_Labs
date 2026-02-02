# Q 1
grades = [85, 92, 78, 95, 88]

grades.append(90)

grades.sort()

print("Sorted grades:", grades)
print("Highest grade:", grades[-1])
print("Lowest grade:", grades[0])
print("Total number of grades:", len(grades))

# Q 2
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]

# Count apples
print("Number of apples:", cart.count("apple"))

# Index of milk
print("Position of milk:", cart.index("milk"))

# Remove one apple
cart.remove("apple")

# Pop last item
removed = cart.pop()
print("Removed item using pop:", removed)

# Check membership
print("Is banana in cart?", "banana" in cart)

# Final cart
print("Final cart:", cart)

# Q 3
point1 = (3, 5)
point2 = (7, 2)

x1, y1 = point1
x2, y2 = point2

distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

chars = tuple("PYTHON")

print("Point 1:", point1)
print("Point 2:", point2)
print(f"x1 = {x1}, y1 = {y1}")
print(f"x2 = {x2}, y2 = {y2}")
print("Distance between points:", distance)
print("Characters tuple:", chars)

for c in chars:
    print(c)

# Q 4
monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}

monday_class.add("Grace")

both = monday_class & wednesday_class
either = monday_class | wednesday_class
only_monday = monday_class - wednesday_class
only_one = monday_class ^ wednesday_class
subset_check = monday_class <= either

print("Monday class:", monday_class)
print("Wednesday class:", wednesday_class)
print("Attended both classes:", both)
print("Attended either class:", either)
print("Only Monday:", only_monday)
print("Only one class (not both):", only_one)
print("Is Monday subset of all students?", subset_check)

# Q 5
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}

print("Alice's number:", contacts["Alice"])

contacts["Diana"] = "555-4321"
print("Contacts after adding Diana:", contacts)

contacts["Bob"] = "555-0000"
print("Contacts after updating Bob:", contacts)

del contacts["Charlie"]
print("Contacts after deleting Charlie:", contacts)

print("All names:", contacts.keys())
print("All numbers:", contacts.values())
print("Total contacts:", len(contacts))

# Q 6
inventory = {
    "Laptop": (999.99, 5),
    "Mouse": (29.99, 15),
    "Keyboard": (79.99, 10),
    "Monitor": (299.99, 8)
}

print("=== Current Inventory ===")
for product, (price, qty) in inventory.items():
    print(f"{product} - Price: ${price}, Quantity: {qty}")

electronics = {"Laptop", "Monitor"}
accessories = {"Mouse", "Keyboard"}

all_products = electronics | accessories
print("\nAll product categories:", all_products)

prices = [price for price, qty in inventory.values()]
print("\nPrice list:", prices)

prices.sort()
print("Sorted prices:", prices)
print("Lowest price: $", prices[0])
print("Highest price: $", prices[-1])

inventory["Headphones"] = (49.99, 20)

price_mouse, _ = inventory["Mouse"]
inventory["Mouse"] = (price_mouse, 12)

del inventory["Monitor"]

print("\n=== Final Inventory ===")
for product, (price, qty) in inventory.items():
    print(f"{product} - Price: ${price}, Quantity: {qty}")