# import the schedule and time from the python libraries
import schedule
import time
from datetime import datetime

def remind_to_check_phone():
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"Reminder: It's {current_time}! Time to check your phone to 1001albums.com on your laptop.")

# Schedule the reminder at 8:00 AM daily
schedule.every().day.at("08:00").do(remind_to_check_phone)

#schedule the reminder at 7:00 PM daily
schedule.every().day.at("19:00").do(remind_to_check_phone)

# Run the script continuously
while True:
    schedule.run_pending()
    time.sleep(1)
