"""numero=5
suma=0

for i in range(1,numero+1):
    if i%2==0:
        suma+=i
    else:
        suma-=i

print(suma)"""

'''x=3
resultado=1

for i in range(1,5):
    if i%2==0:
        resultado*=x
    else:
        resultado+=x

print(resultado)'''

"""n=4
resultado=0
i=1
while i<=n:
    resultado+=i
    i*=2
print (resultado)"""

x=2
y=3
for i in range (1,4):
    x+=i
    for j in range (1,i+1):
        y+=j
print(x,y)