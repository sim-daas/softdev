def rwfile(change, filename='test.txt'):
    with open(filename, 'r') as file:
        content = file.read()
        print('File contents: ', content)
    with open(filename, 'a') as file:
        file.write(change+"\n")
        print('Change written to file.', change)
    with open(filename, 'r') as file:
        content = file.read()
        print('File contents: ', content)

rwfile(input('Enter change: '))
