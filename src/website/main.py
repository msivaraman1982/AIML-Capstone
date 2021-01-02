from flask import Flask
from flask import request
from flask import render_template


import sys, os

from .model import Model
from .helper import save_uploaded_file


model = Model()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/tmp/upload'


if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
    model.initialize()    

@app.route('/', methods=['GET', 'POST'])
def index():
        print(request.method, flush=True)
        print(request, flush=True)
        if request.method == 'POST':
            filepath = save_uploaded_file(app.config['UPLOAD_FOLDER'], request.files['dicom'])
            image_file, result = model.predict(filepath)
            print("Length:", result)
            sys.stdout.flush()
            return render_template('index.html')
        else:
            return render_template('index.html')
