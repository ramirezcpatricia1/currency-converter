def conversor(tipo_pesos, valor_dolar): 
    pesos = input("cuantos pesos " + tipo_pesos + " tienes?: " )
    pesos = float(pesos)
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares+ "dolares")


menu = """
Bienvenido al conversor de monedas 馃馃挷馃挷
1= Pesos colombianos
2- Pesos argentinos
3- Pesos MExicanos
Elige una opci贸n: """

opci贸n = input(menu)

if opci贸n == '1':
    conversor("colombianos", 3875)
elif opci贸n == '2':
    conversor("argentinos", 65)
elif opci贸n == '3':
    conversor("mexicanos", 24)
else: 
    print('ingrese una opci贸n correcta porfavor')