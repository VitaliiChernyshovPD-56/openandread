import os
from pprint import pprint
import glob

base_path = os.getcwd()
path = 'sort'
full_path  = os.path.join(base_path, path, '/.txt')

def sort_file():
    dict_file = {}
    for filename in glob.glob((os.path.join(base_path, path) + '/*.txt')):
        with open(filename, 'rt', encoding='utf-8') as f:

            pprint(os.path.basename(filename))
            quantity = sum(1 for line in f)
            pprint(quantity)

            pprint(f.readlines())

sort_file()