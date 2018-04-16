from os import listdir
from os.path import isfile, abspath, join

def get_files(file_dict,dir_name):
    dir_data = listdir(dir_name)
    for dir in dir_data:
        path = join(dir_name,dir)
        if isfile(path):
            file_dict[dir] = abspath(path)
        else:
            get_files(file_dict,join(dir_name,dir))

def create_path(path):
    path_parts = path.split('\\')
    return '\\\\'.join(path_parts)

loc = input('Enter path: ')
path = create_path(loc)
print(path)
file_dict = dict()
get_files(file_dict,loc)
for key,value in file_dict.items():
    print('{}:\n{}\n'.format(key,value))