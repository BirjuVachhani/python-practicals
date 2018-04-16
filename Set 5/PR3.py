from os import listdir, rmdir, rename
from os.path import isfile, join

def create_path(path):
    path_parts = path.split('\\')
    return '\\\\'.join(path_parts)

def get_files(location):
    file_list = list()
    files = listdir(location)
    #print(files)
    for f in files:
        f_path = join(location,f)
        if isfile(f_path):
            f_parts = f.split('.')
            f_ext = f_parts.pop()
            file_name = '.'.join(f_parts)
            file_names_without_numbers = ''.join([i for i in file_name if not i.isdigit()])
            file_list.append(file_names_without_numbers)
            modified_file_name = file_names_without_numbers+'.'+f_ext
            modified_file_path = join(location,modified_file_name)
            rename(f_path,modified_file_path)
    return file_list

loc = input('Enter path of prank folder: ')
path = create_path(loc)
file_list = get_files(path)
print('\nRenamed all files successfully!')
