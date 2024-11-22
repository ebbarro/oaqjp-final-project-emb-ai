import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, headers=header, json=myobj)
    
    if response.status_code == 400:
        # Return dictionary with values as None for blank entries
        emotion_scores = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return emotion_scores
    else:
        formatted_response = json.loads(response.text)
        
        # Access the predictions
        emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
        
        # Get emotion scores
        emotion_scores = {
            'anger': emotion_predictions.get('anger', 0),
            'disgust': emotion_predictions.get('disgust', 0),
            'fear': emotion_predictions.get('fear', 0),
            'joy': emotion_predictions.get('joy', 0),
            'sadness': emotion_predictions.get('sadness', 0)
        }
        
        # Find the dominant emotion
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        emotion_scores['dominant_emotion'] = dominant_emotion
        
        return emotion_scores

        