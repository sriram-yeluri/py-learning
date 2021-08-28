
fname = input('Enter your first name:')
lname = input('Enter your last name:')

try:
    my_file = open('file1.txt', 'a')
    my_file.write(fname)
    my_file.write(lname)
    my_file.write('\n')
except FileNotFoundError:
    print("File not found")
finally:
    print("CLosing the file")
    my_file.close()


