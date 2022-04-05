print("Program fungsi ganjil genap\n")

def odev(x):
    if x%2==0:
        print(x,"adalah bilangan genap\n")
    else :
        print(x,"adalah bilangan ganjil\n")

a = int(input("masukkan angka :"))
odev(a)