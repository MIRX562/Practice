print("Program Indeks Nilai Mahasiswa\n")
def ind (Name,Score):
    print("Berikut Adalah Indeks Nilai Anda  ")
    print("Nama              :",Name)
    if (Score >= 85):
        ind = "A"
    elif (Score >= 70):
        ind = "B"
    elif (Score >= 55):
        ind = "C"
    elif (Score >= 40):
        ind = "D"
    elif (Score >= 0):
        ind = "E"
    print("Indeks Nilai anda :",ind)
    if Score>=55 :
        stat = "Lulus"
    elif Score>=0 :
        stat = "Tidak Lulus"
    print("Status            :",stat)

nama = input("Masukkan nama anda : ")
nilai= float(input("Masukkan Nilai : "))
ind(nama,nilai)