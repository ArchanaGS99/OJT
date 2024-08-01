# textblob library
# let import textBlob over here in the app

# create a sample text

from textblob import TextBlob

text = [
    "I love NLP it's works greate and I'm ver satisfied",
    "This my first experince on doing sentiment analysis, I am littile bir disappointing",
    "The NLP sentiment anaylysis is quiet interseting it is neither good or bad",
]

# create function to do the sentiment analysis

def analyze_sentiment(text):
    analysis = TextBlob(text)
    # -1.0 to 1.0 polarity score
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment

for text  in text:
    sentiment = analyze_sentiment(text)
    print(f"Text : {text}")
    print(f"Sentiment : {sentiment}\n")





    