i=1
 n = int(input("digite el valor de n"))
suma_notas=0
while i<=n:
    nota = float(input("digita tu nota"))
    suma_notas += nota
    i+=1
print("el promedio es ", suma_notas/n)
