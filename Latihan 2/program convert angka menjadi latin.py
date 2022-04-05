print("Program Pengubah angka ke latin(0-99)")
terbilang = [' ','Satu','Dua','Tiga','Empat','Lima','Enam','Tujuh',
'Delapan','Sembilan','Sepuluh','Sebelas']

inp=int(input("Masukkan angka (0-99) :"))
if inp == 0:
    print("Nol")
elif inp < 12:
    print(terbilang[inp])
elif inp < 20:
    print(terbilang[inp-10] + " Belas")
elif inp <= 99:
    print(terbilang[inp//10] + " Puluh " + terbilang[inp%10])
else:
    print("Angka yang anda masukkan salah!")