from time import perf_counter
from numpy import ones
from scipy.linalg import solve, inv
from numpy import float32
from laplaciana import laplaciana
#Esta importacion de laplaciana me tira error, pero sin esta funciona, porlo que debe venir integrada


memoria0=[]
tiempo0=[]
tamaño0=[]

i=0
while i<10:
    M=[2,3,5,7,10,12,15,20,30,40,50,70,100,150,200,300,500,750,1000,1800,2500,4000]
    for j in M:     
        t1 = perf_counter()
        A=laplaciana(j, dtype=float32)
        b=ones(j)
        
        t2 = perf_counter()
        Am1=inv(A)*b
        
        m = A.nbytes + Am1.nbytes 
        dt_calculo = t2-t1
        
        memoria0.append(m)
        tiempo0.append(dt_calculo)
        tamaño0.append(j)
        
        print (f"memoria = {m} bytes")
        print(f"dt_calculo = {dt_calculo} s")
        print (f"tamaño M = {j}")
        print ()
    i+=1


memoria1=[]
tiempo1=[]
tamaño1=[]

i=0
while i<10:
    M=[2,3,5,7,10,12,15,20,30,40,50,70,100,150,200,300,500,750,1000,1800,2500,4000]
    for j in M:     
        t1 = perf_counter()
        A=laplaciana(j, dtype=float32)
        b=ones(j)
        
        t2 = perf_counter()
        Am1=solve(A,b)
        
        m = A.nbytes + Am1.nbytes 
        dt_calculo = t2-t1
        
        memoria1.append(m)
        tiempo1.append(dt_calculo)
        tamaño1.append(j)
        
        print (f"memoria = {m} bytes")
        print(f"dt_calculo = {dt_calculo} s")
        print (f"tamaño M = {j}")
        print ()
    i+=1

memoria2=[]
tiempo2=[]
tamaño2=[]

i=0
while i<10:
    M=[2,3,5,7,10,12,15,20,30,40,50,70,100,150,200,300,500,750,1000,1800,2500,4000]
    for j in M:     
        t1 = perf_counter()
        A=laplaciana(j, dtype=float32)
        b=ones(j)
        
        t2 = perf_counter()
        Am1=solve(A,b,assume_a="pos")
        
        m = A.nbytes + Am1.nbytes 
        dt_calculo = t2-t1
        
        memoria2.append(m)
        tiempo2.append(dt_calculo)
        tamaño2.append(j)
        
        print (f"memoria = {m} bytes")
        print(f"dt_calculo = {dt_calculo} s")
        print (f"tamaño M = {j}")
        print ()
    i+=1

memoria3=[]
tiempo3=[]
tamaño3=[]

i=0
while i<10:
    M=[2,3,5,7,10,12,15,20,30,40,50,70,100,150,200,300,500,750,1000,1800,2500,4000]
    for j in M:     
        t1 = perf_counter()
        A=laplaciana(j, dtype=float32)
        b=ones(j)
        
        t2 = perf_counter()
        Am1=solve(A,b, assume_a="sym")
        
        m = A.nbytes + Am1.nbytes 
        dt_calculo = t2-t1
        
        memoria3.append(m)
        tiempo3.append(dt_calculo)
        tamaño3.append(j)
        
        print (f"memoria = {m} bytes")
        print(f"dt_calculo = {dt_calculo} s")
        print (f"tamaño M = {j}")
        print ()
    i+=1

memoria4=[]
tiempo4=[]
tamaño4=[]

i=0
while i<10:
    M=[2,3,5,7,10,12,15,20,30,40,50,70,100,150,200,300,500,750,1000,1800,2500,4000]
    for j in M:     
        t1 = perf_counter()
        A=laplaciana(j, dtype=float32)
        b=ones(j)
        
        t2 = perf_counter()
        Am1=solve(A,b, overwrite_a=True)
        
        m = A.nbytes + Am1.nbytes 
        dt_calculo = t2-t1
        
        memoria4.append(m)
        tiempo4.append(dt_calculo)
        tamaño4.append(j)
        
        print (f"memoria = {m} bytes")
        print(f"dt_calculo = {dt_calculo} s")
        print (f"tamaño M = {j}")
        print ()
    i+=1
    
memoria5=[]
tiempo5=[]
tamaño5=[]

i=0
while i<10:
    M=[2,3,5,7,10,12,15,20,30,40,50,70,100,150,200,300,500,750,1000,1800,2500,4000]
    for j in M:     
        t1 = perf_counter()
        A=laplaciana(j, dtype=float32)
        b=ones(j)
        
        t2 = perf_counter()
        Am1=solve(A,b, overwrite_b=True)
        
        m = A.nbytes + Am1.nbytes 
        dt_calculo = t2-t1
        
        memoria5.append(m)
        tiempo5.append(dt_calculo)
        tamaño5.append(j)
        
        print (f"memoria = {m} bytes")
        print(f"dt_calculo = {dt_calculo} s")
        print (f"tamaño M = {j}")
        print ()
    i+=1

memoria6=[]
tiempo6=[]
tamaño6=[]

i=0
while i<10:
    M=[2,3,5,7,10,12,15,20,30,40,50,70,100,150,200,300,500,750,1000,1800,2500,4000]
    for j in M:     
        t1 = perf_counter()
        A=laplaciana(j, dtype=float32)
        b=ones(j)
        
        t2 = perf_counter()
        Am1=solve(A,b, overwrite_a=True, overwrite_b=True)
        
        m = A.nbytes + Am1.nbytes 
        dt_calculo = t2-t1
        
        memoria6.append(m)
        tiempo6.append(dt_calculo)
        tamaño6.append(j)
        
        print (f"memoria = {m} bytes")
        print(f"dt_calculo = {dt_calculo} s")
        print (f"tamaño M = {j}")
        print ()
    i+=1
    
arch = open("Caso A.1 con float32 (simple).txt", "w")
arch.write("Tiempo de calculo(s)   Tamaño matriz \n")
a = 0
while a < len(tamaño0):
    arch.write(f"{tiempo0[a]}     {tamaño0[a]} \n")
    a+=1
arch.close()


arch = open("Caso A.2 con float32 (simple).txt", "w")
arch.write("Tiempo de calculo(s)   Tamaño matriz \n")
b = 0
while b < len(tiempo1):
    arch.write(f"{tiempo1[b]}     {tamaño1[b]} \n")
    b+=1
arch.close()


arch = open("Caso A.3 con float32 (simple).txt", "w")
arch.write("Tiempo de calculo(s)   Tamaño matriz \n")
c = 0
while c < len(tamaño2):
    arch.write(f"{tiempo2[c]}     {tamaño2[c]} \n")
    c+=1    
arch.close()


arch = open("Caso A.4 con float32 (simple).txt", "w")
arch.write("Tiempo de calculo(s)   Tamaño matriz \n")
d = 0
while d < len(tamaño3):
    arch.write(f"{tiempo3[d]}     {tamaño3[d]} \n")
    d+=1
arch.close()


arch = open("Caso A.5 con float32 (simple).txt", "w")
arch.write("Tiempo de calculo(s)   Tamaño matriz \n")
e = 0
while e < len(tiempo4):
    arch.write(f"{tiempo4[e]}     {tamaño4[e]} \n")
    e+=1
arch.close()


arch = open("Caso A.6 con float32 (simple).txt", "w")
arch.write("Tiempo de calculo(s)   Tamaño matriz \n")
f = 0
while f < len(tamaño5):
    arch.write(f"{tiempo5[f]}     {tamaño5[f]} \n")
    f+=1      
arch.close()


arch = open("Caso A.7 con float32 (simple).txt", "w")
arch.write("Tiempo de calculo(s)   Tamaño matriz \n")
g = 0
while g < len(tamaño6):
    arch.write(f"{tiempo6[g]}     {tamaño6[g]} \n")
    g+=1       
    
arch.close()