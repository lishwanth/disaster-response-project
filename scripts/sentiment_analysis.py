import torch
from transformers import BertForSequenceClassification

class SentimentAnalyzer:
    def __init__(self, model_path):
        self.model = BertForSequenceClassification.from_pretrained(model_path)

    def predict_sentiment(self, tokenized_input):
        with torch.no_grad():
            outputs = self.model(**tokenized_input)
            predictions = torch.argmax(outputs.logits, dim=1)
            return predictions.item()

    def sentiment_label(self, sentiment):
        labels = {0: 'Negative', 1: 'Neutral', 2: 'Positive'}
        return labels[sentiment]

if __name__ == "__main__":
    analyzer = SentimentAnalyzer('models/sentiment_model')
    sample_input = {"input_ids": torch.tensor([[101, 2023, 2003, 1037, 6925, 4151, 1999, 2662, 2187, 999, 102]])}
    sentiment = analyzer.predict_sentiment(sample_input)
    print(f"Sentiment: {analyzer.sentiment_label(sentiment)}")
