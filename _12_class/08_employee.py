# Employee Payroll System:
# Create an Employee class with attributes like name, salary, and position.
# Add a method to calculate yearly bonuses.
# Create subclasses for Manager and Worker, with different bonus calculations.

class Employee:
    post_option = ['manager', 'clerk', 'assistant']

    def __init__(self, name, salary, position = None):
        self.name = name
        self.salary = salary
        if position is None:
            self.position = []

    def set_position(self):
        inp = input("Enter position: ").lower()
        if inp in Employee.post_option:
            self.post_option.append(inp)
            return
        print("Wrong choice")

    def yearly_bonus(self):
        if self.position == Employee.post_option[0]:
            return (self.salary * 12) * 0.35

        elif self.position == Employee.post_option[1]:
            return (self.salary * 12) * 0.25

        elif self.position == Employee.post_option[2]:
            return (self.salary * 12) * 0.1

        else:
            return 0




