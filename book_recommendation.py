import os



class MyProj:
    def __init__(self):
        self.test = None
        self.book_list = []



    def run(self):
        with open("D:\Glorious Projects\\Python Practice\\book_affinity_project\\booklist.txt", "r") as list_of_books:
            for x in list_of_books:
                current_place = x[:-1]
                self.book_list.append(current_place)
        print(self.book_list)
            

            

if __name__ == "__main__":
    test = MyProj()
    test.run()

