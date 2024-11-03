from flask import Flask, jsonify, request

app = Flask(__name__)

# Một danh sách để lưu trữ dữ liệu
data = []

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def create_data():
    new_data = request.json  # Lấy dữ liệu từ yêu cầu JSON
    data.append(new_data)  # Thêm dữ liệu mới vào danh sách
    return jsonify(new_data), 201  # Trả về dữ liệu đã thêm cùng mã trạng thái 201

if __name__ == '__main__':
    app.run(debug=True)
