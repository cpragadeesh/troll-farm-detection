import tweepy
import csv

consumer_key = 'AIGcAOnQiY3QPgnamk9xlRhDX'
consumer_secret = 'AJaIp14KuWXP8DueZiNrNq26NXmswKujF5x3CIlYQT6PUR3Js6'
access_key = '331675167-k7GLK5MiN8stcp5Q17svquAkMq9Ui4HbcwP5nC7K'
access_secret = 'UD1yQ3MLzSu6MbBSO7no9zLNECBXyN5AObB05mrQwlmBR'

def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method

	print "Collecting from user: " + screen_name
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#initialize a list to hold all the tweepy Tweets
	alltweets = []

	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)

	#save most recent tweets
	alltweets.extend(new_tweets)

	if len(alltweets) == 0:
		return 

	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1

	#keep grabbing tweets until there are no tweets left to grab

	prev_len = len(alltweets)

	while len(alltweets) < 150:
		print "Collected so far: " + str(len(alltweets))
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

		#save most recent tweets
		alltweets.extend(new_tweets)

		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1

		if len(alltweets) == prev_len:
			break

		prev_len = len(alltweets)

	#transform the tweepy tweets into a 2D array that will populate the csv
	outtweets = [[tweet.id_str, tweet.created_at] for tweet in alltweets]

	#write the csv
	with open('./tweets/%s_tweets.csv' % screen_name, 'w+') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)


if __name__ == '__main__':
	with open("users_list_1.txt") as f:
		for name in f:
			name = name.strip()
			get_all_tweets(name)
