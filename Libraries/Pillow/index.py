#!/usr/bin/env python3

from PIL import Image
import PIL


# Opens an image
img = Image.open("<name_of_the_image_to_be_opened.extension")

# Displays the format of the image
img.format

# Displays the size of the image in a tuple
img.size

# Saves an image that has been changed
img.save("<image_name>", format="<format_to_save_image>")

# Displays an Image
img.show()