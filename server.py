"""
Flask server for emotion detection application.
Provides endpoints for analyzing text emotions and rendering the UI.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def emot_detector():
    """
    Endpoint for emotion detection.
    """
    text_to_analyse = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyse)

    emotion_scores = {
        'anger': response.get('anger', 0),
        'disgust': response.get('disgust', 0),
        'fear': response.get('fear', 0),
        'joy': response.get('joy', 0),
        'sadness': response.get('sadness', 0)
    }

    scores_str = ', '.join(f"{key}: {value}" for key, value in emotion_scores.items())

    dominant_emotion = response['dominant_emotion']

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement:\n"
        f"the system response is:\n{scores_str}.\n"
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """
    Render the index page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
