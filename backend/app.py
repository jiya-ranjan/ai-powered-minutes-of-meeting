from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from flask_cors import CORS
from backend.whisper_utils import transcribe_audio
from gpt_utils import analyze_meeting

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # ❌ exit_ok → ✅ exist_ok

@app.route('/upload', methods=['POST'])  # ❌ methods='POST' → ✅ methods=['POST']
def upload_audio():
    if 'file' not in request.files:   # check agar file upload nahi hui
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']  # ❌ request.files('file') → ✅ request.files['file']
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # Whisper transcription
    transcript = transcribe_audio(filepath)  # ❌ transcipt → ✅ transcript

    # GPT analysis
    result = analyze_meeting(transcript)

    return jsonify({
        "transcript": transcript,
        "analysis": result
    })

if __name__ == '__main__':
    app.run(debug=True)
