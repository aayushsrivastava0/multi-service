from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/divide', methods=['GET'])
def divide():
    x = float(request.args.get('x', 0))
    y = float(request.args.get('y', 0))
    if y == 0:
        return jsonify(error="Cannot divide by zero"), 400
    return jsonify(result=x / y)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
