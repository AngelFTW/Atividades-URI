def f(seg): 
    hora = seg / 3600
    seg %= 3600
    minu = seg / 60
    seg %= 60
      
    return "%d:%01d:%01d" % (hora, minu, seg) 
      
x = int(input())
print(f(x)) 