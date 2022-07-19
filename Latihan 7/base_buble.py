from time import sleep
import os
def bubble_sort (inlist):
   
    x = len(inlist)
    tal = 0
    
    for i in range(x-1):
        # os.system('cls')
        print("\npass ",i+1," ")
        print(inlist)
        y = 0
        # print("\njumlah pengecekan :",tal,"\n")
        # sleep(1)
        for j in range(0, x-i-1):
            # os.system('cls')
            # print(inlist)
            if inlist[j] > inlist[j+1]:
                print(inlist[j],">",inlist[j+1],"---> Tukar")
                inlist[j], inlist[j+1] = inlist[j+1], inlist[j]
                y+=1
                # print(inlist)
            elif inlist[j] < inlist[j+1] :
                print(inlist[j],"<",inlist[j+1],"---> Tetap")
                # print(inlist)
            tal+=1
            # print("\njumlah pengecekan :",tal,"\n")
            
            # sleep(0.2)
        if y <= 0 :
             break
    return print("Sesudah : ",inlist)

a = [6,3,2,5,7,0]
print("Sebelum : ",a)
bubble_sort(a)
print("\nselesai")
