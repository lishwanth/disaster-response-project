from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

class TopicModeler:
    def __init__(self, n_topics=5):
        self.n_topics = n_topics
        self.vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
        self.lda = LatentDirichletAllocation(n_components=self.n_topics, random_state=42)

    def fit_transform(self, tweets):
        tweet_matrix = self.vectorizer.fit_transform(tweets)
        self.lda.fit(tweet_matrix)
        return self.lda.transform(tweet_matrix)

    def print_top_words(self, n_top_words=10):
        feature_names = self.vectorizer.get_feature_names_out()
        for topic_idx, topic in enumerate(self.lda.components_):
            print(f"Topic #{topic_idx}:")
            print(" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))
        print()

if __name__ == "__main__":
    tweets = [
        "Earthquake hits California!",
        "Floods in Venice have reached alarming levels.",
        "Hurricane causes massive damage in Florida.",
        "Wildfire spreading quickly in Australia.",
        "Tornado warnings issued in Texas."
    ]
    modeler = TopicModeler(n_topics=3)
    modeler.fit_transform(tweets)
    modeler.print_top_words()
