from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return 'Positive'
    elif sentiment_score < 0:
        return 'Negative'
    else:
        return 'Neutral'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'text' in request.form:
        text = request.form['text']
        sentiment = analyze_sentiment(text)
        return jsonify({'sentiment': sentiment})
    else:
        return jsonify({'error': 'Text not found in request'}), 400

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
