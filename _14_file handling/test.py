import datetime

class Task:
    status = ["NS", "IP","DO"] # not started - in progress - done
    total_task = 0

    def __init__(self, task, do_date, status="NS", created_date = datetime.date.today()):
        self.task = task
        self.status = status
        self.created_date = created_date
        self.do_date = do_date
        self.days = (self.do_date - self.created_date)
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


def main():
    trial = Task("Do something xyz", datetime.date(2024, 12, 10))
    print(trial.days_left())

if __name__ == "__main__":
    main()