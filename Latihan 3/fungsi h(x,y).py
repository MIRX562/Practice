print("Program Fungsi h(x,y) = 3x - y + xy\n")
def h(x,y):
    z = (3 * x) - y + (x * y)
    print("h(",x,",",y,") =",z,"\n")

i = int(input("Masukkan nilai x : "))
j = int(input("Masukkan nilai y : "))
h(i,j)