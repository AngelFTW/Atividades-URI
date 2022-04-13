num = int(input())
contad = num
x = 1/6
frac = 1/6
if num == 0:
  print("%.10f"%(3))
else:
    while contad >= 2:
        frac = ( 1/ (6 + frac) )
        contad = contad - 1
    print("%.10f" %  (3 + frac))