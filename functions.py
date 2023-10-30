import random

def randomWord():
    consonantes_minus=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    consonantes_mayus=['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    vocales=['a','e','i','o','u']

    palabra = (consonantes_mayus[random.randint(0,len(consonantes_mayus)-1)]+vocales[random.randint(0,len(vocales))-1]+consonantes_minus[random.randint(0,len(consonantes_minus))-1]+vocales[random.randint(0,len(vocales))-1]+consonantes_minus[random.randint(0,len(consonantes_minus))-1]+vocales[random.randint(0,len(vocales))-1])

    return palabra