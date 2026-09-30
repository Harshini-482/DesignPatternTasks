from abc import ABC, abstractmethod
class User(ABC):

    __id_count=0
    __total_users=0

    def __init__(self,name=None,contact_info=None):
        User.__id_count+=1
        User.__total_users+=1
        self.__user_id="U_"+str(User.__id_count)
        self._name=name
        self.__contact_info=contact_info

    @property
    def user_id(self):
        return self.__user_id

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self,val):
        self.__name=val

    @property
    def contact_info(self):
        return self.__contact_info

    @contact_info.setter
    def contact_info(self,val):
        self.__contact_info=val
    


    @classmethod
    def get_totaluser(cls):
        return cls.__total_users

    @abstractmethod
    def display_dashboard(self):
        pass

    @abstractmethod
    def can_barrow_books(self):
        pass


       

        

    