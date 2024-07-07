#!/usr/bin/env python3
import re
import psutil
from plyer import notification

def notify_me():
    notification.notify(
        title='Charging Status',
        message='Battery is not charging',
        app_name='Clocks'
    )

def notify_user():
    battery = psutil.sensors_battery()
    per=str(battery.percent)
    find=re.findall(r'\d+',per)
    power=find[0]+'%'

    notification.notify(
        title='Battery percentage',
        message=f'{power}, Battery below average, please charge!!',
        app_name='Clocks'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    )

battery = psutil.sensors_battery()
per=str(battery.percent)
find=re.findall(r'\d+',per)

power=find[0]

if battery.power_plugged == False and int(power) <50:
    notify_user()

elif battery.power_plugged == False and int(power) >50:
    notify_me()
    