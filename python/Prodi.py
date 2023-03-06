from Course import Course
from Mahasiswa import Mahasiswa
from Dosen import Dosen

class Prodi:
    __namaprodi = ""
    __kodeprodi = ""
    __courses = Course()
    __mhs = Mahasiswa()
    __dsn = Dosen()

    def __init__(self,  namaprodi = "", kodeprodi = "", courses = Course(), mhs = Mahasiswa(), dsn = Dosen()): 
        self.__namaprodi = namaprodi
        self.__kodeprodi = kodeprodi
        self.__courses = courses
        self.__mhs = mhs
        self.__dsn = dsn
    
    def get_namaprodi(self):
        return self.__namaprodi
    def set_namaprodi(self, namaprodi):
        self.__namaprodi = namaprodi
    
    def get_kodeprodi(self):
        return self.__kodeprodi
    def set_kodeprodi(self, kodeprodi):
        self.__kodeprodi = kodeprodi

    def get_couses(self):
        return self.__courses
    def set_couses(self, couses):
        self.__courses = couses

    def get_mhs(self):
        return self.__mhs
    def set_mhs(self, mhs):
        self.__mhs = mhs
    
    def get_dsn(self):
        return self.__dsn
    def set_dsn(self, dsn):
        self.__dsn = dsn