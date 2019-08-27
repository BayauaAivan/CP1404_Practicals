
total = 0

numberofitems = int(input("Number of items: "))
while numberofitems < 0:
    print("ERROR: Please enter a positive interger")
    numberofitems = int(input("Number of items: "))
for a in range(numberofitems):
    price = float(input("Price of item: $"))
    total += price

if total > 100:
    total = total * 0.9

print("Total price for your", numberofitems, " items is $", total, sep='')