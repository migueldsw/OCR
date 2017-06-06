"""
OCR with textract
http://textract.readthedocs.io/en/stable/
"""
from utils import get_files_list, write_file, set_encoding
import textract

set_encoding()

SOURCE_PATH = "./source/"
OUTPUT_PATH = "./output/"
files = get_files_list(SOURCE_PATH)

for file_name in files:
    if file_name.split('.')[1] == 'pdf':
        print ("[PDF]File: %s" % file_name)
        text = textract.process(SOURCE_PATH + file_name, method='tesseract', language='eng')
    elif file_name.split('.')[1] == 'png':
        print ("[PNG]File: %s" % file_name)
        text = textract.process(SOURCE_PATH + file_name, language='eng')
    else:
        print ("File: %s" % file_name)
        text = textract.process(SOURCE_PATH + file_name)
    print text
    write_file(OUTPUT_PATH + '[TEXTRACT]_' + file_name.split('.')[0] + '.txt', text)
