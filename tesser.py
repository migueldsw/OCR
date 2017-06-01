"""
OCR with PyTesser

"""
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

im = Image.open("./source/img4.png")
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('./output/img-out4.jpg')
text = pytesseract.image_to_string(Image.open('./output/img-out4.jpg'))
text2 = pytesseract.image_to_string(im)
print 'text 1:'
print (text)
print 'text 2:'
print (text2)
