print("Program Kalkulator")
Bit1 = float(input("Masukkan angka pertama : "))
operator = input("masukkan operator (+,-,*,/,**,%) : ")
Bit2 = float(input("Masukkan angka kedua   : "))

if operator == "+" :
    print(Bit1,"+",Bit2,"=",Bit1 + Bit2)
elif operator == "-" :
    print(Bit1,"-",Bit2,"=",Bit1 - Bit2)
elif operator == "*" :
    print(Bit1,"*",Bit2,"=",Bit1 * Bit2)
elif operator == "/" :
    print(Bit1,"/",Bit2,"=",Bit1 / Bit2)
elif operator == "**" :
    print(Bit1,"^",Bit2,"=",Bit1 ** Bit2)
elif operator == "%" :
    print(Bit1,"%",Bit2,"=",Bit1 % Bit2)
else :
    print("operator yang anda masukkan salah,mohon cek kembali inputan anda")