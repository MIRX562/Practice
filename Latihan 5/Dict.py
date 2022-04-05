print("\ncontoh1")
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): 
    dic4.update(d)
    print(dic4)

print("\ncontoh2")
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
cek_angka= 3
if cek_angka in d:
    print(cek_angka,' tersedia dalam dictionary')
else:
    print(cek_angka,'tidak tersedia dalam dictionary')
    
print("\ncontoh3")
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)