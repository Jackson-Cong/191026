#-*-coding:UTF-8 -*-

def double_list(input_list):
    'Double all elements of a list'

    list_length = len(input_list)
    for idx in range(list_length):
        input_list[idx]*= 2

        return

# call function
mylist = [1,3,5,7,9]
double_list(mylist)
print(mylist)
