from flask import Blueprint, render_template, request, jsonify
from app.analyzer import get_sentiment

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    text = data['text']
    result = get_sentiment(text)
    return jsonify(result)
