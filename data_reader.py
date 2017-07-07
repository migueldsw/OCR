"""
Reads text (after OCR processing) for data retrieval
"""

from utils import get_files_list, read_text_file, local_config

FILES_PATH = local_config('processed_files_path')
DATA_OUTPUT_PATH = local_config('extracted_files_path')

# TODO: read file and search for keywords, values and so on... try levenshtein distance for matching.
