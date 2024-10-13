# Ques_3
# Write a Python function that takes a list and an element as input. The function should add the element to the list only if it's not already present in the list. 
def add_element_into_list():
    my_list = input("Enter elements of the list separated by comma (e.g., 1,2,3): ")
    my_list = [int(x) for x in my_list.split(",")]
    element_to_add = int(input("Enter an element that you want to add into the list: "))
    def add_element():
        my_list  
        return element_to_add not in my_list
    if add_element():
        print(element_to_add, "added into the list successfully.")
        my_list.append(element_to_add)
        print("Updated List: ", my_list)
    else:
        print(element_to_add, "already exists in the list.")

add_element_into_list()