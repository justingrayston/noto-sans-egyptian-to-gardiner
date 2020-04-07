#!/usr/local/bin/python
import json
import glob
import os


f = open('unicode2gardiner.json', 'r')

data = json.load(f)


for k, v in data.items():
    file_to_rename = glob.glob('svg/u{}_NotoSansEgyptianHieroglyphs.svg'.format(k))
    new_filename = 'svg/{}.svg'.format(v.lower())
    if len(file_to_rename):
        print('old file: {}, new file: {}'.format(file_to_rename[0], new_filename))
        os.rename(file_to_rename[0], new_filename)