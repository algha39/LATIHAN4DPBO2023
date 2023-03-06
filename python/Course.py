class Course:
    __kodematkul = ""
    __namamatkul = ""

    def __init__(self,  kodematkul = "", namamatkul = ""): 
        self.__kodematkul = kodematkul
        self.__namamatkul = namamatkul
    
    def get_kodematkul(self):
        return self.__kodematkul
    def set_kodematkul(self, kodematkul):
        self.__kodematkul = kodematkul
    
    def get_namamatkul(self):
        return self.__namamatkul
    def set_namamatkul(self, namamatkul):
        self.__namamatkul = namamatkul