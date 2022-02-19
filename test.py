#!/usr/bin/python3
"""
Test script help us to test the initial script.py.
"""

import os
import errno
import shutil
import subprocess
import pathlib
import click
from pathlib import Path
from items import Item
opts = Item(
    given_dir_path= './test_dir',
    error_dir_path = './error_dir',
    bank_dir_path = './bank_files',
)
# Preparing for testing by removing test_dir and error_dir

def process_dirs(given_dir_path, error_dir_path, bank_dir_path, total_file = 0, total_file_move = 0):

    if os.path.exists(given_dir_path):
        try:
            shutil.rmtree(given_dir_path)
        except OSError as e:
            print("Error: %s : %s" % (given_dir_path, e.strerror))

    if os.path.exists(error_dir_path):
        try:
            shutil.rmtree(error_dir_path)
        except OSError as e:
            print("Error: %s : %s" % (error_dir_path, e.strerror))


    # Check whether the specified error_dir_path is an existing directory or not;
    # create if not

    if not os.path.exists(given_dir_path):
        try:
            os.makedirs(given_dir_path)
        except OSError as error:
            if error.errno != errno.EEXIST:
                raise
            else:
                print('UNKNOWN EXIT')
                raise SystemExit

    if not os.path.exists(error_dir_path):
        try:
            os.makedirs(error_dir_path)
        except OSError as error:
            if error.errno != errno.EEXIST:
                raise
            else:
                print('UNKNOWN EXIT')
                raise SystemExit

    src_files = os.listdir(bank_dir_path)
    for file_name in src_files:
        full_file_name = os.path.join(bank_dir_path, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, given_dir_path)


    options = dict(capture_output=True, encoding='utf-8')
    result = subprocess.run(['./script.py'], **options)
    print(result)

    # now counting the number of file in the test directory after the script ran
    print('counting the number of files ...')

    for path in pathlib.Path(given_dir_path).iterdir():
        if path.is_file():
            total_file += 1
    print (" The total files in the test directory: ", total_file)

    # now counting the number of file in the error directory after the script ran
    print('counting the number of files ...')
    for path in pathlib.Path(error_dir_path).iterdir():
        if path.is_file():
            total_file_move += 1
    print (" The total files moved in the error directory: ", total_file_move)
    print ('Congratulation the test is working as expected')

@click.command()
@click.option('--dir', default=opts.given_dir_path)
@click.option('--errordir', default=opts.error_dir_path)
@click.option('--ask', default=False, is_flag=True)
def cli(**kwargs):
    opts.update(kwargs)
    print()
    if opts.ask:
        opts.given_dir_path = input('dir (enter for default): ').strip() or opts.given_dir_path
        
        opts.error_dir_path = input('errordir (enter for default): ').strip() or opts.error_dir_path

    process_dirs(opts.given_dir_path, opts.error_dir_path, opts.bank_dir_path)
if __name__ == '__main__':
    cli()