import schedule
import time
import optparse

from subprocess import call

def job(cmd):
  print("Cleaning up old data for elasticsearch...")
  call(cmd.split(" "))

def main():
  parser = optparse.OptionParser()
  parser.add_option('-t', '--time-unit', action="store", dest="time_unit", help="time unit", default="days")
  parser.add_option('-o', '--older-than', action="store", dest="older_than", help="retention length", default="7")
  parser.add_option('-s', '--schedule-unit', action="store", dest="schedule_unit", help="schedule unit", default="day")
  options, args = parser.parse_args()

  print 'time_unit:', options.time_unit
  print 'older_than:', options.older_than

  cmd = "curator --host=localhost delete indices --newer-than %s --time-unit %s --timestring %%Y/%%m/%%d" % (options.older_than, options.time_unit)
  crontab = "schedule.every().%s.do(job, cmd)" % options.schedule_unit

  eval(crontab)
  while 1:
    schedule.run_pending()
    time.sleep(1)

if __name__ == "__main__":
  main()
