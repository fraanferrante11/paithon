from asyncore import read


RC= entero = int( input("Ingresar número de respuestas correctas: "))
RI= entero = int( input("Ingresar número de respuestas incorrectas: "))
RB= entero = int( input("Ingresar número de respuestas en blanco: "))

PRC= RC*3
PRI= RI*(-1)
PRB= RB*0
