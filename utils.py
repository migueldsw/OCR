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
    """
    Get the file name list of the given path
    :param path: path
    :return: list of files names
    """
    return [f for f in listdir(path) if isfile(join(path, f))]


def write_file(file_path_name, text, encode='utf-8'):
    if encode == 'utf-8':
        f = codecs.open(file_path_name, 'w', "utf-8")
    else:
        f = open(file_path_name, 'w')
    f.write(text + '\n')
    f.close()


def local_config(value):
    """
    Get local configuration data
    :param value: 'original_files_path' | 'processed_files_path'
    :return: the selected data string
    """
    f = open('local_config', 'r')
    lines = [x.strip('\n') for x in f.readlines()]
    if value == 'original_files_path':
        return lines[0]
    elif value == 'processed_files_path':
        return lines[1]
