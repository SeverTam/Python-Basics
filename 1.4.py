a = int(input("Введите число: "))
b = 0
c = 0
while a > 0:
    b = a % 10
    if b > c:
        c = b
    a = a // 10
print(c)



#print(len(str(a)))
