import time
from datetime import datetime
from plyer import notification
import winsound

def set_alarm(hour, minute) :
    # Get the current time
    now = datetime.now()
    alarm_time = datetime (now.year, now.month, now.day, hour, minute)

    # Calculate the time difference until the alarm
    time_difference = alarm_time - now

    # Wait until the alarm time
    time.sleep(time_difference.total_seconds())

    # When the alarm time is reached, trigger the notification and play a sound
    notification.notify(
        title='Alarm',
        message='Wake up!',
        app_icon=None,
        timeout=10,
    )
    # Play a sound
    winsound.Beep(1000, 1000)
# Beep at 1000 Hz for 1 second

set_alarm (13, 17)