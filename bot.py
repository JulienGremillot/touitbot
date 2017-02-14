import tweepy
import time

from config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#api.update_status(status="Bonjour ! Grosse journee aujourd'hui !")

last_id = -1;
while 1:
	twt = api.search(q=query,since_id=str(last_id),show_user=1)
	for st in twt:
		if (not st.text.startswith("RT")) : 
			print(st.text)
		last_id = st.id
		
	print("last_id=" + str(last_id))
	time.sleep( 180 );

