from textblob import TextBlob

message = input('type you message')

emotions = TextBlob(message)

sentiment = emotions.sentiment.polarity

if sentiment<0:
    print("😔sorry to hear that things will get good soon")
elif sentiment>0:
    print("😎😍 good to hear that")
else:
    print("ok see you soon")