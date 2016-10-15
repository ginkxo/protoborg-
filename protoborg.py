import tweepy, time
from sys import argv
import random as rd 

CONSUMER_KEY = "hidden"
CONSUMER_SECRET_KEY = "hidden"
ACCESS_KEY = "hidden"
ACCESS_SECRET_KEY = "hidden"
authenticator = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
authenticator.set_access_token(ACCESS_KEY,ACCESS_SECRET_KEY)
api = tweepy.API(authenticator)

symbols = [" <3 ", " !!! ", " ??? "]

def heart_generator(values):

	for i in range(values):

		string = ". . ."
		for i in range(10):
			index = rd.randint(0,2)
			string += symbols[index]

		print "printing . . ."
		print string
		api.update_status(string)
		print "printed."
		time.sleep(60)

script, freq = argv
heart_generator(int(freq))