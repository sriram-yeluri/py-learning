my_data = open('file2.txt', 'r')
data_list = [line.strip() for line in my_data.readlines()]  # read all lines and store in a list
print(data_list)

# data_list = []
# for line in my_data.readlines():
#     data_list.append(line.strip())
#
# print(data_list)

my_data.close()
print(__name__)