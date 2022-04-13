n = float(input())

if (0 <= n <= 1000000.00):
  
  n100 = n/100
  n50 = n%100/50
  n20 = n%50/20
  n10 = n%100%50%20/10
  n5 = n%10/5
  n2 = n%5/2
  n1 = n%100%50%20%10%5%2/1
  m50 = n%1/0.5
  m25 = n%0.5/0.25
  m10 = n%100%50%20%10%5%2%1%0.5%0.25/0.1
  m5 = n%100%50%20%10%5%2%1%0.5%0.25%0.1/0.05
  m1 = n%100%50%20%10%5%2%1%0.5%0.25%0.1%0.05/0.01+0.01

  print("NOTAS:")
  print("%d nota(s) de R$ 100.00" %n100)
  print("%d nota(s) de R$ 50.00" %n50)
  print("%d nota(s) de R$ 20.00" %n20)
  print("%d nota(s) de R$ 10.00" %n10)
  print("%d nota(s) de R$ 5.00" %n5)
  print("%d nota(s) de R$ 2.00" %n2)
  print("MOEDAS:")
  print("%d moeda(s) de R$ 1.00" %n1)
  print("%d moeda(s) de R$ 0.50" %m50)
  print("%d moeda(s) de R$ 0.25" %m25)
  print("%d moeda(s) de R$ 0.10" %m10)
  print("%d moeda(s) de R$ 0.05" %m5)
  print("%d moeda(s) de R$ 0.01" %m1)