from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save-resume', methods=['POST'])
def save_resume():
    data = request.json
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"resume_data_{timestamp}.json"
    save_path = os.path.join('static', filename)

    with open(save_path, 'w', encoding='utf-8') as f:
        import json
        json.dump(data, f, indent=4)

    return jsonify({'status': 'success', 'saved_to': save_path})

if __name__ == '__main__':
    app.run(debug=True)