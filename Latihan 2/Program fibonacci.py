print("Program Fibonacci(15)")
a = 0
b = 1
print(a)
print(b)
n = 3
while (n <= 15):
    c = a + b
    a = b
    b = c
    print(b)
    n += 1
print("Selesai")