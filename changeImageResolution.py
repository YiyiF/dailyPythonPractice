# changeImageResolution.py - Practice 005, change image resolution match iPhone5

import os
from PIL import Image

iPhone5Resolution = {
    "width": 640,
    "height": 1136
}


def changeImageResolution(image):
    '''
    :param image:
    :return:
    '''
    curImage = Image.open(image)
    width, height = curImage.size
    width_ratio = width / iPhone5Resolution['width']
    height_ratio = height / iPhone5Resolution['height']
    if width_ratio <= 1 and height_ratio <= 1:
        img = curImage.copy()
    elif width_ratio >= height_ratio:
        img = curImage.copy().resize((iPhone5Resolution['width'], int(height / width_ratio)))
    elif width_ratio < height_ratio:
        img = curImage.copy().resize((int(width / height_ratio), iPhone5Resolution['height']))
    img.save('./iPhone5Images/' + 'ip5_' + os.path.split(image)[-1])


if __name__ == '__main__':
    path = 'images'
    result_dir = 'iPhone5Images'

    if not os.path.exists(result_dir):
        os.mkdir(result_dir)

    files = os.walk(path)
    for dirpath, dirnames, filenames in files:
        for filename in filenames:
            if not filename.lower().endswith(('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
                continue
            changeImageResolution(dirpath + os.path.sep + filename)

    print('Done.')
