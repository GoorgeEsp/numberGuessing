import random
import math

def upperDimension(number, upper):
	return random.randint(number + 1, upper)

def lowerDimension(lower, number):
	return random.randint(lower + 1, number)

def suma_digitos(n):
    sol = 0
    for i in str(n):
        sol += int(i)
    return sol

def digitos(n):
    sol = 0
    for i in str(n):
        sol += 1
    return sol

def suma(n):
    a = suma_digitos(n)
    while a > 9:
        a = suma_digitos(a)
    return a

# Initializating number of guesses
score = 0

# Taking Inputs
lower_selected = False; upper_selected = False
while not lower_selected:
	lower = input("Introduzca límite inferior: ")
	if lower.isdigit():
		lower = int(lower)
		if lower > 0:
			lower_selected = True

while not upper_selected:
	upper = input("Introduzca límite inferior: ")
	if upper.isdigit():
		upper = int(upper)
		if upper > lower:
			upper_selected = True

# Taking random number to search
number = random.randint(lower, upper + 1)
lista = []
divisores = []
for i in range(2, number + 1):
	if number%i == 0:
		divisores.append(i)
divisoresSabidos = []
guess = None
intentos = 0
intentosPista = 0
while guess != number:
	if trys >= 3:
		answerClue = input('¿Le gustaria recibir una pista?>(y/n):')
					intentosPista = 0
		if(answerClue == 'y'):
			typeClue = random.randint(1, 4)
			if typeClue == 1:
				dimension = upperDimension(number, upper)
				print("El número que se busca se encuentra en el rango [{0} - {1}]".format(lower, dimension))
				upper = dimension
			if typeClue == 2:
				dimension = lowerDimension(lower, number)
				print("El número que se busca se encuentra en el rango [{0} - {1}]".format(dimension, upper))
				lower = dimension
			if typeClue == 3:
				aux = random.choice(divisores)
				divisoresSabidos.append(aux)
				divisores.remove(aux)
				print("Sabemos que el número tiene esto/s divisores: {0}".format(divisoresSabidos))
			if typeClue == 4:
				print("El número contiene {0} digitos".format(digitos(number)))
			if typeClue == 5:
				print("La suma de los digitos del número son {0}".format(suma(number)))
	guess = input('Introduzca un número entre {0} y {1}: '.format(lower, upper))
	if guess.isdigit():
		guess = int(guess)

	if guess >= lower and guess <= upper:
		if guess == number:
			intentos+=1
			print('Lo has logrado! Has empleado {0} intentos'.format(intentos))
			break
		if guess in lista:
			intentosPista+=1
			intentos+=1
			print("Ya has dicho ese número prueba con otro.")
		else:
			print('Has fallado! Intentalo de nuevo.')
			lista.append(guess)
			lista.sort()
	else:
		print('Error: El número introducido no se encuentra en el rango [{0} - {1}]'.format(lower, upper))
	
	print("Lista de número dichos: {0}".format(lista))