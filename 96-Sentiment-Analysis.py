from textblob import TextBlob

# Function to analyze sentiment
def sentiment_analysis(text):
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

while True:
    text = input("enter Your text : ")
    if "stop" in text.lower():
        break
    print(sentiment_analysis(text))
