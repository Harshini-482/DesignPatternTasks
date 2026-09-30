from user import *

class Member(User):
    MAX_BORROW_LIMIT=5

    def __init__(self,name=None,contact_info=None):
        super().__init__(name,contact_info)
        self.__borrowed_book_count=0

    def display_dashboard(self):
        print("---Member Dashboard---")
        print(f"Name: {self.name}")
        print(f"Books borrowed: {self.__borrowed_book_count}")


    def can_barrow_books(self):
        return self.__borrowed_book_count< Member.MAX_BORROW_LIMIT

    def increment_borrow_count(self):
        self.__borrowed_book_count+=1

    def decrement_borrow_count(self):
        self.__borrowed_book_count-=1

    @property
    def get_borrowed_book_count(self):
        return self.__borrowed_book_count
    