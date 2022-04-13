linha = input().split(" ")

A = float(linha[0])
B = float(linha[1])

1<=A<=13
1<=B<=13

if A > B:
  print(int(A))

if B > A:
  print(int(B))

if A == B:
  print(int(A) or int(B))