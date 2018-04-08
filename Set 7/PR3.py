from re import search, compile
file_name = input('Enter file name with extension: ')
counter = 0
reg_exp = r'^From (\S+@\S+)'
email_expression = compile(reg_exp)
try:
    with open(file_name,'r') as f:
        for line in f:
            if line.startswith('From '):
                counter += 1
                match_obj = email_expression.search(line)
                if match_obj is not None:
                    email = match_obj.group(1)
                    print(email)
        print('\nTotal lines starting with "From ": {}'.format(counter))

except IOError as e:
    print('No file found: {}'.format(e)) 
