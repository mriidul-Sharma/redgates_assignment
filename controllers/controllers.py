import os
from flask import request
from PIL import ImageColor
from numpy import asarray
from resources.views import *
import pandas as pd
import json

def create_random_image():
    """ function will create the image as per the provided parameters """
    try:

        width = request.args.get("width")
        height = request.args.get("height")
        color = request.args.get("color")
        ImgFormat = request.args.get("format")

        color_origins = ImageColor.getrgb(color)

        gen_image = generate_image(width, height, color_origins)
        img_name = "random_img." + ImgFormat
        gen_image.save(img_name)

        img = Image.open(img_name)
        img_array = json.dumps({"data": asarray(img).tolist()})

        os.remove(img_name, dir_fd=None)

        response = {
             "Success" : True,
             "data" : img_array
        }, 200

    except Exception as e:
            response = {
                "success": False,
                "message": str(e)
            }, 400

    return response


