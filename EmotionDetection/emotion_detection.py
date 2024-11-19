import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj =  { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, headers=header, json=myobj)
    
    # Convert the response text into a dictionary
    formatted_response = json.loads(response.text)

    # Extract emotion predictions
    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Get the scores for each emotion
    anger_score = emotion_predictions.get('anger', 0)
    disgust_score = emotion_predictions.get('disgust', 0)
    fear_score = emotion_predictions.get('fear', 0)
    joy_score = emotion_predictions.get('joy', 0)
    sadness_score = emotion_predictions.get('sadness', 0)

    # Create a dictionary to store the emotions and their scores
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    # Find the dominant emotion (emotion with the highest score)
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Add the dominant emotion to the dictionary
    emotion_scores['dominant_emotion'] = dominant_emotion

    return emotion_scores