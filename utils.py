"""
Utils
"""
from os import listdir
from os.path import isfile, join
import codecs
import sys


def set_encoding():
    reload(sys)
    sys.setdefaultencoding('utf8')


def get_files_list(path):
    return [f for f in listdir(path) if isfile(join(path, f))]


def write_file(file_path_name, text, encode='utf-8'):
    if encode == 'utf-8':
        f = codecs.open(file_path_name, 'w', "utf-8")
    else:
        f = open(file_path_name, 'w')
    f.write(text + '\n')
    f.close()
