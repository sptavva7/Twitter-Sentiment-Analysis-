import csv
import random
import re
import codecs #provides transparent encoding/decoding

from textblob import TextBlob #Library for Text Processing
import time
from collections import Counter

#Importing libraries for plotting dependencies
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

#Initalisation of sentiment values
positive=0
negative=0
neutral=0
total=0
hashtags = []

#Processing..
print("Performing Sentiment Analysis",end="")
for i in range(5):
 print(".",end="")
 time.sleep(1)

#Reading obtained csv file
filepath='D:/vivek/Documents/VIT/PROJECTS/CSE3021/Tweepy/world_final.csv'
with codecs.open(filepath, "r",encoding='utf-8', errors='ignore') as csvfile:
reader = csv.reader(csvfile)
tweetsList=[]
cleanTweetsList=[]
for row in reader:
	tweet=row[1].strip() #contains tweet
	cleanTweet=" ".join(re.findall("[a-zA-Z]+",tweet))
	analysis=TextBlob(cleanTweet)
	
	#Appends the tweet to list
	tweetsList.append(tweet)
	cleanTweetsList.append(cleanTweet)
	
	#Assigns polarity and calculates count
	total=total+1
	if(analysis.sentiment.polarity>0):
		positive=positive+1
	if(analysis.sentiment.polarity==0):
		neutral=neutral+1
	else:
		negative=negative+1

#To display output
print() #newline
print("Total Tweets: ",total)
print('Positive = ',positive)
print('Neutral= ',neutral)
print('Negative= ',negative)

#Random number generator that aids in picking tweets
randomTweets=[]
randomCleanTweets=[]
randomNumber=random.sample(range(1, 10), 5)
index=0

#Collection of random tweets
for i in range(5):
	number=random.randint(1,10) #Picks a random number between 1-10
	randomTweets.append(tweetsList[randomNumber[index]]) #Stores a random tweet from data without repetitions
	randomCleanTweets.append(tweetsList[randomNumber[index]])
	index=index+1

for tweet in randomCleanTweets:
	print()
	print(tweet,end=' ')
	analysis=TextBlob(tweet)
	print(" => ",analysis.sentiment)

#Write the random tweets to a text file in order to display
with open('tweets.txt', 'w') as file:
	for tweet in randomTweets:
		file.write(tweet)
		file.write('<br><br>\n')

#Finds the hashtags in all the tweets
finalcount={}
for i in tweetsList:
	hashtags.append(re.findall(r"#(\w+)", i))
hashtagnew = [item for sub in hashtags for item in sub]
counts = Counter(hashtagnew)
counts = dict(counts)
finalcount = dict(sorted(counts.items(), key=lambda kv: kv[1], reverse=True))
countname = list(finalcount.keys())

#Plotting data

#Bar Graph
objects = ('Positive','Neutral','Negative')
y_pos = np.arange(len(objects))
performance = [positive,neutral,negative]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('# of tweets')
plt.show()

#Pie Graph
colors = ['yellowgreen', 'gold', 'orangered']
explode = (0, 0, 0.1) # explode last slice

plt.pie(performance, explode=explode, labels=objects, colors=colors,
 autopct='%1.1f%%', shadow=False, startangle=140)

plt.axis('equal')
plt.show()

# Hashtag Plot
x = np.arange(len(finalcount))
y = list(finalcount.values())
x = x[:15]
y = y[:15]
countname = countname[:15]
plt.bar(x, y)
plt.title('Most Trending Hashtags\n')
plt.xticks(x, countname, rotation='vertical')
plt.ylabel('Number of tweets')
plt.xlabel('#Hashtags')
plt.tight_layout()
plt.show()
