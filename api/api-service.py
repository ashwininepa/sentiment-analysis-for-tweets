# The script is the API service for sentiment analysis project.
# It exposes API endpoint (/predict) that accepts text input, processes using pre-trained model, and returns sentiment.
# Loads pre-trained model and vectorizer from pickle files.
# Initializes Flask based API
# Exposes a /predict endpoint that:
# - Accepts JSON payload containing the text to analyze
# - Transforms the text using the vectorizer
# - Uses the model to predict sentiment
# - Returns the sentiment

# Import libraries
import pickle
import logging

from flask import Flask, request, jsonify


logging.info("Starting the API service...")

# Load the pre-trained model and vectorizer
with open('./models/sentiment_analysis_log_model.pkl', 'rb') as model_file:
    logging.info("Loading the model...")
    model = pickle.load(model_file) # Used to classify the sentiment

with open('./models/tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    logging.info("Loading the vectorizer...")
    vectorizer = pickle.load(vectorizer_file) # Used to transform the text data into a format suitable for the model

# Initialize Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST']) # Defines a POST endpoint that accepts JSON and returns a sentiment
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
    app.run(host='0.0.0.0', port=5000) # Runs the Flask app on host 0.0.0.0 and port 5000, host ensures that the app is accessible from other containers or machines in the network