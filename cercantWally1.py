
Alejandro Martínez Rodríguez <alejandro.martinez@iesjoandaustria.org>
dt., 31 de març 18:43 (fa 2 dies)
per a Sergi

import string
import random

#creació de la llista de simbols
#https://docs.python.org/2/library/string.html
simbols=list(string.printable)

def initLandscape(landscape):
    for i in range(100):
        landscape.append("")
    return landscape

def populateLandscape(landscape):
    wally = False
    for posicio in range(100):
        personatge = random.choice(simbols)
        if (personatge == "W"):
            if ("W" not in landscape):
                wally = True
                landscape[posicio] = personatge
        else:    
            landscape[posicio] = personatge
    
    if (not wally):
        #Assegurem que hi hagi en Wally
        landscape[random.randrange(100)] ="W"    
    return landscape

def whereIsWally(landscape,toFind):
    for pos in range(len(landscape)):
      if landscape[pos] == "W":
        posicio = pos+1
    #TODO
    #Completeu aquí el codi per fer la cerca de W (ally)
    return posicio

landscape=populateLandscape(initLandscape([]))
print(landscape)
print("Wally està en la posició "+str(whereIsWally(landscape,"W")))