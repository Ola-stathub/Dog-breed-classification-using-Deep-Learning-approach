from flask import Flask, request, render_template, redirect, url_for
import os
import torch
from PIL import Image
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
app.config['MODEL_PATH'] = '/Users/mac/Downloads/mymodel.pt'  

# Load YOLO model
model = torch.hub.load('/Users/mac/Desktop/Flaskapp/yolov5', 'custom', path=app.config['MODEL_PATH'], source='local')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Run inference
        img = Image.open(filepath)
        results = model(img)

        # Save the result image
        result_img = np.array(results.render()[0])
        result_img_pil = Image.fromarray(result_img)
        result_img_path = os.path.join(app.config['UPLOAD_FOLDER'], 'result_' + filename)
        result_img_pil.save(result_img_path)

        # Extract predictions
        predictions = results.pandas().xyxy[0].to_dict(orient="records")

        return render_template('result.html', original_image=url_for('static', filename='uploads/' + filename), result_image=url_for('static', filename='uploads/result_' + filename), results=predictions)
    return redirect(request.url)

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
