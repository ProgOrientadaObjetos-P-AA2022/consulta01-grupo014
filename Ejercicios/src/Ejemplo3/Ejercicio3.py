def main():
 dolares = input ("Cuantos dolares: ")
 interes = input ("Cuanto interes: ")
 interes = float(interes)
 anos = input ("Cantidad de años: ")
 print ""

 resultado = calculo (dolares, interes, anos)
 print "Cuando pasen", anos, u"años, con un", interes, u"de interes, usted habrá generado", resultado, "dolares."

def calculo (dinero, inte, cant_anos):
 x =dinero * ((1 + inte/100) **cant_anos)
 return x

main()