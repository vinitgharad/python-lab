name = input("Vendor Name: ")
year = int(input("Year of association: "))
contact = input("Contact number: ")
email = input("Email ID: ")

total = 0

for i in range(12):
    purchase = float(input(f"Enter purchase for month {i+1}: "))
    total += purchase

print("Vendor:", name)
print("Annual Purchase:", total)