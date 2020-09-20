from flask import Flask, render_template, request, redirect, url_for
from string import Template
import pandas as pd
import twitter
import smd
from map_world import update_map
from map_switzerland import update_map_swiss

WORLD_ID = 'X3Ps8'
SWISS_ID = 'Tmt8o'

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('world'))

@app.route('/world')
def world():
    return render_template('world.html', MAP_ID=WORLD_ID)

@app.route('/switzerland')
def switzerland():
    return render_template('switzerland.html', MAP_ID=SWISS_ID)

@app.route('/upload_world', methods = ['GET', 'POST'])
def upload_csv_world():
    if request.method == 'POST':
        uploaded_files = request.files.getlist("file")
        #file = request.files['file']
        twitter.process_data(uploaded_files) 
        update_map(WORLD_ID)
        return redirect(url_for('world'))

@app.route('/upload_ch', methods = ['GET', 'POST'])
def upload_csv_ch():
    if request.method == 'POST':
        uploaded_files = request.files.getlist("file")
        #file = request.files['file']
        smd.process_data(uploaded_files) 
        update_map_swiss(SWISS_ID)
        return redirect(url_for('switzerland'))

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)