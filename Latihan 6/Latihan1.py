#program 6
def tampilkanAngka(batas, i= 1):
    prefix = '--' * (i-1)
    print(f'{prefix} Sebelum_rekursif({i})')
    if (i< batas):
        # di sinilahrekursifitasituterjadi
        tampilkanAngka(batas, i+ 1)
        print(f'{prefix} Setelah_rekursif({i})')
# memanggilfungsitampilkanAngka
# untukpertamakali
tampilkanAngka(5)