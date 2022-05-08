def bubble_sort (input_list):
    # x sebagai pannjang list
    x = len(input_list)
    # looping sebanyak x-1
    for i in range(x-1):
        # memreriksa tiap elemen list
        for j in range(0, x-i-1):
            # menukar posisi jika ditemukan elemen yanng lebih besar
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
    return print("Sesudah : ",input_list)

a = [5,1,2,4,9,3,7,0,8,6]
print("Sebelum : ",a)
bubble_sort(a)