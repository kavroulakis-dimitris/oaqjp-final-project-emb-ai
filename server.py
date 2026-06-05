"""
Emotion Detector Server Module.
Provides API endpoints to detect emotions in text and render the user interface.
"""
import json
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyzes the input text for emotions and returns a formatted string response
    displaying individual emotion scores along with the dominant emotion.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Remove 'dominant_emotion'  and save it to a variable if needed
    dominant = response.pop('dominant_emotion', None)

    # Check if the dominant_emotion is None, indicating an error or invalid input
    if dominant is None:
        return "Invalid text! Please try again!"

    # Convert to a formatted string with indentation
    json_string = json.dumps(response, indent=4)

    # Strip the outer curly braces and any extra whitespace/newlines
    clean_output = json_string.strip("{} \n")
    return (
        f"For the given statement, the system response is {clean_output}. "
        f"The dominant emotion is {dominant}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main index HTML page for the user interface.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
