print("Program tahun kabisat\n")
def kab(a):
    if a%4==0:
        print(a,"adalah tahun kabisat\n")
    else:
        print(a,"bukanlah tahun kabisat\n")

i = int(input("Masukkan tahun :"))
kab(i)