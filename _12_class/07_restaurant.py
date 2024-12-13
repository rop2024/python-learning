# Restaurant Menu:
# Develop a Dish class with attributes like name, price, and dietary type (e.g., vegetarian, non-vegetarian).
# Then, create a Menu class that stores multiple Dish objects and
# allows users to filter dishes by dietary type or price range.

class Dish:
    def __init__(self, name, price, dietary=None):
        if dietary is None:
            dietary = []

        self.name = name
        self.price = price
        self.dietary = dietary

    def set_dietary(self):
        options = ['vegetarian', 'non-vegetarian']

        print("Options - ")
        i = 0
        for item in options:
            print(f"{i}. {item}")
            i += 1

        print("-----")
        choice = int(input("Enter choice: "))
        self.dietary.append(options[choice])
        return

class Menu:
    def __init__(self):
        self.menu = []

    def add_dish(self):
        name = input("Name: ")
        price = int(input("Price: "))

        dish = Dish(name, price)
        dish.set_dietary()

        self.menu.append(dish)
        return

    def remove_dish(self):
        name = input("Name: ")

        for dish in self.menu:
            if dish.name == name:
                self.menu.remove(dish)
                print("Dish removed")
                return

        print("No such dish found")
        

    def filter_dish(self):
        # ask for range price
        lower = int(input("Lower limit: "))
        upper = int(input("Upper limit: "))
        # print all the lists that satisfy the dietary price and range of price
        # later....

        print("Items - ")
        print("| Name | Price | Dietary Preference |")
        for item in self.menu:
            if lower <= item.price <= upper:
                print(f"| {item.name} | {item.price} | {item.dietary} |")

        print("-----")


    def list_dish(self):
        print("Items - ")
        print("| Name | Price | Dietary Preference |")
        for item in self.menu:
            print(f"| {item.name} | {item.price} | {item.dietary} |")
        print("-----")


def main():
    cart = Menu()

    while True:
        print("-----")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. List Dish")
        print("4. Filter dishes")
        print("5. Exit")
        print("-----")

        choice = int(input("Enter choice: "))
        if 1 >= choice >=5:
            print("Wrong choice")
            break

        elif choice == 1:
            cart.add_dish()

        elif choice == 2:
            cart.remove_dish()

        elif choice == 3:
            cart.list_dish()

        elif choice == 4:
            cart.filter_dish()

        elif choice == 5:
            break



if __name__ == "__main__":
    main()