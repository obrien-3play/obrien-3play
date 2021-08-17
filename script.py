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


PATH_ERROR_DIR= '/Users/otenkeu/error_dir'

# for storing SIZE of each file
SIZE = 0

MAX_SIZE = 131072

#given_dir = '~/otenkeu/Downloads'

# Check whether the specified path_ERROR_DIR is an existing directory or not

if not os.path.exists(PATH_ERROR_DIR):
    try:
        os.makedirs(PATH_ERROR_DIR)
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise

for path, dirs, files in os.walk(PATH_ERROR_DIR):
    # checking the SIZE of each file
    for file in files:
        SIZE = os.stat(os.path.join( given_dir, file  )).st_SIZE
        #                            ????? something else than folder

        if SIZE>MAX_SIZE:
            shutil.move(path.join(given_dir,file), PATH_ERROR_DIR)

print ('Script ran successfully')
