from PIL import Image

def open_pic(image_path):
    image = Image.open(image_path)
    image.show()