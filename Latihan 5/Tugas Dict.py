print ("program game tebak-tebakan perlawanan kata (antonim)\n")
play=input("Bermain?(y/n) :")
if play=="y":
    src = {
        'aku':'kamu',
        'kita':'mereka',
        'panas':'dingin',
        'banyak':'sedikit',
        'murah':'mahal',
        'senang':'sedih',
        'mudah':'sulit',
        'sayang':'benci',
        'jernih':'keruh',
        'dosa':'pahala'}
    point=0
    for key, value in src.items():
        print("--------------------->")
        print(key)
        jawab=input("Jawaban :")
        if jawab in src.values():
             print("Benar")
             point=point+10
        else:
             print("Salah")
             print("jawaban yang benar : ",src[key])
             continue
    print("\nGame selesai")
    print("jawaban benar : ",int(point/10))
    print("jawaban salah : ",int(10-(point/10)))
    print("skor anda     : ",point,"\n")