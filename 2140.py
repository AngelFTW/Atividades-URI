while True:
  x, y = input().split(' ')
  x = int(x)
  y = int(y)

  if x == 0 or y == 0:
    break;

  tr = y - x
  notas = [2,5,10,20,50,100]

  possible = False

  for i in range(len(notas)):
    for k in range(len(notas)):
      if notas[i] + notas[k] == tr:
        possible = True

  if possible: 
    print("possible")
  else: 
    print("impossible")