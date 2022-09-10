def conversor(tipo_pesos, valor_dolar): 
    pesos = input("cuantos pesos " + tipo_pesos + " tienes?: " )
    pesos = float(pesos)
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares+ "dolares")


menu = """
Bienvenido al conversor de monedas 🤑💲💲
1= Pesos colombianos
2- Pesos argentinos
3- Pesos MExicanos
Elige una opción: """

opción = input(menu)

if opción == '1':
    conversor("colombianos", 3875)
elif opción == '2':
    conversor("argentinos", 65)
elif opción == '3':
    conversor("mexicanos", 24)
else: 
    print('ingrese una opción correcta porfavor')