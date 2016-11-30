import tweepy
import csv
import json
import pprint
import ast

consumer_key = 'AIGcAOnQiY3QPgnamk9xlRhDX'
consumer_secret = 'AJaIp14KuWXP8DueZiNrNq26NXmswKujF5x3CIlYQT6PUR3Js6'
access_key = '331675167-k7GLK5MiN8stcp5Q17svquAkMq9Ui4HbcwP5nC7K'
access_secret = 'UD1yQ3MLzSu6MbBSO7no9zLNECBXyN5AObB05mrQwlmBR'

if __name__ == '__main__':
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	user_list = []

	while(len(user_list) < 100):
		res = api.search(q='#trump', rpp=99)
			
		#pp = pprint.PrettyPrinter(indent=4)
		#pp.pprint(res._json.user.screen_name)

		for r in res:
			if r._json['user']['screen_name'] not in user_list:
				user_list.append(r._json['user']['screen_name'])

	print user_list
	print "Collected: " + str(len(user_list)) + " users"	

#res = [u'Morseileen', u'Bull_Spotter', u'ManMet80', u'colmant_', u'JimPolk', u'dawntaylor78', u'Jijocfran', u'kennedy_tamara', u'axelmojave', u'enunn7', u'RitchiePrice', u'shootawolfe', u'Watkinsmfg', u'kathy_platan', u'Gia84', u'05665lkta', u'06723jcsb', u'CorkysWorld', u'hosf32334', u'02472gnlc', u'dist32940', u'stwa29166', u'pelias01', u'dmfa26103', u'slhf29127', u'82929slhb', u'02110gnlb', u'wilsonvince1', u'slhd28581', u'83705slhd', u'lemondefr', u'Tanya_USA', u'Ebvann', u'citizen_0000', u'flysNort', u'actu_foot_360', u'seabee0', u'PsyOpMilitant', u'dmfa26224', u'jasp32052', u'Sandbagger59', u'01902gnlb', u'08011gnla', u'CFNLgtbt', u'rusticrobin', u'MiketteHP', u'CalvinSwine905', u'GloomandDoom1', u'2717PRODUCTIONS', u'glockarmor25', u'mesanabinladen', u'twenty48dotnet', u'wldrvrsrrn', u'shahin_gourgi', u'AmericanV_2017', u'pennsylbama2705', u'nancy_tobi', u'twnklsdad', u'RealFKNNews', u'urdu_khabarnama', u'KMCaton', u'2L84you2C', u'10thAmendment', u'RossCervellera', u'toddhenry1971', u'1maryalice', u'gilbuly', u'BLRidgell', u'von_Steiner', u'22norsedad', u'eiramartens', u'Daily_Express', u'webcrawlerw', u'dkoceanside', u'rupigo', u'SteveSteinbach', u'MicheWrites', u'Owl_131', u'RochdaleHerald', u'Hispantv', u'rodsandguitars', u'BorthwickKathy', u'IvanMiljojkovic', u'KimJongUnique', u'geopoliting', u'jimdwrench', u'manzanog00', u'DebbieJones46', u'Hashtag1USA', u'genderscheisse', u'cathyken3', u'klabrakakis', u'tunetribe', u'CustosDivini', u'F3nws', u'RaWwDance560', u'bspence5', u'HassanAltarazi', u'MariaWiesz', u'Tmagadla_yesco', u'Jorhendrik', u'FToaquizaEcuavi', u'FarizzleBizzle', u'shimonshan']