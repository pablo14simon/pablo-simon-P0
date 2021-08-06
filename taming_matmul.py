# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 19:56:50 2021

@author: Toshiba
"""

from numpy import zeros
from time import perf_counter
import sys
import numpy

print(sys.version)
print(numpy.version.version)

memoria=[]
tiempo=[]
tamaño=[]

i=0
while i<10:
    M=[2,3,5,7,10,12,15, 20, 30,40,50, 70, 100, 150, 200, 300, 500, 750, 1000, 1800, 2500, 4000]
    for j in M:
        A = zeros((j, j))+1
        B = zeros((j, j))+2
    
        t1 = perf_counter()
        C = A@B
        t2 = perf_counter()
    
        dt = t2 - t1
        m = A.nbytes + B.nbytes + C.nbytes

        memoria.append(m)
        tiempo.append(dt)
        tamaño.append(j)
        
        print (f"m = {m} bytes")
        print(f"dt = {dt} s")
        print (f"M = {j}")
        print ()
    i+=1

arch = open("Rendimiento.txt", "w")
x = 0
arch.write("Tiempo(s)   Memoria(bytes)    Tamaño \n")
while x < len(tiempo):
    arch.write(f"{tiempo[x]}   {memoria[x]}   {tamaño[x]} \n")
    x+=1
arch.close()
