"""General utility functions that do not fit into another module"""

import uuid
import os

def random_str_uuid(string_length):
    """Returns a random string of length string_length"""
    if not isinstance(string_length, int) or not 1 <= string_length <= 32:
        msg = "string_length must be type int where 1 <= string_length <= 32"
        raise ValueError(msg)
    random = str(uuid.uuid4()).upper().replace('-', '')
    return random[0:string_length]

def random_name_filepath(path_full, length_random=5):
    '''Take a filepath, add randome characters to its basename,
    and return the new filepath

    :param filename: either a filename or filepath
    :param length_random: length of random string to be generated
    '''
    path_full_pre_extension, extension = os.path.splitext(path_full)
    random_str = random_str_uuid(length_random)
    return "{}{}{}".format(path_full_pre_extension, random_str, extension)

def list_filepathes_with_predicate(path_dir, predicate):
    '''List all filepathes in a directory that begin with predicate

    :param path_dir: the directory whose top-level contents you wish to list
    :param predicate: the predicate you want to test the directory's
        found files against
    '''
    if not os.path.isdir(path_dir):
        raise ValueError("{} is not a directory".format(path_dir))
    contents = (os.path.join(path_dir, a) for a in os.listdir(path_dir))
    files = (c for c in contents if os.path.isfile(c))
    return [f for f in files if f.startswith(predicate)]

def read_file(filepath):
    '''Read the contents of a file, returning a string variable'''
    with open(filepath, 'r') as file_to_read:
        content = file_to_read.read()
    return content

def recursive_apply(inval, func):
    '''Recursively apply a function to all levels of nested iterables

    :param inval: the object to run the function on
    :param func: the function that will be run on the inval
    '''
    if isinstance(inval, dict):
        return {k: recursive_apply(v, func) for k, v in inval.items()}
    elif isinstance(inval, list):
        return [recursive_apply(v, func) for v in inval]
    else:
        return func(inval)
