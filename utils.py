"""
Utils
"""
from os import listdir
from os.path import isfile, join


def get_files_list(path):
    return [f for f in listdir(path) if isfile(join(path, f))]


def write_file(file_path_name, text):
    f = open(file_path_name, 'w')
    f.write(text + '\n')
    f.close()
