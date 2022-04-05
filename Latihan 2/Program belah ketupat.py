
print("Program Belah Ketupat")
x = int(input("Masukkan Lebar : "))
row = x
s = ""
while row >= 0 :
    col = row
    while col > 0 :
        s = s + "  "
        col -= 1
    l = 1
    while l < (x - (row - 1)):
        s = s + "* "
        l += 1
    r = 1
    while r < l -1 :
        s = s + "* "
        r += 1
    s = s + "\n\n"
    row -= 1

row = 1 
while row <= x :
    col = row + 1
    while col > 1:
        s = s + "  "
        col -= 1
    l = 0
    while l < (x - row ):
        s = s + "* "
        l += 1
    r = l
    while r > 1 :
        s = s + "* "
        r -=1
    s = s + "\n\n"
    row +=1
print(s)