#!/usr/bin/python3

"""
Test script for managing files too large for our API.
"""

import os
import errno
import shutil
from pathlib import Path

base_dir = Path.home()
DEFAULT_GIVEN_DIR = base_dir / 'Downloads'

print("Enter folder path (enter for default)")
given_dir = os.path.abspath(input() or DEFAULT_GIVEN_DIR)

PATH_ERROR_DIR = base_dir / 'error_dir'
MAX_SIZE = 131072  # larger than this is an error

# Check whether the specified path_ERROR_DIR is an existing directory or not;
# create if not
if not os.path.exists(PATH_ERROR_DIR):
    try:
        os.makedirs(PATH_ERROR_DIR)
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise
        else:
            print('UNKNOWN EXIT')
            raise SystemExit

# Walk the directory, moving files that don't meet our condition
for path, dirs, files in os.walk(PATH_ERROR_DIR):
    # checking the size of each file
    for file in files:
        size = os.stat(os.path.join(given_dir, file)).st_SIZE
        if size > MAX_SIZE:
            shutil.move(path.join(given_dir, file), PATH_ERROR_DIR)

print ('Script ran successfully')
