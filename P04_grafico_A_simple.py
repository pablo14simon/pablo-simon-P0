import matplotlib.pyplot as plt

arch1 = open("Caso A.1 con float32 (simple).txt", "r")
arch2 = open("Caso A.2 con float32 (simple).txt", "r")
arch3 = open("Caso A.3 con float32 (simple).txt", "r")
arch4 = open("Caso A.4 con float32 (simple).txt", "r")
arch5 = open("Caso A.5 con float32 (simple).txt", "r")
arch6 = open("Caso A.6 con float32 (simple).txt", "r")
arch7 = open("Caso A.7 con float32 (simple).txt", "r")

mat1 = arch1.read()
mat1 = mat1.split("\n")
mat1.pop(0)
mat1.pop(-1)

x=0
uno=0
un=0
e=0
tiempo1 = []
tamaño1 = []
prom1 =[]



M = int(len(mat1)/2)

for d in mat1:
    l=d.split()
    tiempo1.append(float(l[0]))
    tamaño1.append(float(l[1]))
    x+=1        

while uno<len(tiempo1):
    while e<len(mat1):
        un+=tiempo1[e]
        e+=M
    prom1.append(un/10)
    e+=1
    uno+=10
       
    
arch1.close()

mat2 = arch2.read()
mat2 = mat2.split("\n")
mat2.pop(0)
mat2.pop(-1)

x=0
tiempo2 = []
tamaño2 = []
prom=[]


M = int(len(mat2)/2)

for d in mat2:
    l=d.split()
    tiempo2.append(float(l[0]))
    tamaño2.append(float(l[1]))
    prom.append((float(l[0]))/10)
    x+=1        
    
arch2.close()

mat3 = arch3.read()
mat3 = mat3.split("\n")
mat3.pop(0)
mat3.pop(-1)

x=0
tiempo3 = []
tamaño3 = []
prom3=[]


M = int(len(mat3)/2)

for d in mat2:
    l=d.split()
    tiempo3.append(float(l[0]))
    tamaño3.append(float(l[1]))
    prom3.append((float(l[0]))/10)
    x+=1        
    
arch3.close()  


mat4 = arch4.read()
mat4 = mat4.split("\n")
mat4.pop(0)
mat4.pop(-1)

x=0
uno=0
un=0
e=0
tiempo4 = []
tamaño4 = []
prom4 =[]



M = int(len(mat4)/2)

for d in mat4:
    l=d.split()
    tiempo1.append(float(l[0]))
    tamaño1.append(float(l[1]))
    x+=1        

while uno<len(tiempo4):
    while e<len(mat4):
        un+=tiempo4[e]
        e+=M
    prom4.append(un/10)
    e+=1
    uno+=10
       
    
arch4.close()

mat5 = arch5.read()
mat5 = mat5.split("\n")
mat5.pop(0)
mat5.pop(-1)

x=0
uno=0
un=0
e=0
tiempo5 = []
tamaño5 = []
prom5 =[]



M = int(len(mat5)/2)

for d in mat5:
    l=d.split()
    tiempo5.append(float(l[0]))
    tamaño5.append(float(l[1]))
    x+=1        

while uno<len(tiempo5):
    while e<len(mat5):
        un+=tiempo5[e]
        e+=M
    prom5.append(un/10)
    e+=1
    uno+=10
       
    
arch5.close()

mat6 = arch6.read()
mat6 = mat6.split("\n")
mat6.pop(0)
mat6.pop(-1)

x=0
uno=0
un=0
e=0
tiempo6 = []
tamaño6 = []
prom6 =[]



M = int(len(mat6)/2)

for d in mat6:
    l=d.split()
    tiempo6.append(float(l[0]))
    tamaño6.append(float(l[1]))
    x+=1        

while uno<len(tiempo6):
    while e<len(mat6):
        un+=tiempo6[e]
        e+=M
    prom6.append(un/10)
    e+=1
    uno+=10
       
    
arch6.close()

mat7 = arch7.read()
mat7 = mat7.split("\n")
mat7.pop(0)
mat7.pop(-1)

x=0
uno=0
un=0
e=0
tiempo7 = []
tamaño7 = []
prom7 =[]



M = int(len(mat7)/2)

for d in mat7:
    l=d.split()
    tiempo7.append(float(l[0]))
    tamaño7.append(float(l[1]))
    x+=1        

while uno<len(tiempo7):
    while e<len(mat7):
        un+=tiempo1[e]
        e+=M
    prom7.append(un/10)
    e+=1
    uno+=10
       
    
arch7.close()            

x1 = ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
T1 = [10,20,50,100,200,500,1000,2000,5000,10000,20000]

y1 = ["0.1 ms", "1 ms", "10 ms","0.1 s", "1 s", "10 s", "1 min", "10 min"]
dt1 = [0.1/1000,1/1000,10/1000,0.1,1,10,60,60*10]

y2 = ["1 KB", "10KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "10 GB"]
m1 = [1*10**3,10*10**3,100*10**3,1*10**6,10*10**6,100*10**6,1*10**9,10*10**9]


plt.figure(1)
plt.subplot(2,1,1)
plt.title("Rendimiento A todos los casos single")
i=0
j=0
while i < 10:
    while j < len(mat1):
        plt.loglog(tamaño1[j:j+22],tiempo1[0:22], "o-")
        plt.loglog(tamaño2[0:22],tiempo2[0:22], "o-")
        plt.loglog(tamaño3[0:22],tiempo3[0:22], "o-")
        plt.loglog(tamaño4[j:j+22],tiempo4[0:22], "o-")
        plt.loglog(tamaño5[0:22],tiempo5[0:22], "o-")
        plt.loglog(tamaño6[0:22],tiempo6[0:22], "o-")
        plt.loglog(tamaño7[0:22],tiempo7[0:22], "o-")
        j+=M
    i+=1



plt.yticks(dt1, y1)
plt.xticks(T1, x1, rotation=45)
plt.xticks(T1, ["","","","","","","","","",""])
plt.xlim(right=20000)
plt.grid()
plt.ylabel("Tiempo transcurrido (s)")
plt.xlabel("Tamaño matriz M")



plt.savefig("Redimiento de inversion")
plt.show()


