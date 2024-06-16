# for mac and linux

# import os
# import time
#
# notification_title = input("Enter the title of the notification: ")
# notification_details = input("Enter the details of the notification: ")
# seconds_wait = int(input("Enter the seconds: "))
#
# time.sleep(seconds_wait)
#
# os.system(f'''
#     osascript -e 'display notification "{notification_details}" with title "{notification_title}"'
# ''')


# for windows

# import time
# from plyer import notification  # pip install plyer
#
# notification_title = input("Enter the title of the notification: ")
# notification_details = input("Enter the details of the notification: ")
# seconds_wait = int(input("Enter the seconds: "))
#
# time.sleep(seconds_wait)
#
# notification.notify(
#     title=notification_title,
#     message=notification_details,
# )

import time
import os
from plyer import notification  # pip install plyer
from sys import platform

notification_title = input("Enter the title of the notification: ")
notification_details = input("Enter the details of the notification: ")
seconds_wait = int(input("Enter the seconds: "))

time.sleep(seconds_wait)

if platform == "linux" or platform == "linux2" or platform == "darwin":
    os.system(f'''
        osascript -e 'display notification "{notification_details}" with title "{notification_title}"'
    ''')
elif platform == "win32":
    notification.notify(
        title=notification_title,
        message=notification_details,
    )