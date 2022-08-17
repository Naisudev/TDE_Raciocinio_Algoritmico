alturaCilindro = float(input("Digite o valor da altura do tanque: "))
raioCilindro = float(input("Digite o valor do raio do tanque: "))
pi = 3.14
volumeCilindro = pi*(raioCilindro**2)*alturaCilindro
quantidadeLatas = volumeCilindro/15
custoLata = 50
custoTanque = quantidadeLatas*custoLata
print("O custo para pintar o tanque será de R$", custoTanque, "e você precisará de", quantidadeLatas,"latas.")
