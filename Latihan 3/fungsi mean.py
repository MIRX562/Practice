print("Program menghitung rata-rata\n")
def mean (n):
    hmp = []
    jml = 0
    for i in range(0,n):
        tmp = float(input("Masukkan data ke-%d: " % (i+1)))
        hmp.append(tmp)
        jml += hmp[i]
    print("rata-rata = ",jml/n)
x = int(input("Banyak data : "))
mean (x)