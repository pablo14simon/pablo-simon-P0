from time import perf_counter
from numpy import zeros
from scipy.linalg import inv
from numpy import float128
#from laplaciana import laplaciana
#Esta importacion de laplaciana me tira error, pero sin esta funciona, porlo que debe venir integrada

memoria=[]
ensamblaje=[]
inversion=[]
tamaño=[]

i=0
while i<10:
    M=[2,3,5,7,10,12,15, 20,30,40,50, 70, 100, 150, 200, 300, 500, 750, 1000, 1800, 2500, 4000]
    for j in M:     
        t1 = perf_counter()
        A=laplaciana(j, dtype=float128)
        
        t2 = perf_counter()
        Am1=inv(A, overwrite_a=False)
        
        t3=perf_counter()
        
        m = A.nbytes + Am1.nbytes 
        dt_ensamblaje = t2-t1
        dt_inversion = t3-t2
        
        memoria.append(m)
        ensamblaje.append(dt_ensamblaje)
        inversion.append(dt_inversion)
        tamaño.append(j)
        
        print (f"memoria = {m} bytes")
        print(f"dt_inversion = {dt_inversion} s")
        print(f"dt_ensamblaje = {dt_ensamblaje} s")
        print (f"tamaño M = {j}")
        print ()
    i+=1

arch = open("timing_inv_caso_2_longdouble.txt", "w")
x = 0
arch.write("Tiempo en inversión(s)      Memoria(bytes)       Tamaño matriz \n")
while x < len(ensamblaje):
    arch.write(f"{inversion[x]}   {memoria[x]}   {tamaño[x]} \n")
    x+=1
arch.close()

