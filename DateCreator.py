import time
import datetime

class DateCreator:
    '''object to manage current dates and check if times are equal to current date'''

    def __init__(self):
        '''constructor'''
        self.date = datetime.date.today()

    def update(self):
        '''updates instance date every time another method is called'''
        self.date = datetime.date.today()

    def get_date(self):
        '''returns current date'''
        self.update()
        return self.date

    def check_date(self, to_check: datetime.time):
        '''checks if a date is equal to or beyond current date with minute precision'''
        self.update()
        return to_check <= self.date
