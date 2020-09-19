from flask import Flask, render_template, request, redirect, url_for
from string import Template
import pandas as pd
from twitter import process_data

app = Flask(__name__)

@app.route('/')
@app.route('/world')
def homepage():
    return render_template('index.html')

@app.route('/upload', methods = ['GET', 'POST'])
def upload_csv():
    if request.method == 'POST':
        uploaded_files = request.files.getlist("file")
        #file = request.files['file']
        process_data(uploaded_files)        
        return redirect(url_for('homepage'))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)