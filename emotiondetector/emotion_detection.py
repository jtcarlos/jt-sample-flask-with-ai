""" 
This module contains a function that detects emotions on a given text / phrase 
"""
import json
import requests

# NOTE: Don't try to use this
# This won't work unless you are in the lab's environment
URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    """ 
    This function detects the emotion of user based on a given text / phrase 
    """
    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(URL, json=payload, headers=HEADERS, timeout=10)
    formatted_response = json.loads(response.text)

    # get all emotions based on the text / phrase
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    emotions["dominant_emotion"] = max(emotions, key=lambda index: emotions[index])

    return emotions
