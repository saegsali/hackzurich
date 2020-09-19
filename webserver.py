from flask import Flask, render_template, request
from string import Template
app = Flask(__name__)

@app.route('/')
@app.route('/world')
def homepage():
    return render_template('index.html')

@app.route('/upload', methods = ['GET', 'POST'])
def upload_csv():
    if request.method == 'POST':
      f = request.files['file']
      #f.save(secure_filename(f.filename))
      return 'file uploaded successfully'


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)