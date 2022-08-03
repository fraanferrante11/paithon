from ast import Num
from asyncore import read
from multiprocessing.sharedctypes import Value
from turtle import distance

V= entero = int( input("Ingresar velocidad: "))
T= entero = int( input("Ingresar tiempo: "))

Dist = V * T

print (Dist)