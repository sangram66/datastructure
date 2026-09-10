import sys
import datetime
 
for line in sys.stdin:
    line = line.strip()
    userid, unixtime = line.split('\t')
    weekday = datetime.datetime.fromtimestamp(float(unixtime)).isoweekday()
    print (','.join([userid, str(weekday)]))