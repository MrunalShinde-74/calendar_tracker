from flask import Flask, request, jsonify

app = Flask(__name__)

shopping_list = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(shopping_list)

@app.route('/items', methods=['POST'])
def add_item():
    data = request.json
    item = data.get("item")
    if item:
        shopping_list.append(item)
        return jsonify({"message": f"{item} added"}), 201
    return jsonify({"error": "No item provided"}), 400

@app.route('/items/<item>', methods=['DELETE'])
def delete_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        return jsonify({"message": f"{item} removed"}), 200
    return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

