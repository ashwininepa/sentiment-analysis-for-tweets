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

## Building images and testing
1. docker-compose.yml serves the purpose to create images for api and message reader services.
1. To run it, use `docker-compose up --build` this command. This will create images for app-service and twitter reader service
1. Use Postman to test the model and links
1. Select 'raw' (and on right make sure JSON is selected as that is what is allowed on this api).
1. Paste example to test e.g. 
- {"Review": "This are mysteriously bad. Unknown everywhere"} or 
- {"Review: "He’s not hated , but also not really likable.  Just a boring face of the NFL.}
6. Next thing is good to have gcloud credentials or whichever cloud platform you choose.

## Deploy to gcloud run
1. Authenticate docker with gcp
gcloud auth configure-docker
2. Tag local docker image
- `docker tag sentiment-analysis-for-tweets-api_service:latest gcr.io/sentiment-analysis-455515/sentiment-analysis-for-tweets-api_service:latest`
- `docker tag sentiment-analysis-for-tweets-twitter_reader:latest gcr.io/sentiment-analysis-for-tweets-twitter_reader:latest/sentiment-analysis-455515/sentiment-analysis-for-tweets-twitter_reader:latest`
3. Push the image to GCR
- `docker push gcr.io/sentiment-analysis-455515/sentiment-analysis-for-tweets-api_service:latest`
- `docker push gcr.io/sentiment-analysis-455515/sentiment-analysis-455515/sentiment-analysis-for-tweets-twitter_reader:latest`
4. Verify the images in GCP(console.cloud.com > Container Registry > Artifact Registry)
5. Deploy the images to GCP
- `gcloud run deploy api-service --image gcr.io/sentiment-analysis-455515/sentiment-analysis-for-tweets-api_service:latest --memory 8G`
- `gcloud run deploy api-service --image gcr.io/sentiment-analysis-455515/sentiment-analysis-455515/sentiment-analysis-for-tweets-twitter_reader:latest --memory 8G`
