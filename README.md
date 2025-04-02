This is an application to deploy a ML model for sentiment analysis of Twitter messages. It will also demonstrate
to create an application in another container to read tweets from Twitter and classify them.

## Resources
1. The data used in this project is taken from Kaggle located at `https://www.kaggle.com/datasets/mfaaris/spotify-app-reviews-2022`.
1. Pre-requisites 
- One needs to have X Developers account to fetch tweets from X (Twitter).
- Follow the steps to create a new project.
- It will prompt to create API key, API secret key, Access token, Access token secret and Bearer token.
- Save the values from step 3 to your env variables locally on your computer.
- This will enable to fetch tweets using X api.
- Good to have Postman to test API and results from model.
1. Inspiration for jupyter notebook is taken from `https://github.com/ashwininepa/NLP-Era/blob/main/spotify_review_project/notebooks/sklearn_pipeline.ipynb` which is also one our past works during NLP club.
## Testing API
I have used postman to test api and by sending some text via postman.
1. Make sure you have post request and the url set to `http://127.0.0.1:5000/predict`.
1. Select 'raw' (and on right make sure JSON is selected as that is what is allowed on this api).
1. Paste example to test e.g. 
- {"Review": "This are mysteriously bad. Unknown everywhere"} or 
- {"Review: "He’s not hated , but also not really likable.  Just a boring face of the NFL.}
