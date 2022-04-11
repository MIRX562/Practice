# deklarasi fungsi pembalik input
def reverse(msk):
    # mereturn input yang sudah dibalik
    if len(msk)==0:
        return msk
    # rekursi untuk membalikkan input
    else:
        # loop mengambil karakter pertama input dan menyimpannya
        # sehingga output akan mulai dari karakter terakhir
        # saat string input sudah kosong
        return reverse(msk[1:])+msk[0]
# meminta input dari user
x = input("Masukkan string : ")
# print kebalikannya dengan memanggil fungsi reverse
print ("kebalikannya : ")
print(reverse(x))