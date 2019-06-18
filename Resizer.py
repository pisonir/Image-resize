import PIL
from PIL import Image
import os

def resize(basewidth, path, input_format, output_format):
    '''
    Resizes, to the chosen pixel size (basewidth), the images with the input_format extension
    in the path folder and changes their format to the output_format
    :param basewidth: int.
    :param path: str.
    :param input_format: str.
    :param output_format: str.
    :return: nothing. It saves the new resized images.
    '''
    for image_file in os.listdir(path):
        if image_file.endswith(input_format):
            img = Image.open(image_file)
            W, H = img.size
            wpercent = (basewidth / float(W))
            # in order to keep the same ratio as the original image
            hsize = int((float(H)*float(wpercent)))
            # PIL.Image.ANTIALIAS is a high quality downsampling filter
            img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
            # replace .tif with .jpg, qulaity = 95 keeps the optimal resolution. If you don't care about resolution
            # and you just want to minimize the size of your file then you cna remove the quality option.
            img.save(image_file.replace(input_format,'_RESIZED'+output_format), quality = 95)


if __name__ == "__main__":
    path = r'C:\Users\...\folder'
    os.chdir(path)
    pixel = 300
    input_format = '.tif'
    output_format = '.jpg'
    resize(pixel, path, input_format, output_format)