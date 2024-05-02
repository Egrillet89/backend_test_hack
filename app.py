import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def test_hack_1():
    return jsonify({'payload': 'success'}), 200

@app.route('/user', methods=['POST'])
def test_hack_2():
    return jsonify({"payload":'success'}), 200

@app.route('/user' , methods=['DELETE'])
def test_hack_3():
    return jsonify({"payload":'success'}), 200

@app.route('/user' , methods=['PUT'])
def test_hack_4():
    response = {
        "payload": 'success',
        "error": False
    }
    return jsonify(response), 200

@app.route('/api/v1/users' , methods=['GET'])
def test_hack_5():
    return jsonify({'payload':[]}), 200

@app.route('/api/v1/user', methods=['POST'])
def test_hack_6():
    email = request.args.get('email')
    name = request.args.get('name')
    if not email or not name:
        return jsonify({'error': 'Bad Request'}), 400
    response = {
        'payload': {
            'email': email,
            'name': name,
        }
    }

    return jsonify(response), 200 


@app.route('/api/v1/user/add', methods=['POST'])
def test_hack_7():
    data = request.form  
    email = data.get('email')
    name = data.get('name')
    id = data.get('id')

    return jsonify({
        'payload': {
            'email': email,
            'name': name,
            'id': id,
        }
    }), 200

@app.route('/api/v1/user/create', methods=['POST'])
def test_hack_8():
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    id = data.get('id')

    response = {
        'payload': {
            'email': email,
            'name': name,
            'id': id,
        }
    }

    return jsonify(response), 200 

if __name__ == '__main__':
    app.run(debug=True)
