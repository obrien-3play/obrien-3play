#!/usr/bin/env python3
"""
Test script for managing files too large for our API.
"""
import os
import errno
import shutil
import click
from pathlib import Path
from items import Item
opts = Item(
    given_dir_path= './test_dir',
    error_dir_path = './error_dir',
)

def process_dirs(given_dir_path, error_dir_path, max_size=131072):
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
    # Walk the directory, moving files that don't meet our condition
    for path, dirs, files in os.walk(given_dir_path):
        # checking the size of each file
        for file in files:
            size = os.stat(os.path.join(given_dir_path, file)).st_size
            if size > max_size:
                print()
                shutil.move(os.path.join(given_dir_path, file), error_dir_path)
                print()
                print("the filename is", file,"the file size is",size, "bytes which is greater" ,max_size)
                
    # If the error directory has a file that is less the than max_size
    # the file will be moved back to the given_dir
    #
    for path, dirs, files in os.walk(error_dir_path):
        # checking the size of each file
        for file in files:
            size = os.stat(os.path.join(error_dir_path, file)).st_size
            if size < max_size:
                print()
                shutil.move(os.path.join(error_dir_path, file), given_dir_path)
                print("ALERT ALERT This", file,"does not beloow HERE , the file size is",size, "bytes which is smaller than" ,max_size )
                print()
                print ('Congratulation the script ran successfully')

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
    #print(opts)
    process_dirs(opts.given_dir_path, opts.error_dir_path)
    print()
if __name__ == '__main__':
    cli()