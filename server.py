from flask import Flask, request, jsonify
from emotion_detection import emotion_predictor

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    result = emotion_predictor(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
