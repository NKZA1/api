from flask import Flask, request, jsonify
from flask_cors import CORS
from collections import OrderedDict

app = Flask(__name__)
CORS(app)  # Cho phép CORS

key_storage = OrderedDict()
MAX_KEYS = 400

@app.route('/api/store_key', methods=['POST'])
def store_key():
    data = request.get_json()
    if 'key' not in data:
        return jsonify({"error": "Missing key"}), 400
    
    key = data['key']
    
    if len(key_storage) >= MAX_KEYS:
        key_storage.popitem(last=False)
    
    key_id = len(key_storage) + 1
    key_storage[key_id] = key
    return jsonify({"message": "Key stored successfully", "key_id": key_id}), 201

@app.route('/api/get_key/<int:key_id>', methods=['GET'])
def get_key(key_id):
    if key_id not in key_storage:
        return jsonify({"error": "Key not found"}), 404
    
    return jsonify({"key_id": key_id, "key": key_storage[key_id]}), 200

if __name__ == '__main__':
    app.run(debug=True)
