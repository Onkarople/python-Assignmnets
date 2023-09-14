#

class BookStore:
    NoofBooks=0
    def __init__(self,name,author):
        self.Name=name
        self.Author=author
        BookStore.NoofBooks=BookStore.NoofBooks+1
        
    

    def Display(self):
        print("Name of Book is:",self.Name)
        print("Author of Book is :",self.Author)
        print("Number of Books is :",BookStore.NoofBooks)
    





def main():
    obj1=BookStore("Linux Programming","Rpbert Love")
    obj1.Display()

    obj2=BookStore("C programming","Dennis Ritche")
    obj2.Display()

if __name__ == "__main__":
    main()