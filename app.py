from flask import Flask, render_template, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

# Ensure static folder exists
if not os.path.exists('static'):
    os.makedirs('static')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/save-resume', methods=['POST'])
def save_resume():
    data = request.json

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"resume_{timestamp}.json"
    filepath = os.path.join('static', filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    return jsonify({
        "status": "success",
        "file": filepath
    })


if __name__ == '__main__':
    app.run(debug=True)
