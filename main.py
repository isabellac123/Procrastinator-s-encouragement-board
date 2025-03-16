from flask import Flask, jsonify, render_template_string
import random

app = Flask(__name__)

encouragements = [
  "Great job delaying that task! Every minute counts.",
  "You're a master at postponing—keep up the good work!",
  "Procrastination is an art, and you're a true artist!",
  "Why do today what you can put off until tomorrow?",
  "Your ability to delay is truly inspirational.",
  "Keep postponing; you're doing it perfectly!",
  "You have a talent for making time stand still.",
  "Every second wasted is a moment of excellence in procrastination.",
  "You're setting records in the art of delay.",
  "Procrastination: the best ideas come at the last minute.",
  "Embrace the delay—you’re a champion of doing nothing.",
  "Your procrastination skills are off the charts!",
  "Keep calm and delay on.",
  "Why rush when you can take your sweet time?",
  "Your future self will thank you for all this delay.",
  "You're mastering the art of not doing things.",
  "Delayed tasks are just future accomplishments in disguise.",
  "Procrastination unlocks unexpected creativity.",
  "You're turning delay into a lifestyle.",
  "Keep procrastinating—you're doing it magnificently!"
]

@app.route("/")
def index():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Procrastinator’s Encouragement Board</title>
      <style>
        body {
          font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
          background-color: #f5f5f7;
          color: #1d1d1f;
          margin: 0; padding: 0;
        }
        .container {
          max-width: 700px;
          margin: 80px auto;
          text-align: center;
          padding: 20px;
          background: #fff;
          border-radius: 12px;
          box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        h1 { font-size: 2.5rem; margin-bottom: 0.5rem; }
        #result {
          font-size: 1.3rem;
          margin: 20px 0;
          padding: 30px;
          border: 1px solid #eaeaea;
          border-radius: 8px;
          background: #f9f9f9;
        }
        button {
          background-color: #007aff;
          border: none;
          color: white;
          padding: 10px 20px;
          font-size: 1rem;
          border-radius: 8px;
          cursor: pointer;
          transition: background 0.3s ease;
        }
        button:hover { background-color: #005bb5; }
      </style>
    </head>
    <body>
      <div class="container">
        <h1>Procrastinator’s Encouragement Board</h1>
        <div id="result">{{ result }}</div>
        <button onclick="fetchResult()">Encourage Me</button>
      </div>
      <script>
        function fetchResult() {
          fetch('/api')
          .then(response => response.json())
          .then(data => { document.getElementById('result').innerText = data.result; });
        }
      </script>
    </body>
    </html> 
    """
    return render_template_string(html, result=random.choice(encouragements))

@app.route("/api")
def api():
    return jsonify({"result": random.choice(encouragements)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
