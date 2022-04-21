# deklarasi fungsi fpb
def fpb(a,b):
    # mereturn hasil fpb
    if b==0:
        return a
    else:
        # melakukan rekursi untuk mencari fpb
        # menggunakan  metode euler
        return fpb(b,a%b)
# menampilkan output program
x = fpb(13,23)
print(x)