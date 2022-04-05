
menu_item= 0
namelist= []
while menu_item!= 9:
    print ("-----------------------------")
    print ("1. Mencetaklist ID")
    print ("2. Menambahkan ID ")
    print ("3. Menghapus ID")
    print ("4. Mengubah data sebuah ID ")
    print ("9. Keluar")
    menu_item = int(input("Pilih menu: "))
    if menu_item== 1:
        current = 0
        if len(namelist) > 0 :
            while current < len(namelist):
                print (current,"." , namelist[current])
                current = current + 1
        else :
          print ("List Kosong")

    elif menu_item==2:
        t=int(input("banyak input :"))
        i=0
        while(i<t):
            n=input("masukkan nama : ")
            namelist.append(n)
            i+=1

    elif menu_item==3:
        d=input("Masukkan nama  yng ingin dihapus : ")
        if d in namelist:
            namelist.remove(d)
        else:
            print(d,"tidak  ditemukan")

    elif menu_item==4:
        u=input("masukkan nama yang ingin diubah : ")
        if u in namelist:
            i=namelist.index(u)
            n=input("nama baru : ")
            namelist[i] = n
        else:
            print(u,"tidak ditemukan")

    elif menu_item==9:
        break