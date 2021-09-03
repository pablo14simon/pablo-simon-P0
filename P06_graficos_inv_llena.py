import matplotlib.pyplot as plt

arch2 = open("Caso_inv_llena.txt", "r")


mat2 = arch2.read()
mat2 = mat2.split("\n")
mat2.pop(0)
mat2.pop(-1)


x=0
tiempo_e_2 = []
tiempo_c_2 = []
tamaño2 = []


M = int(len(mat2)/10)

for d in mat2:
    l=d.split()
    tiempo_e_2.append(float(l[0]))
    tiempo_c_2.append(float(l[1]))
    tamaño2.append(float(l[2]))
    x+=1        
       
    
arch2.close()



#x2 = ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
#T2 = [10,20,50,100,200,500,1000,2000,5000,10000,20000]

x2 = ["10","20","50","100","200","500","1000","2000","5000","10000","20000","50000","100000","200000","500000","1000000","2000000","5000000","5000000000"]
T2 = [10,20,50,100,200,500,1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000,2000000,5000000, 5000000000000]

y2 = ["0.1 ms", "1 ms", "10 ms","0.1 s", "1 s", "10 s", "1 min", "10 min"]
dt2 = [0.1/1000,1/1000,10/1000,0.1,1,10,60,60*10]
#y2 = ["0.1 ms", "1 ms", "10 ms","0.1 s", "1 s", "10 s", "1 min"]
#dt2 = [0.1/1000,1/1000,10/1000,0.1,1,10]


plt.figure(1)
plt.subplot(2,1,1)
plt.title("Rendimiento caso_inv_llena")
i=0
j=0
while i < 10:
    while j < len(mat2):
        plt.loglog(tamaño2[j:j+21],tiempo_e_2[j:j+21], "o-",alpha=0.3,ms=3,color="k")
        j+=M
    i+=1


plt.hlines(y=max(tiempo_e_2), xmin=min(tamaño2), xmax=max(tamaño2), linestyle="--", color="blue", label="Constante")

principio=dt2[0]
fin=max(tiempo_e_2)

eje_y_1=[principio,fin]
eje_x_1=[tamaño2[0],tamaño2[-1]]

eje_y_2=[principio**2,fin]
eje_x_2=[tamaño2[0]**2,tamaño2[-1]]

eje_y_3=[principio**3,fin]
eje_x_3=[tamaño2[0]**3,tamaño2[-1]]

eje_y_4=[principio**4,fin]
eje_x_4=[tamaño2[0]**4,tamaño2[-1]]


plt.loglog(eje_x_1,eje_y_1, linestyle="--", color="orange", label="O(N)")
plt.loglog(eje_x_2,eje_y_2, linestyle="--", color="green", label="O(N2)") 
plt.loglog(eje_x_3,eje_y_3, linestyle="--", color="red", label="O(N3)")
plt.loglog(eje_x_4,eje_y_4, linestyle="--", color="purple", label="O(N4)") 

    

plt.yticks(dt2, y2)
plt.xticks(T2, x2, rotation=45)
plt.xticks(T2, ["","","","","","","","","",""])
plt.xlim(right=20000)
plt.ylim(bottom=dt2[0], top=dt2[-2])
plt.grid()
plt.ylabel("Tiempo de ensamblaje(s)")


plt.subplot(2,1,2)
i=0
j=0
while i < 10:
    while j < len(mat2):
        plt.loglog(tamaño2[j:j+21],tiempo_c_2[j:j+21], "o-",alpha=0.3,ms=3,color="k")
        j+=M
    i+=1


plt.hlines(y=max(tiempo_c_2), xmin=min(tamaño2), xmax=max(tamaño2), linestyle="--", color="blue", label="Constante")

principio=dt2[0]
fin=max(tiempo_c_2)

eje_y_1=[principio,fin]
eje_x_1=[tamaño2[0],tamaño2[-1]]

eje_y_2=[principio**2,fin]
eje_x_2=[tamaño2[0]**2,tamaño2[-1]]

eje_y_3=[principio**3,fin]
eje_x_3=[tamaño2[0]**3,tamaño2[-1]]

eje_y_4=[principio**4,fin]
eje_x_4=[tamaño2[0]**4,tamaño2[-1]]


plt.loglog(eje_x_1,eje_y_1, linestyle="--", color="orange", label="O(N)")
plt.loglog(eje_x_2,eje_y_2, linestyle="--", color="green", label="O(N2)") 
plt.loglog(eje_x_3,eje_y_3, linestyle="--", color="red", label="O(N3)")
plt.loglog(eje_x_4,eje_y_4, linestyle="--", color="purple", label="O(N4)") 

    

plt.yticks(dt2, y2)
plt.xticks(T2, x2, rotation=45)
plt.xticks(T2, x2)
plt.xlim(right=20000)
plt.ylim(bottom=dt2[0], top=dt2[-2])
plt.grid()
plt.ylabel("Tiempo de solución(s)")
plt.xlabel("Tamaño matriz M")


plt.show()
