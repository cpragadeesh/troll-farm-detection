from os import listdir
import csv

files = listdir("adjusted_tweets/")

cnt = 0

for f in files:

	with open("adjusted_tweets/" + f, "r") as fd:
		reader = csv.reader(fd)
		for line in reader:
			cnt += 1

print cnt

