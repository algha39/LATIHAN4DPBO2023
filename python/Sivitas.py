from Human import Human

class Sivitas(Human):
    __univ = ""
    __fakultas = ""
    __email = ""

    def __init__(self,nik = "" ,nama = "", gender = "", univ = "", fakultas = "", email = ""): 
        super().__init__(nik, nama, gender)
        self.__univ = univ
        self.__fakultas = fakultas
        self.__email = email
    
    def get_univ(self):
        return self.__univ
    def set_univ(self, univ):
        self.__univ = univ
    
    def get_fakultas(self):
        return self.__fakultas
    def set_fakultas(self, fakultas):
        self.__fakultas = fakultas

    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email