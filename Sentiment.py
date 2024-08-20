import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Create a SentimentIntensityAnalyzer object
sia = SentimentIntensityAnalyzer()

# Ask the user to enter the text
text = input("Enter the text: ")

# Analyze the sentiment
sentiment_scores = sia.polarity_scores(text)

# Print the sentiment scores
print(sentiment_scores)

# Print the sentiment category
if sentiment_scores['compound'] >= 0.05:
    print("Positive")
elif sentiment_scores['compound'] <= -0.05:
    print("Negative")
else:
    print("Neutral")

