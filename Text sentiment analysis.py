from textblob import TextBlob 
from newspaper import Article 
import nltk

# Download the necessary NLTK tokenizer
nltk.download('punkt')
nltk.download('punkt_tab')  # Attempt to download punkt_tab if available

# URL of the article to be processed
url = "https://en.wikipedia.org/wiki/Option_(finance)"
article = Article(url)

# Downloading and parsing the article
article.download()
article.parse()
article.nlp()

# Extracting the text from the article
text = article.text

# Printing the extracted text
print(text)

# Printing the sentiment of the text
blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)