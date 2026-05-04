from transformers import pipeline

# Initialize the pipeline once
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def get_sentiment(text):
    result = sentiment_pipeline(text)[0]
    return {
        'label': result['label'],
        'score': round(float(result['score']), 4)
    }
