#! /usr/bin/python3

"""
Test script for managing files too large for our API.
"""

import os
import os.path
import errno
import shutil

print("Enter folder path")
given_dir = os.path.abspath(input())


path= '/Users/otenkeu/error_dir'

# for storing size of each file
size = 0

max_size = 131072

#given_dir = '~/otenkeu/Downloads'

# Check whether the specified path is an existing directory or not

if not os.path.exists(path):
    try:
        os.makedirs(path)
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise

for path, dirs, files in os.walk(path):
    # checking the size of each file
    for file in files:
        size = os.stat(os.path.join( folder, file  )).st_size
        #                            ????? something else than folder

        if size>max_size:
            shutil.move(path.join(given_dir,file), path)

print ('Script ran successfully')
