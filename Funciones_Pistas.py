# Returns sum of digits of a number
def suma_digitos(n):
    sol = 0
    for i in str(n):
        sol += int(i)
    return sol

# Returns number of digits of a number
def digitos(n):
    sol = 0
    for i in str(n):
        sol += 1
    return sol

# Returns sum of digits of a number
def suma(n):
    a = suma_digitos(n)
    while a > 9:
        a = suma_digitos(a)
    return a

# Returns a list with dividers of a number
def getDividers(numbero):
    dividers = []
    for i in range(2, numbero + 1):
        if numbero%i == 0:
            dividers.append(i)
    return dividers

# Ask for clues and return True if user wants clues actives
def askForClues():
    answerClues = input('¿Le gustaria habilitar las pistas durante la partida?>(y/n):')
    if(answerClues.lower() == 'y'):
        return True
    return False

# Asks por number to guess
def askForGuess(lower, upper):
    guess = input('Introduzca un número entre {0} y {1}: '.format(lower, upper))
    while True:
        if(not guess.isdigit()):
            guess = input('Introduzca un número entre {0} y {1}: '.format(lower, upper))
        else:
            guess = int(guess)
            if(guess < lower or guess > upper):
                guess = input('Introduzca un número entre {0} y {1}: '.format(lower, upper))
            else: 
                return guess