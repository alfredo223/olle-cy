#Problema para hallar la suma de 2 numeros enteros
def suma(a,b):
    c=a+b
    return c
def resta(a,b):
    z=a-b
    return z
x=int(input("Ingrese el Primer Numero Entero: "))
y=int(input("Ingrese el Segundo NUmero Entero: "))
print("La suma de x e y es: {}".format(suma(x,y)))
print("La resta de x e y es: {}".format(resta(x,y)))
