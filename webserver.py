from flask import Flask, render_template, request, redirect, url_for
from string import Template
import pandas as pd
from twitter import process_data
from map_world import update_map
from map_switzerland import update_map_swiss

WORLD_ID = 'X3Ps8'
WORLD_ID_SWISS = 'Tmt8o'

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('world'))

@app.route('/world')
def world():
    return render_template('world.html', MAP_ID=WORLD_ID)

@app.route('/switzerland')
def switzerland():
    return render_template('switzerland.html', MAP_ID=WORLD_ID_SWISS)

@app.route('/upload', methods = ['GET', 'POST'])
def upload_csv():
    if request.method == 'POST':
        uploaded_files = request.files.getlist("file")
        #file = request.files['file']
        process_data(uploaded_files) 
        update_map(WORLD_ID)
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)