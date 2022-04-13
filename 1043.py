linha = input().split(" ")
A = float(linha[0])
B = float(linha[1])
C = float(linha[2])
if (B - C) < A < B + C and (A - C) < B < A + C and (A - B) < C < A + B:
  Perimetro = A + B + C
  print("Perimetro =",Perimetro)
else:
    Area = (A + B)*C/2
    print("Area =",Area)