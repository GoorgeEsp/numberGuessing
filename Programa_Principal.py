import random
import math
from Funciones_Dimensiones import *
from Funciones_Pistas import *

# Print introduccion game
introduction()

# Initializating number of trys
trys = 0
trysForClue = 0

# Initializating clues
typeClues = 4
cluesUsed = 0

# Initializating score
# Without depending on range, everyone will start with 100 points
# Depending on probability and clues showed, score will go decrease faster
score = 100

# Asking if player want clues
wantClues = askForClues()
numberDigitsAlready = False

#Initializating lists to empty
numbersTryed = []
dividerForUser = []

#Initializating Guess to None to enter while and wait for answer
guess = None

# Taking Inputs
lower = selectLower()
upper = selectUpper(lower)
range = upper - lower
default = 100/range
dividersShowed = False
defaultDividers = 0

# Taking random number to search
number = random.randint(lower, upper + 1)

# Getting dividers for number to guess in case user wants clues
if wantClues:
	dividers = getDividers(number)

while guess != number and score > 0:
	if(wantClues == True):
		if trysForClue >= 3:	#Every 3 times user trys to guess number, option to get a clue appears
			answerClue = input('¿Le gustaria recibir una pista?>(y/n):')
			trysForClue = 0
			if(answerClue == 'y'):
				cluesUsed += 1
				score += -2*default
				typeClue = random.randint(1, typeClues)
				if typeClue == 1:
					dimension = upperDimension(number, upper)
					print("El número que se busca se encuentra en el rango [{0} - {1}]".format(lower, dimension))
					upper = dimension
					range = newDimension(lower, upper, numbersTryed)
					default = 100/range
				if typeClue == 2:
					dimension = lowerDimension(lower, number)
					lower = dimension
					print("El número que se busca se encuentra en el rango [{0} - {1}]".format(lower, upper))
					range = newDimension(lower, upper, numbersTryed)
					default = 100/range
				if typeClue == 3:
					dividersShowed = True
					aux = random.choice(dividers)
					defaultDividers = score/round(upper//aux)
					dividerForUser.append(aux)
					print("Sabemos que el número tiene esto/s divisores: {0}".format(dividerForUser))
				if typeClue == 4:
					if(numberDigitsAlready == False):
						print("El número contiene {0} digitos".format(digitos(number)))
						numberDigitsAlready = True
					else:
						print("La suma de los digitos del número son {0}".format(suma(number)))
						typeClues += 1
				print("Puntuación actual: {0:.2f}".format(score))

	guess = askForGuess(lower, upper)
	if guess >= lower and guess <= upper:
		if guess == number:
			trys+=1
			print()
			print('Lo has logrado! Has empleado {0} intentos'.format(trys))
			if wantClues:
				print('Has recibido {0} pistas'.format(cluesUsed))
			print("Puntuación final: {0:.2f}".format(score))
			break
		if guess in numbersTryed:
			print("Ya has dicho ese número prueba con otro.")
		else:
			if dividersShowed == False:
				score += -default
			if dividersShowed == True:
				score += -defaultDividers
			trysForClue+=1
			trys+=1
			range += -1
			print('Has fallado! Intentalo de nuevo.')
			numbersTryed.append(guess)
			numbersTryed.sort()
			print("Puntuación actual: {0:.2f}".format(score))
	else:
		print('Error: El número introducido no se encuentra en el rango [{0} - {1}]'.format(lower, upper))

	print("Lista de número dichos: {0}".format(numbersTryed))

if(score <= 0):
	print()
	print("Has perdido!")
	print("Puntuación final: 0")
