import re
import nltk
from transformers import BertTokenizer

class TweetProcessor:
    def __init__(self):
        nltk.download('stopwords')
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.stopwords = set(nltk.corpus.stopwords.words('english'))

    def clean_tweet(self, tweet):
        tweet = re.sub(r'http\S+', '', tweet)
        tweet = re.sub(r'@\w+', '', tweet)
        tweet = re.sub(r'#', '', tweet)
        tweet = re.sub(r'\W', ' ', tweet)
        tweet = tweet.lower()
        return tweet

    def remove_stopwords(self, tweet):
        return ' '.join([word for word in tweet.split() if word not in self.stopwords])

    def tokenize(self, tweet):
        return self.tokenizer(tweet, padding='max_length', truncation=True, max_length=128, return_tensors="pt")

if __name__ == "__main__":
    processor = TweetProcessor()
    sample_tweet = "There’s been a massive earthquake in California! #earthquake #disaster"
    clean_tweet = processor.clean_tweet(sample_tweet)
    clean_tweet = processor.remove_stopwords(clean_tweet)
    tokenized_tweet = processor.tokenize(clean_tweet)
    print(tokenized_tweet)
