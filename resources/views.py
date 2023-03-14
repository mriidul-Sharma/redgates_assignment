from PIL import Image
from PIL import ImageColor

def generate_image(width, height, clr):
    """ the function is gonna return an image generated by using the parameters provided. """

    img  = Image.new( mode = "RGB", size = (int(width), int(height)), color = clr)

    return img
