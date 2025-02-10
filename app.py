# app.py
import os
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# Folder gambar
IMAGE_FOLDER = 'static/images/'
ORGANIC_FOLDER = os.path.join(IMAGE_FOLDER, 'organik')
NON_ORGANIC_FOLDER = os.path.join(IMAGE_FOLDER, 'non-organik')

# Ambil daftar gambar dalam folder
organic_images = os.listdir(ORGANIC_FOLDER)
non_organic_images = os.listdir(NON_ORGANIC_FOLDER)

@app.route('/')
def home():
    return render_template('index.html', organic_images=organic_images, non_organic_images=non_organic_images)

@app.route('/predict', methods=['POST'])
def predict():
    selected_image = request.form.get('selected_image')
    if selected_image in organic_images:
        predicted_class = "Organik"
    elif selected_image in non_organic_images:
        predicted_class = "Non-Organik"
    else:
        predicted_class = "Tidak diketahui"
    
    image_url = url_for('static', filename=f'images/{"organik" if predicted_class == "Organik" else "non-organik"}/{selected_image}')
    return render_template('index.html', predicted_class=predicted_class, img_path=image_url, organic_images=organic_images, non_organic_images=non_organic_images)

if __name__ == '__main__':
    app.run(debug=True)
