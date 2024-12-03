import os, sys, datetime

basedir = os.path.abspath(os.path.dirname(sys.argv[0]))
today = datetime.date.today()
year = today.year

yearpath = os.path.join(basedir, str(year))

os.makedirs(yearpath, exist_ok=True)

for d in range(1, 26):
  daydir = "{:02d}".format(d)
  daypath = os.path.join(yearpath, daydir)
  os.makedirs(daypath, exist_ok=True)

