from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "coucou"})

app.run(host='0.0.0.0', port=5000, debug=True)
