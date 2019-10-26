#-*-coding:UTF-8 -*-

def fill_list(input_output_list):
    'fill sth. into an empty list'

    for element_data in range(10):
        input_output_list.append(element_data)

    return

# call function
mylist=[]
fill_list(mylist)
print(mylist)

fill_list(mylist)
print(mylist)
