
def remove_duplicate_element(n):
    """Remove duplicate from user defined list."""
    result_list = []
    for element in n:
        if element not in result_list:
            result_list.append(element)
    return result_list

inputList = input("Enter list number separated by space:")
userList = inputList.split()
print("User input list is:",userList)
print("Result List is:",remove_duplicate_element(userList))
