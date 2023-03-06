from Sivitas import Sivitas

class Dosen(Sivitas):
    __nip = ""
    __pendterakhir = ""
    __keahlian = ""

    def __init__(self,  nik = "", nama = "", gender = "",univ = "", fakultas = "", email = "", nip = "", pendterakhir = "", keahlian = ""): 
        super().__init__(nik, nama, gender, univ, fakultas, email)
        self.__nip = nip
        self.__pendterakhir = pendterakhir
        self.__keahlian = keahlian
    
    def get_nip(self):
        return self.__nip
    def set_nip(self, nip):
        self.__nip = nip
    
    def get_pendterakhir(self):
        return self.__pendterakhir
    def set_pendterakhir(self, pendterakhir):
        self.__pendterakhir = pendterakhir

    def get_keahlian(self):
        return self.__keahlian
    def set_keahlian(self, keahlian):
        self.__keahlian = keahlian