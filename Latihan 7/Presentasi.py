print("Program sorting data dengan metode bubble sort")

def bubble_sort_asc (input_list):
    # x sebagai pannjang list
    x = len(input_list)
    # looping sebanyak x-1
    for i in range(x-1):
        # memreriksa tiap elemen list
        for j in range(0, x-i-1):
            # menukar posisi jika ditemukan elemen yanng lebih besar
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
    return print(input_list)

def bubble_sort_dsc (input_list):
    # x sebagai pannjang list
    x = len(input_list)
    # looping sebanyak x-1
    for i in range(x-1):
        # memreriksa tiap elemen list
        for j in range(0, x-i-1):
            # menukar posisi jika ditemukan elemen yanng lebih kecil
            if input_list[j] < input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
    return print(input_list)

while True :
    print(
        "\n||-------------------Menu-------------------|| :\n",
        "  1. Demo(Contoh)\n",
        "  2. Input data manual\n",
        "  9. Exit"
    )
    menu = input("   Pilih : ")
    if menu == "1":
        a = [5,1,2,4,9,3,7,0,8,6]
        print("sebelum sorting : ",a,"\n",)
        print("setelah sorting :")
        print("keatas(ascending) : ")
        bubble_sort_asc(a),
        print("\nkebawah(descending) : ")
        bubble_sort_dsc(a)
    
    elif menu == "2":
        x =[]
        n = int(input("banyak data :"))
        for i in range(n):
            y = int(input("Data :"))
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