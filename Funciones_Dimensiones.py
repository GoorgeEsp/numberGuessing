import random

# Returns a random limiter dimension upper
def upperDimension(number, upper):
	return random.randint(number + 1, upper)

# Returns a random limiter dimension lower
def lowerDimension(lower, number):
	return random.randint(lower + 1, number)

# User select lower range
def selectLower():
	aux = input("Introduzca límite inferior: ")
	while True:
		if(not aux.isdigit()):
			aux = input("Introduzca límite inferior: ")
		else:
			aux = int(aux)
			return aux

# User select upper range
def selectUpper(lower):
	aux = input("Introduzca límite superior: ")
	while True:
		if(not aux.isdigit()):
			aux = input("Introduzca límite superior: ")
		else:
			aux = int(aux)
			if aux <= lower:
				aux = input('Introduzca un número entre {0} y {1}: '.format(lower, upper))
			else: 
				return aux

# New dimension depending on numbers already said
def newDimension(lower, upper, list):
	dimension = upper - lower
	for n in list:
		if (n >= lower and n <= upper):
			dimension += -1
	return dimension

# Print introduction to game
def introduction():
	print("Hola, Bienvenido/a al juego GuessingNumber.")
	print("El objetivo de este juego es adivinar un número dentro del rango que tu elijas.")
	print("Se podrán recibir pistas. En caso de activarlas y aceptarlas cada pista reducirá tu puntuación")
	print("Cada intento reduce la puntuación de forma proporcional.")
	print("El objetivo es adivinar el numero con la mayor puntuación posible. ¡Suerte!")
	print()