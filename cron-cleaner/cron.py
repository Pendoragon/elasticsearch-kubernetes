import schedule
import time
import datetime
import optparse
import os
from subprocess import call

def job(cmd):
  print("[%s] Cleaning up old data for elasticsearch..." % datetime.datetime.now())
  call(cmd.split(" "))

def main():
  # The flags are mainly for testing purpose
  parser = optparse.OptionParser()
  parser.add_option('-t', '--time-unit', action="store", dest="time_unit", help="time unit", default="days")
  parser.add_option('-o', '--newer-than', action="store", dest="newer_than", help="retention length", default="7")
  parser.add_option('-s', '--schedule-unit', action="store", dest="schedule_unit", help="schedule unit", default="day")
  options, args = parser.parse_args()

  # Use env vars as parameters to launch cron jobs
  time_unit = os.getenv('CURATOR_TIME_UNIT', "days")
  newer_than = os.getenv('CURATOR_NEWER_THAN', "7")
  schedule_unit = os.getenv('SCHEDULE_UNIT', "day")

  cmd = "curator --host=localhost delete indices --newer-than %s --time-unit %s --timestring %%Y/%%m/%%d" % (newer_than, time_unit)
  crontab = "schedule.every().%s.do(job, cmd)" % schedule_unit

  eval(crontab)
  while 1:
    schedule.run_pending()
    time.sleep(1)

if __name__ == "__main__":
  main()
