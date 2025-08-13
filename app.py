from flask import Flask, render_template, redirect, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_file('static/favicon.ico')

@app.errorhandler(Exception)
def error_handler(e):
    return redirect('/')

if '__main__' == __name__:
    app.run('localhost', 12081)