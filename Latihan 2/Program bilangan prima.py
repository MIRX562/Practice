print("Program Menampilkan Bilangan Prima dari 1-100")
a=2
while(a <= 100):
    b=2
    while(b <= (a/b)):
        if not(a%b):
            break
        b+=1
    if (b > a/b):
        print(a)
    a+=1
print("Selesai")