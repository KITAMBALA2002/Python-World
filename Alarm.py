#!/usr/bin/env python3
import datetime

class Alarm:

    def __init__(self,hour,min):
        self.user_hour=hour
        self.user_min=min
    
    def curret_time(self):
        now=datetime.datetime.now()
        print(f'The current date is {now.strftime('%Y-%m-%d')}')
        print(f'The current time is {now.strftime('%H.%M')}')
        
    
    def check (self):
        now=datetime.datetime.now()
        #today_date=now.strftime('%Y-%m-%d')
        current_moment=now.strftime('%H%M')

        if self.user_hour and self.user_min == current_moment:
            print('Congratulations! you are doing great.')
        else:
            print('Not yet, try again later!')

obj=Alarm('06','13')
obj.curret_time()
obj.check()