from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import os

app = Flask(__name__)

print("Loading sentiment analysis model...")
sentiment_pipeline = pipeline("sentiment-analysis")
print("Model loaded successfully.")

@app.route('/')
def home():
    """Render the HTML interface."""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """
    Accepts JSON payload with 'text' and returns the sentiment label and score.
    """
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided. Please send a JSON with a "text" field.'}), 400
    
    text = data['text']
    
    try:
        result = sentiment_pipeline(text)[0]
        return jsonify({
            'label': result['label'],
            'score': result['score']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
