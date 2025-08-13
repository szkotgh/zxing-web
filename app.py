from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if '__main__' == __name__:
    app.run('0.0.0.0', 80, debug=True)