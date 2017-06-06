"""
OCR with PyTesser

"""
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from utils import get_files_list, write_file, set_encoding

set_encoding()

SOURCE_PATH = "./source/"
OUTPUT_PATH = "./output/"
files = get_files_list(SOURCE_PATH)

# im = Image.open("./source/img4.png")
# im = im.filter(ImageFilter.MedianFilter())
# enhancer = ImageEnhance.Contrast(im)
# im = enhancer.enhance(2)
# im = im.convert('1')
# im.save('./output/img-out4.jpg')

for image_file_name in files:
    if image_file_name.split('.')[1] == 'png':
        text = pytesseract.image_to_string(Image.open(SOURCE_PATH+image_file_name))
        print "%s: \n>>%s"%(image_file_name, text)
        write_file(OUTPUT_PATH + '[PYTESSER]_' + image_file_name.split('.')[0] + '.txt', text)
