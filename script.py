from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        image = Image.open(file.stream)
        # Пример обработки: конвертация в grayscale
        image = image.convert('L')
        # Сохраняем изображение в память
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        return jsonify({'message': 'Image uploaded and processed successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)



