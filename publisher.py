class Publisher:
    def __init__(self,name):
        self.name=name
class Book(Publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author
    def displayinfo(self):
        print("Publisher:",self.name)
        print("Title:",self.title)
        print("Author:",self.author)
class Python(Book):
    def __init__(self, name, title, author,price,no_of_pages):
        super().__init__(name, title, author,)
        self.price=price
        self.no_of_pages=no_of_pages
    def displayinfo(self):
        print("Publisher:",self.name)
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",self.price)
        print("No of pages:",self.no_of_pages)

#py_book=Python(name="fsgsf",title="fgggfg",author="sgfsgfg",price=7878,no_of_pages=534)    
py_book=Python(
    name=input("Enter name:"),
    author=input("Enter author:"),
    title=input("Enter title:"),
    price=int(input("enter price:")),
    no_of_pages=int(input("Enter pages:"))
)
py_book.displayinfo()