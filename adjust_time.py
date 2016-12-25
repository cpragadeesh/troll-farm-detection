from datetime import datetime, timedelta
from os import listdir
import csv

def dummy():
	str_time = "2016-12-23 16:26:55"
	offset = timedelta(seconds=2.5*3600)

	d = datetime.strptime(str_time, "%Y-%m-%d %H:%M:%S")

	print d

	d = d - offset;

	print d

def adjust_tz(time, offset):

	offset = timedelta(seconds=offset*3600)

	d = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")

	d = d + offset

	return str(d)

tz_data = {}

if __name__ == "__main__":

	with open("user_tz_data.csv") as tzf:
		reader = csv.reader(tzf)

		for line in reader:
			tz_data[line[0]] = float(line[1])

	files = listdir('tweets_wc/')

	for tfile in files:
		if tfile[0] == '.':
			continue

		with open("tweets_wc/" + tfile) as f, open("adjusted_tweets/" + tfile, "w") as f2:
			name = tfile[:tfile.find('_tweets.csv')]
			reader = csv.reader(f)
			new_data = []
			print "Working on: " + name

			cnt = 0

			for line in reader:
				if cnt == 0:
					cnt += 1
					continue

				time = line[1].strip()
				line[1] = adjust_tz(time, tz_data[name])
				new_data.append([line[0], line[1]])

			writer = csv.writer(f2)
			writer.writerows(new_data)
