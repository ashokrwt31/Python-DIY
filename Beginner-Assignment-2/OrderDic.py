from collections import OrderedDict

dic_length = int(input("enter number of element element in dictionary: "))
input_dic = OrderedDict()

for i in range(dic_length):
    keys = input("Enter key: ")
    values = input("Enter value for above key: ")
    input_dic[keys] = values
print("result dictionary is ",input_dic);


