def bubble_sort_asc (inlist):
    # x sebagai pannjang list
    x = len(inlist)
    # looping sebanyak x-1
    for i in range(x-1):
        print("\npass ",i+1," ",inlist)
        # memreriksa tiap elemen list
        for j in range(0, x-i-1):
            # menukar posisi jika ditemukan elemen yanng lebih besar
            if inlist[j] > inlist[j+1]:
                print(inlist[j],">",inlist[j+1],"---> Tukar")
                inlist[j], inlist[j+1] = inlist[j+1], inlist[j]
            
        

a = [5,1,2,4,9,3,7,0,8,6]

print("Sebelum Sorting = ",a)

print("\nKeatas (Ascending)")
bubble_sort_asc(a)

