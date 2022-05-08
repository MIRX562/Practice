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
        print("pass ",i+1," ",input_list)

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
        print("pass",i+1," :",input_list,)

a = [5,1,2,4,9,3,7,0,8,6]

print("Sebelum Sorting = ",a)

print("\nKeatas (Ascending)")
bubble_sort_asc(a)

print("\nKebawah (Descending)")
bubble_sort_dsc(a)