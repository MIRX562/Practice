def bubble_sort (inlist):
    # x sebagai pannjang list
    x = len(inlist)
    # looping sebanyak x-1
    for i in range(x-1):
        # memreriksa tiap elemen list
        for j in range(0, x-i-1):
            # menukar posisi jika ditemukan elemen yang lebih besar
            if inlist[j] > inlist[j+1]:
                inlist[j], inlist[j+1] = inlist[j+1], inlist[j]
    return print("Sesudah : ",inlist)

a = [5,1,2,4,9,3,7,0,8,6]
print("Sebelum : ",a)
bubble_sort(a)