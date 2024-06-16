from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_current_time():
    return "Hello flask"

if __name__ == '__main__':
    app.run(debug=True)