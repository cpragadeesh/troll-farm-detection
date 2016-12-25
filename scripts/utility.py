from datetime import datetime, timedelta
from random import random, randint
import csv

from os import listdir
import csv

def get_next_time(start, offset_limit):
"""get next random time after start time and within the offset_limit"""

rand_offset = randint(0, offset_limit)
offset = timedelta(minutes=rand_offset)

return start + offset

def get_first_tweet_id():
	
	tweet_id = ""

	for c in bot_name:
		tweet_id = tweet_id + str(ord(c))

	tweet_id = tweet_id + "0000"
	tweet_id = int(tweet_id)

	return tweet_id

def get_next_tweet_id(tweet_id):
	
	return tweet_id + 1

def run():
	"""Generate 7-8 tweets/day for 5 days"""

	bot_name = raw_input("Enter name for the bot: ").strip()

	start_date = datetime(2016, 12, 19, 9, 0, 0)

	for day in range(5):
		time = get_next_time(start_date, 60)
		tweet_id = get_first_tweet_id()

		tweets = []

		tweets.append([tweet_id, time])

		for i in range(randint(7, 8)):
			time = get_next_time(time, 60)
			tweet_id = get_next_tweet_id(tweet_id)

			tweets.append([tweet_id, time])

		time = get_next_time(start_date + timedelta(hours=10), 60)
		tweet_id = get_next_tweet_id(tweet_id)

		tweets.append([tweet_id, time])

		start_date = start_date + timedelta(days=1)


	with open(bot_name + "_tweets.csv", "w") as f:
		writer = csv.writer(f)
		writer.writerows(tweets)

class Statistics:

def count_tweets():
	"""Count total number of tweets collected"""

	tweet_dir = "tweets_wc/"
	files = listdir(tweet_dir)

	cnt = 0

	for f in files:

		with open(tweet_dir + f, "r") as fd:
			reader = csv.reader(fd)
			for line in reader:
				cnt += 1

	print cnt

def count_distinct_users():

	def find_union(file1, file2):

		user_list = []

		with open(file1) as f1, open(file2) as f2:
			
			for line in f1:
				user = line.strip()
				if user not in user_list:
					user_list.append(user)

			for line in f2:
				user = line.strip()
				if user not in user_list:
					user_list.append(user)

	return user_list


	users = find_union("users_list_1.txt", "users_list_1.txt")

	print len(users)





