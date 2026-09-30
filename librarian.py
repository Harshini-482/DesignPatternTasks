from user import *
class Librarian(User):


    def _init__(self,name,contact_info,employee_number):
        super().__init__(name,contact_info)
        self.__employee_number=employee_number

    def display_dashboard(self):
        print("---Librarian Dashboard---")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.__employee_number}")

    def can_barrow_books(self):
        return True

    def add_new_book(self):
        pass

    def remove_book(self):
        pass
