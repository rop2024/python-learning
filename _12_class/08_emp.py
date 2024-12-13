# this is copy or reference

class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    def yearly_bonus(self):
        # Default bonus (could be zero if no specific calculation for the role)
        return 0

    def __str__(self):
        return f"Employee: {self.name}, Position: {self.position}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary, position="Manager")

    def yearly_bonus(self):
        # Managers get a 35% bonus on annual salary
        return (self.salary * 12) * 0.35

    def __str__(self):
        return f"{super().__str__()}, Yearly Bonus: {self.yearly_bonus()}"


class Worker(Employee):
    def __init__(self, name, salary, position):
        super().__init__(name, salary, position)

    def yearly_bonus(self):
        # Workers get a different bonus rate based on position
        if self.position == "Clerk":
            return (self.salary * 12) * 0.25
        elif self.position == "Assistant":
            return (self.salary * 12) * 0.1
        else:
            return 0

    def __str__(self):
        return f"{super().__str__()}, Yearly Bonus: {self.yearly_bonus()}"


# Test with some sample employees
def main():
    # Create a manager
    manager = Manager(name="Alice", salary=5000)
    print(manager)

    # Create workers
    clerk = Worker(name="Bob", salary=3000, position="Clerk")
    assistant = Worker(name="Charlie", salary=2500, position="Assistant")

    print(clerk)
    print(assistant)


if __name__ == "__main__":
    main()
