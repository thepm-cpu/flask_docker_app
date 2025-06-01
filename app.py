from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hey future Chibuzor, this is our first website!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
