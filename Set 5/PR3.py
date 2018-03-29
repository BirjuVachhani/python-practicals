from os import listdir, rmdir
from os.path import isfile, join

def create_path(path):
    path_parts = path.split('\\')
    return '\\\\'.join(path_parts)

def get_files(location):
    file_list = list()
    files = listdir(location)
    #print(files)
    for f in files:
        if isfile(join(location,f)):
            f_parts = f.split('.')
            f_parts.pop()
            file_name = '.'.join(f_parts)
            file_names_without_numbers = ''.join([i for i in file_name if not i.isdigit()])
            file_list.append(file_names_without_numbers)
    return file_list

loc = input('Enter path of prank folder: ')
path = create_path(loc)
file_list = get_files(path)
for f in file_list:
    print(f)
