def read(filepath, option):
    with open(filepath, 'r') as file:
        if option == 'all':
            return file.read()
        elif option == '5':
            return file.read(5)
        elif option == 'line':
            return file.readline()
        elif option == 'lines':
            return file.readlines()
print(read('Alaa.txt','all'))
print(read('Alaa.txt','5')) 
print(read('Alaa.txt','line')) 
print(read('Alaa.txt','lines'))  
def write(filepath, content, option):
    with open(filepath, 'w') as file:
        if option == 'write':
            file.write(content)
        elif option == 'lines':
            file.writelines(content)
write('Alaa2.txt', 'Hello, World!\n', 'write')
write('Alaa2.txt', ['Hello, World!\n', 'Welcome to the new file.\n', 'This is a test.\n'], 'lines')
def append(filepath, newcontent, option):
    with open(filepath, 'a') as file:
        if option == 'write':
            file.write(newcontent)
        elif option == 'lines':
            file.writelines(newcontent)
append('Alaa3.txt', 'Hello, World!3\n', 'write')
append('Alaa3.txt', ['Hello, World!3\n', 'Welcome to the new file3.\n', 'This is a test3.\n'], 'lines')