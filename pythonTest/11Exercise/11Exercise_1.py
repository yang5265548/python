#Implement the following class hierarchy using Python:
# A publication can be either a book or a magazine.
# Each publication has a name.
# Each book also has an author and a page count, whereas each magazine has a chief editor.
# Also write the required initializers to both classes.
# Create a print_information method to both subclasses for printing out all information of the publication in question.
# In the main program, create publications Donald Duck (chief editor Aki Hyyppä) and
# Compartment No. 6 (author Rosa Liksom, 192 pages).
# Print out all information of both publications using the methods you implemented.


class Publish:
    def __init__(self,name):
        self.name=name
class Book(Publish):
    def __init__(self,name,author,pages):
        super().__init__(name)
        self.author=author
        self.pages=pages
    def print_infomation(self):
        print(f"the name of book: {self.name}")
        print(f"the author of book: {self.author}")
        print(f"the pages of book: {self.pages}")


class Magazine(Publish):
    def __init__(self,name,chiefeditor):
        super().__init__(name)
        self.chiefeditor=chiefeditor

    def print_infomation(self):
        print(f"the name of magazine: {self.name}")
        print(f"the chiefeditor of magazine: {self.chiefeditor}")



if __name__ == '__main__':
    book1=Book("Compartment No. 6 ","Rosa Liksom",192)
    magazine1=Magazine("Donald Duck"," Aki Hyyppä)")
    book1.print_infomation()
    print(" ")
    magazine1.print_infomation()