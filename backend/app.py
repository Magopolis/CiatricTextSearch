from flask import Flask, jsonify, request
from pipeline import process_text

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    text = data.get('text', '')
    result = process_text(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
