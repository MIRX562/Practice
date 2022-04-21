nama          = []
nim           = []
tanggal_lahir = []
jenis_kelamin = []
prodi         = []
menu = 0

while True:
    print (
        "-----------------------------",
        "\n1. Mencetak list ID yang terdaftar",
        "\n2. Menambahkan ID ke dalam list",
        "\n3. Menghapus ID dari list",
        "\n4. Mengubah data sebuah ID dalam list",
        "\n9. Keluar")
    menu = input("Pilih Menu : ")
    print()
 
    if menu == "1":
        current = 0
        
        if len(nama) > 0 : 
            while current < len(nama):
                print (
                "ID",nama[current],"\n" ,
                "Nama           : ",nama[current],"\n",
                "NIM            : ",nim[current],"\n",
                "Tanggal Lahir  : ",tanggal_lahir[current],"\n",
                "jenis kelamin  : ",jenis_kelamin[current],"\n",
                "Prodi          : ",prodi[current],"\n\n")
                current = current + 1

        else :
          print ("List Masih Kosong")
 
    elif menu == "2":
        t = int(input("banyak input : "))
        i = 0

        while(i < t):
            print("\nInput",i + 1)
            n = input("Masukkan Nama          : ")
            nama.append(n)
            o = input("Masukkan NIM           : ")
            nim.append(o)
            p = input("Masukkan Tanggal Lahir : ")
            tanggal_lahir.append(p)
            q = input("Masukkan Jenis Kelamin : ")
            jenis_kelamin.append(q)
            r = input("Masukkan Program Studi : ")
            prodi.append(r)
            i+=1

    elif menu == "3":
        d = input("Masukkan data dari ID yang ingin dihapus : ")

        def hap(x) :   
            del nama[x]
            del nim[x]
            del tanggal_lahir[x]
            del jenis_kelamin[x]
            del prodi[x]

        if d in nama:
            j = nama.index(d)
            hap(j)
        elif d in nim:
            j = nim.index(d)
            hap(j)
        elif d in tanggal_lahir:
            j = tanggal_lahir.index(d)
            hap(j)
        elif d in jenis_kelamin:
            j = jenis_kelamin.index(d)
            hap(j)
        elif d in prodi:
            j = prodi.index(d)
            hap(j)
        else:
            print(d,"tidak  ditemukan")
    
    elif menu == "4":
        u=input("masukkan nama ID yang ingin di edit : ")
        if u in nama:
            i=nama.index(u)
            print("Pilih data yang ingin di edit")

            print(
                "1. Nama           : ",nama[i],
                "\n2. NIM            : ",nim[i],
                "\n3. Tanggal Lahir  : ",tanggal_lahir[i],
                "\n4. jenis kelamin  : ",jenis_kelamin[i],
                "\n5. Prodi          : ",prodi[i],
                "\n9. Batal")

            while True:
                g = input("Pilih : ")
                print("")
                if g == "1":
                    k = input("Masukkan Nama baru : ")
                    nama[i] = k
                    break
                elif g == "2":
                    k = input("Masukkan NIM baru : ")
                    nim[i] = k
                    break
                elif g == "3":
                    k = input("Masukkan Tanggal Lahir baru : ")
                    tanggal_lahir[i] = k
                    break
                elif g == "4":
                    k = input("Masukkan Jenis Kelamin baru : ")
                    jenis_kelamin[i] = k
                    break
                elif g == "5":
                    k = input("Masukkan Program Studi baru : ")
                    prodi[i] = k
                    break
                elif g == "9":
                    break
                else :
                    print("Pilihan anda salah, coba lagi\n")

        else:
            print(u,"tidak ditemukan")

    elif menu == "9":
        break

    else :
        print("Pillihan anda salah, mohon cek kembali pilihan anda") 