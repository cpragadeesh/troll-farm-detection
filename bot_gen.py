from datetime import datetime, timedelta
from random import random, randint
import csv

bot_name = raw_input("Enter name for the bot: ").strip()

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

if __name__ == "__main__":
	
	"""Generate 7-8 tweets/day for 5 days"""

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







