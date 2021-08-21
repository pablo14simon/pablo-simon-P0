from time import perf_counter
from numpy import ones
from scipy.linalg import eigh, inv
from numpy import float64
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
        A=laplaciana(j, dtype=float64)
        b=ones(j)
        
        t2 = perf_counter()
        #Am1=inv(A)*b
        w, h=eigh(A)
        
        #m = A.nbytes + Am1.nbytes 
        dt_calculo = t2-t1
        
        #memoria0.append(m)
        tiempo0.append(dt_calculo)
        tamaño0.append(j)
        
        #print (f"memoria = {m} bytes")
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
        A=laplaciana(j, dtype=float64)
        b=ones(j)
        
        t2 = perf_counter()
        w, h=eigh(A, turbo="ev", overwrite_a=True)
        
        #m = A.nbytes + Am1.nbytes 
        dt_calculo = t2-t1
        
        #memoria2.append(m)
        tiempo1.append(dt_calculo)
        tamaño1.append(j)
        
        #print (f"memoria = {m} bytes")
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
        A=laplaciana(j, dtype=float64)
        b=ones(j)
        
        t2 = perf_counter()
        w, h=eigh(A, turbo="evd", overwrite_a=True)
        
        #m = A.nbytes + Am1.nbytes 
        dt_calculo = t2-t1
        
        #memoria3.append(m)
        tiempo2.append(dt_calculo)
        tamaño2.append(j)
        
        #print (f"memoria = {m} bytes")
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
        A=laplaciana(j, dtype=float64)
        b=ones(j)
        
        t2 = perf_counter()
        w, h=eigh(A, turbo="evr", overwrite_a=True)
        
        #m = A.nbytes + Am1.nbytes 
        dt_calculo = t2-t1
        
        #memoria4.append(m)
        tiempo3.append(dt_calculo)
        tamaño3.append(j)
        
        #print (f"memoria = {m} bytes")
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
        A=laplaciana(j, dtype=float64)
        b=ones(j)
        
        t2 = perf_counter()
        w, h=eigh(A, turbo="evx", overwrite_a=True)
        
        #m = A.nbytes + Am1.nbytes 
        dt_calculo = t2-t1
        
        #memoria5.append(m)
        tiempo4.append(dt_calculo)
        tamaño4.append(j)
        
        #print (f"memoria = {m} bytes")
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
        A=laplaciana(j, dtype=float64)
        b=ones(j)
        
        t2 = perf_counter()
        w, h=eigh(A, turbo="ev", overwrite_a=False)
        
        #m = A.nbytes + Am1.nbytes 
        dt_calculo = t2-t1
        
        #memoria6.append(m)
        tiempo5.append(dt_calculo)
        tamaño5.append(j)
        
        #print (f"memoria = {m} bytes")
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
        A=laplaciana(j, dtype=float64)
        b=ones(j)
        
        t2 = perf_counter()
        w, h=eigh(A, turbo="evd", overwrite_a=False)
        
        #m = A.nbytes + Am1.nbytes 
        dt_calculo = t2-t1
        
        #memoria6.append(m)
        tiempo6.append(dt_calculo)
        tamaño6.append(j)
        
        #print (f"memoria = {m} bytes")
        print(f"dt_calculo = {dt_calculo} s")
        print (f"tamaño M = {j}")
        print ()
    i+=1

memoria7=[]
tiempo7=[]
tamaño7=[]

i=0
while i<10:
    M=[2,3,5,7,10,12,15,20,30,40,50,70,100,150,200,300,500,750,1000,1800,2500,4000]
    for j in M:     
        t1 = perf_counter()
        A=laplaciana(j, dtype=float64)
        b=ones(j)
        
        t2 = perf_counter()
        w, h=eigh(A, turbo="evr", overwrite_a=False)
        
        #m = A.nbytes + Am1.nbytes 
        dt_calculo = t2-t1
        
        #memoria6.append(m)
        tiempo7.append(dt_calculo)
        tamaño7.append(j)
        
        #print (f"memoria = {m} bytes")
        print(f"dt_calculo = {dt_calculo} s")
        print (f"tamaño M = {j}")
        print ()
    i+=1

memoria8=[]
tiempo8=[]
tamaño8=[]

i=0
while i<10:
    M=[2,3,5,7,10,12,15,20,30,40,50,70,100,150,200,300,500,750,1000,1800,2500,4000]
    for j in M:     
        t1 = perf_counter()
        A=laplaciana(j, dtype=float64)
        b=ones(j)
        
        t2 = perf_counter()
        w, h=eigh(A, turbo="evx", overwrite_a=False)
        
        #m = A.nbytes + Am1.nbytes 
        dt_calculo = t2-t1
        
        #memoria6.append(m)
        tiempo8.append(dt_calculo)
        tamaño8.append(j)
        
        #print (f"memoria = {m} bytes")
        print(f"dt_calculo = {dt_calculo} s")
        print (f"tamaño M = {j}")
        print ()
    i+=1

   
arch = open("Caso B.1 con float64 (double).txt", "w")
arch.write("Tiempo de calculo(s)   Tamaño matriz \n")
a = 0
while a < len(tamaño0):
    arch.write(f"{tiempo0[a]}     {tamaño0[a]} \n")
    a+=1
arch.close()


arch = open("Caso B.2 con float64 (double).txt", "w")
arch.write("Tiempo de calculo(s)   Tamaño matriz \n")
b = 0
while b < len(tiempo1):
    arch.write(f"{tiempo1[b]}     {tamaño1[b]} \n")
    b+=1
arch.close()


arch = open("Caso B.3 con float64 (double).txt", "w")
arch.write("Tiempo de calculo(s)   Tamaño matriz \n")
c = 0
while c < len(tamaño2):
    arch.write(f"{tiempo2[c]}     {tamaño2[c]} \n")
    c+=1    
arch.close()


arch = open("Caso B.4 con float64 (double).txt", "w")
arch.write("Tiempo de calculo(s)   Tamaño matriz \n")
d = 0
while d < len(tamaño3):
    arch.write(f"{tiempo3[d]}     {tamaño3[d]} \n")
    d+=1
arch.close()


arch = open("Caso B.5 con float64 (double).txt", "w")
arch.write("Tiempo de calculo(s)   Tamaño matriz \n")
e = 0
while e < len(tiempo4):
    arch.write(f"{tiempo4[e]}     {tamaño4[e]} \n")
    e+=1
arch.close()


arch = open("Caso B.6 con float64 (double).txt", "w")
arch.write("Tiempo de calculo(s)   Tamaño matriz \n")
f = 0
while f < len(tamaño5):
    arch.write(f"{tiempo5[f]}     {tamaño5[f]} \n")
    f+=1      
arch.close()


arch = open("Caso B.7 con float64 (double).txt", "w")
arch.write("Tiempo de calculo(s)   Tamaño matriz \n")
g = 0
while g < len(tamaño6):
    arch.write(f"{tiempo6[g]}     {tamaño6[g]} \n")
    g+=1       
    
arch.close()

arch = open("Caso B.8 con float64 (double).txt", "w")
arch.write("Tiempo de calculo(s)   Tamaño matriz \n")
h = 0
while h < len(tiempo4):
    arch.write(f"{tiempo7[h]}     {tamaño7[h]} \n")
    h+=1
arch.close()


arch = open("Caso B.9 con float64 (double).txt", "w")
arch.write("Tiempo de calculo(s)   Tamaño matriz \n")
i = 0
while i < len(tamaño8):
    arch.write(f"{tiempo8[i]}     {tamaño8[i]} \n")
    i+=1      
arch.close()


