from flask import Flask, send_from_directory
#from api.populate_db import addto_classification,addto_news,addto_summaries


app = Flask(__name__,static_folder="../build")



@app.route("/")
def home():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run(debug=True)