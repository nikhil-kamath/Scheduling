from time import sleep
from .DateCreator import DateCreator
from .TimeCreator import TimeCreator
import datetime
import threading

def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper

class Scheduler:
    '''class that schedules methods to run at a certain time'''
    def __init__(self, precision: float = 1) -> None:
        '''constructor'''
        self.precision = precision
        self.time_creator = TimeCreator()
        self.date_creator = DateCreator()
        self.scheduled_events = 0
    
    def get_precision(self):
        '''return the precision of the time check'''
        return self.precision
    
    def set_precision(self, precision: float):
        '''change the precision of the time check'''
        self.precision = precision

    @threaded
    def schedule(self, to_run, scheduled_time: datetime.time, scheduled_date:datetime.date, *args, **kwargs):
        '''creates a new thread that checks the current time every precision seconds'''
        self.scheduled_events += 1
        while True:
            if self.time_creator.check_time(scheduled_time) and self.date_creator.check_date(scheduled_date):
                to_run(*args, **kwargs)
                self.scheduled_events -= 1
                return
            sleep(self.precision)

    def is_finished(self):
        '''returns true if no tasks are scheduled'''
        return self.scheduled_events == 0

        