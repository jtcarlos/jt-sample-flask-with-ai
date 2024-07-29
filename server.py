""" 
Server code for emotion detector 
"""
from flask import Flask, render_template, request
from emotiondetector.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    """ 
    Calls the emotion_detector function and returns the response 
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    joy = response["joy"]
    fear = response["fear"]
    anger = response["anger"]
    disgust = response["disgust"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is 'anger': {anger}, " \
    f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. " \
    f"The dominant emotion is <b>{dominant_emotion}</b>."

@app.route("/")
def render_index_page():
    """ 
    Renders the index page 
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
