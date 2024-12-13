# Write a program to determine whether the seller has made profit or incurred loss. Also
# determine how much profit he made or loss he incurred. Cost price and selling price of an item is
# input by the user.

cost_price = int(input("Enter cost price: "))
selling_price = int(input("Enter selling price: "))

if selling_price <= cost_price:
    print(f"Loss of {cost_price - selling_price}")
else:
    print(f"Gain of {selling_price - cost_price}")
