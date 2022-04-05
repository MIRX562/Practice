# menddeklarasikan list untuk sebuah ID 
# satu ID terdiri dari lima list
# data sebuah ID akan disimpan dengan nomor index yang sama di setiap listnya
nama          = []
nim           = []
tanggal_lahir = []
jenis_kelamin = []
prodi         = []
menu = 0

# pengulangan untuk mengulang program dan akan berhenti saat syntax break dijalankan
while True:
    # menampilkan pilihan
    print (
        "-----------------------------",
        "\n1. Mencetak list ID yang terdaftar",
        "\n2. Menambahkan ID ke dalam list",
        "\n3. Menghapus ID dari list",
        "\n4. Mengubah data sebuah ID dalam list",
        "\n9. Keluar")
    # meminta input menu
    menu = input("Pilih Menu : ")
    print()
    # menu 1
    if menu == "1":
        cur = 0
        # mengecek apakah ada isi dalam list
        if len(nama) > 0 : 
            # perulangan untuk menampilkan semua data yang ada dalam  list
            while cur < len(nama):
                print ("ID",nama[cur],"\n" ,
                "Nama           : ",nama[cur],"\n",
                "NIM            : ",nim[cur],"\n",
                "Tanggal Lahir  : ",tanggal_lahir[cur],"\n",
                "jenis kelamin  : ",jenis_kelamin[cur],"\n",
                "Prodi          : ",prodi[cur],"\n\n")
                cur = cur + 1
        # jika list kosong
        else :
          print ("List Masih Kosong")
    # menu 2
    elif menu == "2":
        # meminta banyak input data yang dinginkan
        t = int(input("banyak input : "))
        i = 0
        # mengulang penginputan data sebanyak t kali
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
    # menu 3
    elif menu == "3":
        # masukan data untuk mencari id
        d = input("Masukkan data dari ID yang ingin dihapus : ")
        # deklarasi fungsi hap untuk menghapus isi dalam setiap list yang berindex sama
        def hap(x) :   
            del nama[x]
            del nim[x]
            del tanggal_lahir[x]
            del jenis_kelamin[x]
            del prodi[x]
        #mengecek apakah data yang dimasukkan ada, jika ada maka data dengan index yang sama disetiap list akan dihapus menggunakan fungsi hap
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
        # jika data yang diinpuutkan tidak ditemukan
        else:
            print(d,"tidak  ditemukan")
    # menu 4
    elif menu == "4":
        # masukan data untuk mencari id
        u=input("masukkan nama ID yang ingin di edit : ")
        # memeriksa apakah data yang dicari ada
        if u in nama:
            i=nama.index(u)
            print("Pilih data yang ingin di edit")
            # menampilkan data yang bisa diedit
            print(
                "1. Nama           : ",nama[i],
                "\n2. NIM            : ",nim[i],
                "\n3. Tanggal Lahir  : ",tanggal_lahir[i],
                "\n4. jenis kelamin  : ",jenis_kelamin[i],
                "\n5. Prodi          : ",prodi[i],
                "\n9. Batal")
            # mengupdate data sesuaii pilihan 
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
        # jika data yang dicari tidak ada
        else:
            print(u,"tidak ditemukan")
    # menu untuk menghentikann perulangan dan sekaligus menghentikan program
    elif menu == "9":
        break

    else :
        print("Pillihan anda salah, mohon cek kembali pilihan anda")