# Ques_2
# Write a Python function that takes a list of strings as input and returns a tuple containing the shortest and longest word from the list
def word_length(input_list):
    if not input_list:
        return ("No words found", "No words found")
    shortest = min(input_list, key=len)
    longest = max(input_list, key=len)
    return (shortest, longest)
input_string = input("Enter comma-separated strings: ")
list_of_strings = [s.strip() for s in input_string.split(',')]
result_tuple = word_length(list_of_strings)
print(f"Shortest Word: {result_tuple[0]}")
print(f"Longest Word: {result_tuple[1]}")
