# pip install qrcode
import qrcode

# pip install pillow
# from PIL import Image, ImageDraw

from tool.logging_tool import log

import qrcode

if __name__ == '__main__':
    img = qrcode.make('Some data here')
    type(img)  # qrcode.image.pil.PilImage
    img.save("some_file.png")
