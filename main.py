x = int(input("Give me a base: "))
n = int(input("Give me a power: "))

m = ""
for b in range(1,n+1): # 1,2,3,4....n+1
    m += str(x)+" x "
    
a = x**n
m += "= "+ str(a)

m = m.replace("x =","=")
print(m)