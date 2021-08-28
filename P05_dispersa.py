import scipy.sparse as sparse
import scipy.sparse.linalg as lin
import numpy as np
from numpy import float64
from laplaciana import laplaciana
from time import perf_counter

def matriz_laplaciana(M, t=np.float64):
    e=np.eye(M)-np.eye(M,M,1)
    return t(e+e.T)

#Acsr=sparse.csr_matrix(A)
#Acsr=sparse.csc_matrix(A)
#Acsr=sparse.coo_matrix(A)
#Acsr=sparse.lil_matrix(A)


ensamblaje=[]
calculo=[]
tamaño=[]

i=0
while i<10:
    M=[2,3,5,7,10,12,15,20,30,40,50, 70, 100, 150, 200, 300, 500, 750, 1000, 1800, 2500, 4000]
    for j in M:     
        t1 = perf_counter()
        A=laplaciana(j, dtype=float64)
        B=laplaciana(j, dtype=float64)
        Acsr=sparse.csr_matrix(A)
        Bcsr=sparse.csr_matrix(B)
        
        t2 = perf_counter()
        dt_ensamblaje = t2-t1
        
        t3=perf_counter()
        Ccsr=Acsr@Bcsr
        
        t4=perf_counter()
        dt_calculo = t4-t3
        
        ensamblaje.append(dt_ensamblaje)
        calculo.append(dt_calculo)
        tamaño.append(j)
        
        print(f"dt_calculo = {dt_calculo} s")
        print(f"dt_ensamblaje = {dt_ensamblaje} s")
        print (f"tamaño M = {j}")
        print ()
    i+=1

arch = open("Caso_2_dispersa.txt", "w")
x = 0
arch.write("Tiempo de ensamblaje(s)     Tiempo en calcular(s)     Tamaño matriz \n")
while x < len(ensamblaje):
    arch.write(f"{ensamblaje[x]}   {calculo[x]}   {tamaño[x]} \n")
    x+=1
    
arch.close()