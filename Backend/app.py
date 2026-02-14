from flask import Flask, request, jsonify
import os
from flask_cors import CORS
from services.pdf_loader import extract_text_from_pdf
from services.ocr import extract_text_from_image
from services.rag_pipeline import process_document, ask_question

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files['file']
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    if file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(path)
    else:
        text = extract_text_from_image(path)

    process_document(text)
    os.remove(path)
    return jsonify({"message": "Document processed successfully"})

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json['question']
    result = ask_question(question)
    return jsonify({"answer": result})

if __name__ == "__main__":
    app.run(debug=True)
