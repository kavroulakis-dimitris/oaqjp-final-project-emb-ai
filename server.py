from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import emotion_detector 
import json

app = Flask("Emotion Detector")

@app.route("/emotionDetector") 
def sent_detector(): 
    # Retrieve the text to analyze from the request arguments 
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response 
    response = emotion_detector(text_to_analyze)

    # Remove 'dominant_emotion'  and save it to a variable if needed
    dominant = response.pop('dominant_emotion', None)

    # Convert to a formatted string with indentation
    json_string = json.dumps(response, indent=4)

    # Strip the outer curly braces and any extra whitespace/newlines
    clean_output = json_string.strip("{} \n")
    return "For the given statement, the system response is {}. The dominant emotion is  {}.".format(clean_output, dominant)

@app.route("/") 
def render_index_page(): 
    return render_template('index.html')

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000)