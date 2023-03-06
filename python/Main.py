"""
Saya Alghaniyu Naufal Hamid NIM 2105673 mengerjakan Latihan 4
dalam mata kuliah Desain Pemrograman Berorientasi Objek 
untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan.
Aamiin.
"""

"""panggil semua file yang berisi class yang akan digunakan"""
from Mahasiswa import Mahasiswa
from Dosen import Dosen
from Course import Course
from Prodi import Prodi

"""buat var untuk menampung array output"""
mahasiswa = []
dosen = []
course = []
prodi = []

"""buat inputan dengan hardcode"""

mahasiswa.append(Mahasiswa("123","nopal gg gaming1","LAKI","UPI","FBTM","Nopalgg@upi.edu","2105673","3.7"))
mahasiswa.append(Mahasiswa("123","nopal gg gaming2","LAKI","UPI","FBTM","Nopalgg@upi.edu","2341453","3.7"))
mahasiswa.append(Mahasiswa("123","nopal gg gaming3","LAKI","UPI","FBTM","Nopalgg@upi.edu","2213456","3.7"))

dosen.append(Dosen("321","nopal jd dosen1","LAKI","UPI","FBTM","Nopalgg@upi.edu","210","S5 Tank", "jd Jungler"))
dosen.append(Dosen("321","nopal jd dosen2","LAKI","UPI","FBTM","Nopalgg@upi.edu","210","S5 Assasin", "jd roamer"))
dosen.append(Dosen("321","nopal jd dosen3","LAKI","UPI","FBTM","Nopalgg@upi.edu","210","S5 MM", "jd gold line"))

course.append(Course("IKJ1","Statistika Tapir"))
course.append(Course("IKJ2","Statistika Gajah"))
course.append(Course("IKJ3","Statistika Kucing"))

                                            #  ambil data dari input
prodi.append(Prodi("Ilmu Bahasa Tapir", "TPR", course, mahasiswa, dosen))

"""keluarkan output dengan menggunakan looping"""
for Prodi in prodi:
    print(Prodi.get_namaprodi(), "(Kode : ",Prodi.get_kodeprodi(),")")
    temp = 0
    print("Mata Kuliah: ")
    for j in course:
        print("- ", Prodi.get_couses()[temp].get_namamatkul())  
        temp += 1  
    temp = 0
    print("Dosen :")
    for j in course:
        print("- ", Prodi.get_dsn()[temp].get_nama())  
        temp += 1  
    temp = 0
    print("Mahasiswa: ")
    for j in course:
        print("- ", Prodi.get_mhs()[temp].get_nama())  
        temp += 1  

print()
print("Data Mahasiswa: ")
print("|nim | nama | gender | ipk |")
print()
i = 0
for Mahasiswa in mahasiswa:
    print("| ", Mahasiswa.get_nim()," | ", Mahasiswa.get_nama(), " | ", Mahasiswa.get_gender(), " | ", Mahasiswa.get_ipk(), " | ")
    i += 1

print()
print("Data Dosen: ")
print("|nip | nama | gender | pendidkan terahikr | keahlian |")
print()
i = 0
for Dosen in dosen:
    print("| ", Dosen.get_nip()," | ", Dosen.get_nama(), " | ", Dosen.get_gender(), " | ", Dosen.get_pendterakhir(), " | ", Dosen.get_keahlian(), " | ")
    i += 1

print()
print("Data Mata Kuliah: ")
print("| Kode | nama matakuliah |")
print() 
i = 0
for Course in course:
    print("| ", Course.get_kodematkul()," | ", Course.get_namamatkul(), " | ")
    i += 1