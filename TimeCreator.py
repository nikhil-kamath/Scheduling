import time
import datetime 

class TimeCreator:
    '''object to manage current times and check if times are equal to current time'''
    def __init__(self):
        '''constructor'''
        self.time = datetime.datetime.now().time()
    
    def update(self):
        '''updates instance time every time another method is called'''
        self.time = datetime.datetime.now().time()
    
    def get_time(self):
        '''returns current time'''
        self.update()
        return self.time

    def check_time(self, to_check: datetime.time):
        '''checks if a time is equal to or beyond current time with minute precision'''
        self.update()
        return to_check <= self.time


