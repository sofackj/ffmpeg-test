from PIL import Image, ImageTk

def open_image_and_resize(image_path, size):
    image = Image.open(image_path)
    width, height = image.size
    new_width = size
    new_image = image.resize((new_width, int(height*new_width/width)))
    tk_image = ImageTk.PhotoImage(new_image)
    return tk_image

# open_image_and_resize("test-app/entries/20555551_051_c7d6.jpeg", 200).show()