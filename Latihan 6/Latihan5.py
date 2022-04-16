#mencarinilaiminimum
def nilai_minimal(list):
    nilai_terkecil= list[0]
    print(f'{list} -> {nilai_terkecil}')
    if len(list) > 1:
        # proses rekursif
        next_nilai_terkecil= nilai_minimal(list[1:])
        if next_nilai_terkecil< nilai_terkecil:
            nilai_terkecil= next_nilai_terkecil
        print(f'{list} -> {nilai_terkecil}')
    return nilai_terkecil

x =[1,2,3,4,5,6,7,8,9,0]
print("x = ",x,"\n")

nilai_minimal(x)