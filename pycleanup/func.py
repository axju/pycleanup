'''This file contains all the functions.'''
from pycleanup import DIR_KIND, FILE_KIND
import os, shutil


def cleanup(directory, args):
    search = []
    for key, data in DIR_KIND.items():
        if args.get(key, False):
            search.append(data['search'])

    n = delete_dirs(directory, search)
    print('Delete', n, 'directorys')

    search = []
    for key, data in FILE_KIND.items():
        if args.get(key, False):
            search.append(data['search'])

    n = delete_files(directory, search)
    print('Delete', n, 'files')


def print_infos(directory):
    print('directory:', directory)

    result = {}
    for dir in find_dir(directory):
        for key, data in DIR_KIND.items():
            if dir.find(data['search'])>0:
                result[key] = result.get(key, 0) + 1
                break

    for dir in find_files(directory):
        for key, data in FILE_KIND.items():
            if dir.find(data['search'])>0:
                result[key] = result.get(key, 0) + 1
                break
    print()
    for name, count in result.items():
        print(name + ':', count)

    if not result:
        print('Nothing to clean up')


def delete_files(directory, search):
    counter = 0
    for file in find_files(directory):
        for item in search:
            if file.find(item)>0:
                os.remove(file)
                counter += 1
                break
    return counter


def delete_dirs(directory, search):
    counter = 0
    for dir in find_dir(directory):
        for item in search:
            if dir.find(item)>0:
                shutil.rmtree(dir, ignore_errors=True)
                counter += 1
                break
    return counter


def find_files(directory):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            filename = os.path.join(root, basename)
            yield filename


def find_dir(directory):
    for root, dirs, files in os.walk(directory):
        for basename in dirs:
            dirname = os.path.join(root, basename)
            yield dirname
