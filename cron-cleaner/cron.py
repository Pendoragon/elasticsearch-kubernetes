import schedule
import time
from subprocess import call

def job():
  print("Cleaning up old data for elasticsearch...")
  call(cmd.split(" "))

cmd = "curator --host=localhost delete indices --older-than 7 --time-unit days --timestring %Y/%m/%d"
schedule.every().week.do(job)

while 1:
  schedule.run_pending()
  time.sleep(1)
