import os
import sys
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename

# ✅ Add server/ to Python path so we can import utils modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ✅ Now import extract_text and matcher
from utils.extract_text import extract_text
from utils.matcher import get_matching_scores

# Create Flask blueprint
upload_blueprint = Blueprint('upload', __name__)

# Define the uploads folder path
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@upload_blueprint.route('/upload', methods=['POST'])
def upload_files():
    # ✅ Check for both resume and JD file
    if 'resume' not in request.files or 'jd' not in request.files:
        return jsonify({"error": "Missing file(s): 'resume' and/or 'jd'"}), 400

    resume = request.files['resume']
    jd = request.files['jd']

    resume_filename = secure_filename(resume.filename)
    jd_filename = secure_filename(jd.filename)

    resume_path = os.path.join(UPLOAD_FOLDER, resume_filename)
    jd_path = os.path.join(UPLOAD_FOLDER, jd_filename)

    # ✅ Save files
    resume.save(resume_path)
    jd.save(jd_path)

    try:
        # 🧠 Extract text
        resume_text = extract_text(resume_path)
        jd_text = extract_text(jd_path)

        # 🤖 Get matching scores
        scores = get_matching_scores(resume_text, jd_text)

    except Exception as e:
        return jsonify({"error": f"Text processing failed: {str(e)}"}), 500

    return jsonify({
        "message": "✅ Files uploaded and matched successfully",
        "resume_file": resume_filename,
        "jd_file": jd_filename,
        "match_scores": scores
    })
