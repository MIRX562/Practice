print("Program sorting data dengan metode bubble sort")

def bubble_sort_asc (init):
    # x sebagai pannjang list
    x = len(init)
    # looping sebanyak x-1
    for i in range(x-1):
        # memreriksa tiap elemen list
        for j in range(0, x-i-1):
            # menukar posisi jika ditemukan elemen yanng lebih besar
            if init[j] > init[j+1]:
                init[j], init[j+1] = init[j+1], init[j]
    return print(init)

def bubble_sort_dsc (init):
    # x sebagai pannjang list
    x = len(init)
    # looping sebanyak x-1
    for i in range(x-1):
        # memreriksa tiap elemen list
        for j in range(0, x-i-1):
            # menukar posisi jika ditemukan elemen yanng lebih kecil
            if init[j] < init[j+1]:
                init[j], init[j+1] = init[j+1], init[j]
    return print(init)
#mengulang hingga ada input break
while True :
    print(
        "\n<--Menu--> :\n",
        "1. Demo(Contoh)\n",
        "2. Input data manual\n",
        "9. Exit"
    )
    menu = input("   Pilih : ")
    if menu == "1":
        a = [5,1,2,4,9,3,7,0,8,6]
        print("\nsebelum sorting : ",a)
        print("\nsetelah sorting :")
        print("keatas(ascending) : ")
        bubble_sort_asc(a),
        print("\nkebawah(descending) : ")
        bubble_sort_dsc(a)
    
    elif menu == "2":
        x =[]
        n = int(input("banyak data :"))
        for i in range(n):
            y = input("Data :")
            x.append(y)
        
        print("\nList Input =",x)
        print("\nAscending :")
        bubble_sort_asc(x)
        print("\nDescending :")
        bubble_sort_dsc(x)

    elif menu == "9":
        break
    else :
        print("input salah!")