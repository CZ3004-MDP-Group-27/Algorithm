from PIL import ImageTk, Image 

def get_img():
    Arena_img = Image.open("GUI_Images/Arena.png")
    Arena_img = Arena_img.convert('RGBA')

    Arena_img = Arena_img.resize((800,800), Image.ANTIALIAS)
    return Arena_img


