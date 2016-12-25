import numpy
import csv
from datetime import datetime, timedelta
from os import listdir

tweets_dir = "../tweets_working_copy/"
dataset_dir = "../dataset/"

def compute_avg_time(time_list):
	"""Compute relative average time in seconds. Ignores day, month, year"""

	seconds = []

	for time in time_list:
		start = datetime(time.year, time.month, time.day, 0, 0, 0)

		delta = time - start

		sec = delta.total_seconds()
		seconds.append(sec)

	return numpy.mean(seconds)

def create_datapoint(file_name):
	"""Returns datapoint as a list. 
		Datapoint: 
			[avg_start_time,
			avg_end_time,
		    avg_count,
			sd_count,
			avg_day_length,
			sd_day_length]"""

	start_times = []
	end_times = []
	counts = []
	day_lens = []

	with open(file_name, "r") as f:

		reader = csv.reader(f)

		day = []

		for line in reader:

			dt = datetime.strptime(line[1], "%Y-%m-%d %H:%M:%S")

			if len(day) == 0:
				day.append(dt)
				continue

			if day[-1].day == dt.day:
				day.append(dt)

			else:
				start_times.append(day[-1])
				end_times.append(day[0])
				day_lens.append(day[0] - day[-1])
				counts.append(len(day))

				day = [dt]

		start_times.append(day[-1])
		end_times.append(day[0])
		day_lens.append(day[0] - day[-1])
		counts.append(len(day))

	# print start_times
	# print end_times
	# print counts
	# print day_lens

	day_lengths = []

	for day in day_lens:
		day_lengths.append(day.total_seconds())
	
	avg_start_time = compute_avg_time(start_times)
	avg_end_time = compute_avg_time(end_times)

	avg_count = numpy.mean(counts)
	sd_count = numpy.std(counts)

	avg_day_length = numpy.mean(day_lengths)
	sd_day_length = numpy.std(day_lengths)

	datapoint = [avg_start_time, avg_end_time, avg_count, sd_count, avg_day_length, sd_day_length]

	print datapoint

	return datapoint

if __name__ == "__main__":

	file_list = listdir(tweets_dir)

	dfile = open(dataset_dir + "dataset.csv", "w")
	writer = csv.writer(dfile)

	for f in file_list:

		if f[0] == ".":
			continue

		d_pt = create_datapoint(tweets_dir + f)

		name = f[ :f.find('_tweets.csv')]

		writer.writerow([name] + d_pt)

