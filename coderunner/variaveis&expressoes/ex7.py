notas = (input())
pesos = (input())
sn = notas.split()
sp = pesos.split()
media = (float(sn[0]) * float(sp[0]) + float(sn[1]) * float(sp[1]) + float(sn[2]) * float(sp[2])) / (float(sp[0]) + float(sp[1]) + float(sp[2]))
print(f'{media:.6f}')