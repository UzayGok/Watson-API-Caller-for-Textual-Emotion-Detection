'''Run this module to start the Flask server
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def run_ed():
    '''This function calls the emotion detection module to receive the result and format it
    '''
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
    "For the given statement, the system response is: " +
    "'anger': " + response['anger'] + ", " +
    "'disgust': " + response['disgust'] + ", " +
    "'fear': " + response['fear'] + ", " +
    "'joy': " + response['joy'] + " and " +
    "'sadness': " + response['sadness'] + ". " +
    "The dominant emotion is " + response['dominant_emotion'] + "."
    )

@app.route("/")
def render_index_page():
    '''render index page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    #run app
    app.run(host="0.0.0.0", port = 5000)
