import tweepy
import csv

consumer_key = 'AIGcAOnQiY3QPgnamk9xlRhDX'
consumer_secret = 'AJaIp14KuWXP8DueZiNrNq26NXmswKujF5x3CIlYQT6PUR3Js6'
access_key = '331675167-k7GLK5MiN8stcp5Q17svquAkMq9Ui4HbcwP5nC7K'
access_secret = 'UD1yQ3MLzSu6MbBSO7no9zLNECBXyN5AObB05mrQwlmBR'

time_zones = {}

tz_rawoffset = {
    'Karachi': 5.0,
    'Arizona': -7.0,
    'Eastern Time (US & Canada)': -5.0,
    'Quito': -5.0,
    'None': -5.0,
    'Brisbane': 10.0,
    'Hawaii': -10.0,
    'Atlantic Time (Canada)': -3.5,
    'Athens': 2,
    'Alaska': -9,
    'Pacific Time (US & Canada)': -8,
    'America/Los_Angeles': -8,
    'Paris': 1,
    'Mid-Atlantic': -4,
    'London': 0,
    'Mountain Time (US & Canada)': -6,
    'Sri Jayawardenepura': +5.5,
    'America/New_York': -5,
    'Central Time (US & Canada)': -6,
    'Brussels': 1
}

not_found = []

def get_geo(screen_name):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    tweet = api.user_timeline(screen_name = screen_name,count=1)[0]

    if tweet.user.time_zone == None:
        not_found.append(screen_name)
        return

    if tweet.user.time_zone.encode('UTF-8') not in tz_rawoffset:
        print "ERRRRRORORRROROROROROROROROROROROOROROROROROROROROROROR"
        return

    return tz_rawoffset[tweet.user.time_zone.encode('UTF-8')]

if __name__ == "__main__":
    
    with open("user_tz_data.csv", "w") as tz_f:
        writer = csv.writer(tz_f)

        with open("done_list.txt") as f:
            for name in f:
                print "User: " + name
                name = name.strip()
                tz = get_geo(name)

                writer.writerow([name, str(tz)])

        print not_found
