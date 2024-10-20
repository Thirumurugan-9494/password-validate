from flask import Flask, request, jsonify
import json

app = Flask(__name__)
 
def capitalize(a):
    return a.capitalize()
def uppercase(a):
    return a.uppercase()
def lowercase(a):
    return a.lowercase()

@app.route('/capitalize', methods=['POST'])
def capitalize_text():
    print(request.data)
    d = json.loads(request.data)
    string =d['string']
    result=capitalize(string)
    return jsonify({'capitalize':result})

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/uppercase', methods=['POST'])
def uppercase_txt():
    print(request.data)
    d = json.loads(request.data)
    string =d['string']
    result=uppercase(string)
    return jsonify({'uppercase':result})

if __name__ == '__main__':
    app.run(debug=True)
