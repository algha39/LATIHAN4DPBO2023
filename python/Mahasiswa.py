from Sivitas import Sivitas

class Mahasiswa(Sivitas):
    __nim = ""
    __ipk = ""

    def __init__(self, nik = "",nama = "", gender = "",univ = "", fakultas = "", email = "", nim = "", ipk = ""): 
        super().__init__(nik,nama,gender,univ,fakultas,email)
        self.__nim = nim
        self.__ipk = ipk

    def get_nim(self):
        return self.__nim
    def set_nim(self, nim):
        self.__nim = nim

    def get_ipk(self):
        return self.__ipk
    def set_ipk(self, ipk):
        self.__ipk = ipk