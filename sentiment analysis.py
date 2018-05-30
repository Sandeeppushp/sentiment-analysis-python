# first install textblob from pip 

from textblob import TextBlob
text=input('Enter your Text: ')
wiki=TextBlob(text)
print(wiki.sentiment.polarity)
input()