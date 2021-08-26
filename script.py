#!/usr/bin/env python3

"""
Test script for managing files too large for our API.
"""

import errno
import os
import shutil
from pathlib import Path

import click


def process_dir(given_dir, error_dir, max_size):
    base_dir = Path.home()
    if given_dir is None:
        print("Enter folder path (enter for default)")
        given_dir = os.path.abspath(input())
        if not given_dir:
            given_dir = base_dir / 'Downloads'

    if not error_dir:
        error_dir = base_dir / 'error_dir'

    # Check whether the error_dir exists; create if not
    if not os.path.exists(error_dir):
        try:
            os.makedirs(error_dir)
        except OSError as error:
            if error.errno != errno.EEXIST:
                raise error
            print(f'UNKNOWN EXIT {error}')
            raise SystemExit

    # Walk the directory, moving files that don't meet our condition
    # into the error_dir
    for path, dirs, files in os.walk(given_dir):
        # checking the size of each file
        for file in files:
            size = os.stat(os.path.join(given_dir, file)).st_size
            if size > max_size:
                shutil.move(path.join(given_dir, file), error_dir)

    print ('Script ran successfully')


@click.command()
@click.option('--dir', default=None)
@click.option('--error-dir', default=None)
@click.option('--max-size', default=128 * 1024)
def main(dir, error_dir, max_size):
    print(f'{dir=} {error_dir=} {max_size=}')
    process_dir(dir, error_dir, max_size)


if __name__ == '__main__':
    main()
