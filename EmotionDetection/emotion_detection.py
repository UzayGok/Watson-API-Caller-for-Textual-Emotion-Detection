import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=input_json, headers=headers)
    if (response.status_code == 400):
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    dictionary_response=json.loads(response.text)
    emotion_dict  = dictionary_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion_dict, key = lambda i: emotion_dict[i])
    emotion_dict.update({'dominant_emotion': dominant_emotion})
    return emotion_dict