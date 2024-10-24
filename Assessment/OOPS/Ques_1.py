#Ques_1
class MyString:
    def get_string(self):
        self.string = input("Enter a string: ")

    def print_string(self):
        print(self.string.upper())
# Example usage
my_string = MyString()
my_string.get_string()
my_string.print_string()