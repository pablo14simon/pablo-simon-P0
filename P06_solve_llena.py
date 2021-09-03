import numpy as np
from numpy import ones
#from laplaciana import laplaciana
from time import perf_counter
import scipy.sparse as sparse
import scipy.sparse.linalg as lin
from scipy.linalg import solve
from numpy import double

from numpy import zeros

def laplaciana(M, dtype):
    A=zeros((M,M), dtype=dtype)
    for i in range(M):
        A[i,i]=2
        for j in range(max(0,i-2),i):
            if abs(i-j)==1:
                A[i,j]=-1
                A[j,i]=-1
                
    return(A)

def matriz_laplaciana(M, t=double):
    e=np.eye(M)-np.eye(M,M,1)
    return t(e+e.T)


ensamblaje=[]
calculo=[]
tamaño=[]

i=0
while i<10:
    M=[2,3,5,7,10,12,15,20,30,40,50,70,100,150,200,300,500,750,1000,1800,2500,4000]
    for j in M:     
        t1 = perf_counter()
        A=matriz_laplaciana(j,double)
        b=ones(j, dtype=double)
        
        t2 = perf_counter()
        dt_ensamblaje = t2-t1
        
        t3=perf_counter()
        x=solve(A,b)
        
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

arch = open("Caso_solve_llena.txt", "w")
x = 0
arch.write("Tiempo de ensamblaje(s)     Tiempo en calcular(s)     Tamaño matriz \n")
while x < len(ensamblaje):
    arch.write(f"{ensamblaje[x]}   {calculo[x]}   {tamaño[x]} \n")
    x+=1
    
arch.close()
