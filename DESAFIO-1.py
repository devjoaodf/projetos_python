def recomendar_plano():
  consumo = float(input("Digite o valor em gb da sua média mensal: "))
  if  consumo <= 10:
    print("Plano Essencial Fibra - 50Mbps")
  elif consumo <= 20 >= 10:
    print("Plano Prata Fibra - 100Mbps")
  elif consumo >= 20:
    print("Plano Premium Fibra - 300Mbps")
    
while True:
  recomendar_plano()