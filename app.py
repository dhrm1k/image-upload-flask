from flask import Flask, render_template, request, send_file
import os
from PIL import Image
from io import BytesIO

app = Flask(__name__)

# Folder to save uploaded images
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    image_file = request.files['image']
    image_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
    image_file.save(image_path)
    
    # Process image to JPEG format
    img = Image.open(image_path)
    img = img.convert('RGB')
    
    # Save it as a JPEG in memory
    img_io = BytesIO()
    img.save(img_io, 'JPEG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/jpeg', as_attachment=True, download_name='processed_image.jpg')

if __name__ == "__main__":
    app.run(debug=True)

