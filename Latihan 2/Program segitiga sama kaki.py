print("Program segitiga sama kaki")
i = int(input("Masukkan tinggi :"))
row = i
s = ""
while row >= 0 :
    col = row
    while col >0:
        s = s + "  "
        col -= 1
    l = 1
    while l < (i - (row - 1)):
        s = s + "* "
        l += 1
    r = 1
    while r < l -1 :
        s = s + "* "
        r +=1
    s = s + "\n\n"
    row -=1
print(s)
