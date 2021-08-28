import matplotlib.pyplot as plt

arch1 = open("Caso_1_llena.txt", "r")


mat1 = arch1.read()
mat1 = mat1.split("\n")
mat1.pop(0)
mat1.pop(-1)


x=0
tiempo_e_1 = []
tiempo_c_1 = []
tamaño1 = []


M = int(len(mat1)/10)

for d in mat1:
    l=d.split()
    tiempo_e_1.append(float(l[0]))
    tiempo_c_1.append(float(l[1]))
    tamaño1.append(float(l[2]))
    x+=1        
       
    
arch1.close()



x1 = ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
T1 = [10,20,50,100,200,500,1000,2000,5000,10000,20000]

y1 = ["0.1 ms", "1 ms", "10 ms","0.1 s", "1 s", "10 s", "1 min", "10 min"]
dt1 = [0.1/1000,1/1000,10/1000,0.1,1,10,60,60*10]


plt.figure(1)
plt.subplot(2,1,1)
plt.title("Rendimiento caso 1")
i=0
j=0
while i < 10:
    while j < len(mat1):
        plt.loglog(tamaño1[j:j+22],tiempo_e_1[j:j+22], "o-",alpha=0.3,ms=3,color="k")
        j+=M
    i+=1


plt.hlines(y=max(tiempo_e_1), xmin=min(tamaño1), xmax=max(tamaño1), linestyle="--", color="blue", label="Constante")

principio=dt1[0]
fin=max(tiempo_e_1)

eje_y_1=[principio,fin]
eje_x_1=[tamaño[0],tamaño[-1]]

eje_y_2=[principio**2,fin]
eje_x_2=[tamaño[0]**2,tamaño[-1]]

eje_y_3=[principio**3,fin]
eje_x_3=[tamaño[0]**3,tamaño[-1]]

eje_y_4=[principio**4,fin]
eje_x_4=[tamaño[0]**4,tamaño[-1]]


plt.loglog(eje_x_1,eje_y_1, linestyle="--", color="orange", label="O(N)")
plt.loglog(eje_x_2,eje_y_2, linestyle="--", color="green", label="O(N2)") 
plt.loglog(eje_x_3,eje_y_3, linestyle="--", color="red", label="O(N3)")
plt.loglog(eje_x_4,eje_y_4, linestyle="--", color="purple", label="O(N4)") 

    

plt.yticks(dt1, y1)
plt.xticks(T1, x1, rotation=45)
plt.xticks(T1, ["","","","","","","","","",""])
plt.xlim(right=20000)
plt.ylim(bottom=dt1[0], top=dt1[-3])
plt.grid()
plt.ylabel("Tiempo de ensamblaje(s)")


plt.subplot(2,1,2)
i=0
j=0
while i < 10:
    while j < len(mat1):
        plt.loglog(tamaño1[j:j+22],tiempo_c_1[j:j+22], "o-",alpha=0.3,ms=3,color="k")
        j+=M
    i+=1


plt.hlines(y=max(tiempo_c_1), xmin=min(tamaño1), xmax=max(tamaño1), linestyle="--", color="blue", label="Constante")

principio=dt1[0]
fin=max(tiempo_c_1)

eje_y_1=[principio,fin]
eje_x_1=[tamaño[0],tamaño[-1]]

eje_y_2=[principio**2,fin]
eje_x_2=[tamaño[0]**2,tamaño[-1]]

eje_y_3=[principio**3,fin]
eje_x_3=[tamaño[0]**3,tamaño[-1]]

eje_y_4=[principio**4,fin]
eje_x_4=[tamaño[0]**4,tamaño[-1]]


plt.loglog(eje_x_1,eje_y_1, linestyle="--", color="orange", label="O(N)")
plt.loglog(eje_x_2,eje_y_2, linestyle="--", color="green", label="O(N2)") 
plt.loglog(eje_x_3,eje_y_3, linestyle="--", color="red", label="O(N3)")
plt.loglog(eje_x_4,eje_y_4, linestyle="--", color="purple", label="O(N4)") 

    

plt.yticks(dt1, y1)
plt.xticks(T1, x1, rotation=45)
plt.xticks(T1, x1)
plt.xlim(right=20000)
plt.ylim(bottom=dt1[0], top=dt1[-1])
plt.grid()
plt.ylabel("Tiempo de solución(s)")
plt.xlabel("Tamaño matriz M")


plt.show()
