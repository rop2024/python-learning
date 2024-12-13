# input tasks, mark done
import datetime, json

class Task:
    status = ["NS", "IP","DO"] # not started - in progress - done
    total_task = 0

    def __init__(self, task, do_date, status="NS", created_date = datetime.date.today()):
        self.task = task
        self.status = status
        self.created_date = created_date
        self.do_date = do_date
        self.days = self.do_date - self.created_date
        Task.total_task += 1

    def toggle_status(self, command):
        command = command.lower()

        if command in ['in progress', 'inp', 'in']:
            self.status = Task.status[1]
        elif command in ['not started', 'ns', 'not']:
            self.status = Task.status[0]
        elif command in ['done', 'do']:
            self.status = Task.status[2]
        else:
            self.status = 'XX'

    def days_left(self):
        return self.days

class TaskManager:

    def __init__(self):
        self.tasks = []

    def task_add(self, task, do_date):
        new = Task(task,do_date)
        self.tasks.append(new)

    def list_task(self):
        print("Tasks to do - ")
        i = 1
        for task in self.tasks:
            if task.status in ['NS','IP']:
                print(f"{i}. {task.task}")
                i += 1

    def toggle(self):
        i = 1
        dict = {}
        for tasky in self.tasks:
            dict[i] = tasky.task
            i += 1

        print(dict)

        select = int(input("Select task index to toggle : "))
        status = input("ns-ip-do ??")

        for task in self.tasks:
            if task.task == dict[select]:
                task.toggle_status(status)

    def tasks_list_done(self):
        print("Tasks done - ")
        i = 1
        for task in self.tasks:
            if task.status in ['DO']:
                print(f"{i}. {task.task}")
                i += 1

    def remove(self):
        i = 1
        dict = {}
        for tasky in self.tasks:
            dict[i] = tasky.task
            i += 1

        print(dict)

        select = int(input("Select task index you want to delete : "))

        for task in self.tasks:
            if task.task == dict[select]:
                self.tasks.remove(task)


    def backup(self):
        task_dict = [task.__dict__ for task in self.tasks]
        file = open("taskAll.json", "w")
        json.dump(task_dict,file,default=str, indent = 4)
        file.close()

        print("Backup was successful !!")

    def load(self):
        file = open("taskAll.json", "r")
        content = file.read()
        cleandata = json.loads(content)
        self.task = []

        for task_data in cleandata:
            task = Task(
                task=task_data["task"],
                do_date=datetime.date.fromisoformat(task_data["do_date"]),
                status=task_data["status"],
                created_date=datetime.date.fromisoformat(task_data["created_date"])
            )

            self.tasks.append(task)

        file.close()
        print("Tasks loaded successfully !!")

def main():
    taskmanager()

def taskmanager():
    taskmanager = TaskManager()
    while True:
        ch = choice()

        if ch == 0:
            break
        elif ch == 1:
            task = input("Enter task: ")
            date = int(input("Enter date to do :"))
            month = int(input("Enter month to do :"))
            year = int(input("Enter year to do:"))
            taskmanager.task_add(task,datetime.date(year,month,date))

            print("Task added successfully !!")
        elif ch == 2:
            print("List of task --")
            taskmanager.list_task()
            print("-----")

        elif ch == 3:
            print("List of task done -- ")
            taskmanager.tasks_list_done()
            print("-----")

        elif ch == 4:
            print("Changing status of task --")
            taskmanager.toggle()
            print("-----")

        elif ch == 5:
            print("Removing task ")
            taskmanager.remove()

        elif ch == 6:
            print("Backup ")
            taskmanager.backup()

        elif ch == 7:
            print("Load from file")
            taskmanager.load()

        else:
            print("Wrong choice !!")

def choice():
    print("-----")
    print("[1] Add task")
    print("[2] List to do list")
    print("[3] List done tasks")
    print("[4] Toggle status")
    print("[5] Remove task")
    print("[6] Backup")
    print("[7] Load from txt file")
    print("[0] Exit")
    print("-----")
    return int(input("Enter choice: "))


if __name__ == "__main__":
    main()