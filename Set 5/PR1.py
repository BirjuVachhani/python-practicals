data=input('Enter text to save it in a file:')
file_name=input('enter file name with extension in which the text will be stored:')
with open(file_name,'w') as f:
    f.write(data)

print('Data is written successfully.')
print('\nWritten Data:')
with open(file_name) as f:
    print(f.read())
