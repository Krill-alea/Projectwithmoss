# very small simple testing module
from flask import Flask, render_template

app = Flask(__name__)


#routes go here
@app.route('/')
def index():
    return render_template('index.html')

#this bit of code runs the app that we just made with debug on
if __name__ == "__main__":
    app.run(debug=True)