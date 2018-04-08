from re import search
file_name = input('Enter file name with extension: ')
counter = 0
reg_exp = r'^From (\S+@\S+)'
try:
    with open(file_name,'r') as f:
        for line in f:
            if line.startswith('From '):
                counter += 1
                match_obj = search(reg_exp,line)
                if match_obj is not None:
                    email = match_obj.group(1)
                    print(email)
        print('\nTotal lines starting with "From ": {}'.format(counter))

except IOError as e:
    print('No file found: {}'.format(e)) 
