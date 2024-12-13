# Online Shopping Cart:
# Design classes for Product and ShoppingCart.
# The Product class should have attributes for name, price, and quantity.
# The ShoppingCart class should have methods to add or remove products,
# calculate the total cost, and display all items in the cart.

class Product:

    def __init__(self, name = "", price = 0, quantity = 1):
        self.name = name
        self.price = price
        self.quantity = quantity

    # unique value setter
    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def set_quantity(self, quantity):
        self.quantity = quantity


class ShoppingCart:


    def __init__(self):
        self.cart = []

    def display_list(self):
        print("| Name | Price | Quantity |")
        print("-----")
        for items in self.cart:
            print(f"| {items.name} | {items.price} | {items.quantity} |")

        print("-----")

    def add_item(self):
        name = input("Enter name of items: ")
        price = int(input("Enter price : "))
        quantity = int(input("Enter quantity: "))

        self.cart.append(Product(name, price, quantity))
        return

    def remove_items(self):
        name = input("Enter the name of the item you want to remove : ")
        for item in self.cart:
            if item.name == name:
                self.cart.remove(item)
                return

        print("No such item in cart")


    def display_total(self):
        bill = 0

        for item in self.cart:
            bill += (item.price * item.quantity)

        print(f"Total price : {bill}")


def main():
    cart = ShoppingCart()

    while True:
        print("-----")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. Display the total")
        print("4. Display the list")
        print("5. Exit")
        print("-----")

        choice = int(input("Enter choice: "))
        if 1 >= choice >=5:
            print("Wrong choice")
            break

        elif choice == 1:
            cart.add_item()

        elif choice == 2:
            cart.remove_items()

        elif choice == 3:
            cart.display_total()

        elif choice == 4:
            cart.display_list()

        elif choice == 5:
            break


if __name__ == "__main__":
    main()



