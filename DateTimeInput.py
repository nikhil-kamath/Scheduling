import datetime as dt

class DateTimeInput:
    def __init__(self):
        pass

    def input_date(self) -> dt.date:
        '''gets input from console and returns DATE object'''
        goal_date_str = input("Enter a date at which our code should run: ").split()
        if goal_date_str[0] == 'today':
            return dt.date.today()
        goal_date_data = [int(a) for a in goal_date_str]
        goal_date: dt.date

        while True:
            try:
                if goal_date_str == 'today':
                    goal_date = dt.date.today()
                    break
                goal_date = dt.date(*goal_date_data)
                break
            except ValueError:
                print("invalid date")
                goal_date_str = input(
                    "Enter a date at which our code should run: ").split()
                goal_date_data = [int(a) for a in goal_date_str]
        
        return goal_date

    def input_time(self) -> dt.time:
        '''gets input from console and returns TIME object'''
        goal_time_str = input("Enter a time at which our code should run: ").split()
        if goal_time_str[0] == 'now':
            return dt.datetime.now().time()
        goal_time_data = [int(a) for a in goal_time_str]
        goal_time: dt.time

        while True:
            try:
                goal_time = dt.time(*goal_time_data)
                break
            except ValueError:
                print("invalid time")
                goal_time_str = input(
                    "Enter a time at which our code should run: ").split()
                goal_time_data = [int(a) for a in goal_time_str]
        
        return goal_time
