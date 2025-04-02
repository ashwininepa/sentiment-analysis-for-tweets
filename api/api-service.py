import pickle
import logging

from flask import Flask, request, jsonify


logging.info("Starting the API service...")

# Load the pre-trained model and vectorizer
with open('./models/sentiment_analysis_log_model.pkl', 'rb') as model_file:
    logging.info("Loading the model...")
    model = pickle.load(model_file)

with open('./models/tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    logging.info("Loading the vectorizer...")
    vectorizer = pickle.load(vectorizer_file)

# Initialize Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the review text from the request
    data = request.json
    if 'Review' not in data:
        return jsonify({'error': 'No review text provided'}), 400
    review_text = [data['Review']]

    # Transform the review text using the vectorizer
    review_vectorized = vectorizer.transform(review_text)

    # Predict the sentiment using the loaded model
    prediction = model.predict(review_vectorized)
    logging.info("Prediction: ", prediction)

    # Return the prediction as a JSON response
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)