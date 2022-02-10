#!/usr/bin/python3

"""
Test script for managing files too large for our API.
"""

import os
import errno
import shutil
from pathlib import Path
#from os import path


DEFAULT_GIVEN_DIR_PATH = '/Users/otenkeu/wa/script_python/obrien-3play/test_dir'

DEFAULT_ERROR_DIR_PATH = '/Users/otenkeu/wa/script_python/obrien-3play/error_dir'

print("Please enter folder path (enter for default)")
given_dir_path = os.path.abspath(input() or DEFAULT_GIVEN_DIR_PATH)


print("Please enter the error folder path (enter for default)")
error_dir_path = os.path.abspath(input() or DEFAULT_ERROR_DIR_PATH)


max_size = 131072  # larger than this is an error

# Check whether the specified error_dir_path is an existing directory or not;
# create if not

if not os.path.exists(error_dir_path):
    try:
        os.makedirs(error_dir_path)
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise
        else:
            print('UNKNOWN EXIT')
            raise SystemExit

# Walk the directory, moving files that don't meet our condition
for path, dirs, files in os.walk(given_dir_path):
    # checking the size of each file
    for file in files:
        size = os.stat(os.path.join(given_dir_path, file)).st_size
        if size > max_size:
            shutil.move(os.path.join(given_dir_path, file), error_dir_path)
            print("the filename moved is", file,"the file size is",size, "bytes which is greater 131072 bytes ")


print ('Congratulation the script ran successfully')
