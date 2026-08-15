import time
from plyer import notification
while True:
    notification.notify(
        title="Hydration Reminder",
        message="Please Sip some water to stay hydrated!",
        timeout=10
    )
    time.sleep(3600)  # Remind every hour
