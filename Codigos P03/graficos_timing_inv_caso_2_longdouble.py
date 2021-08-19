import matplotlib.pyplot as plt

arch = open("timing_inv_caso_2_longdouble.txt", "r")

mat = arch.read()
mat = mat.split("\n")
mat.pop(0)
mat.pop(-1)

x=0
tiempo = []
tamaño = []
memoria = []

M = int(len(mat)/10)

for d in mat:
    l=d.split()
    tiempo.append(float(l[0]))
    memoria.append(float(l[1]))
    tamaño.append(float(l[2]))

arch.close()    

x1 = ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
T1 = [10,20,50,100,200,500,1000,2000,5000,10000,20000]

y1 = ["0.1 ms", "1 ms", "10 ms","0.1 s", "1 s", "10 s", "1 min", "10 min"]
dt1 = [0.1/1000,1/1000,10/1000,0.1,1,10,60,60*10]

y2 = ["1 KB", "10KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "10 GB"]
m1 = [1*10**3,10*10**3,100*10**3,1*10**6,10*10**6,100*10**6,1*10**9,10*10**9]

plt.figure(1)
plt.subplot(2,1,1)
plt.title("Rendimiento_inv caso 2 longdouble")
i=0
j=0
while i < 10:
    while j < len(mat):
        plt.loglog(tamaño[j:j+22],tiempo[j:j+22], "o-")
        j+=M
    i+=1
    
plt.yticks(dt1, y1)
plt.xticks(T1, ["","","","","","","","","",""])
plt.xlim(right=20000)
plt.grid()
plt.ylabel("Tiempo transcurrido (s)")

plt.subplot(2,1,2)
plt.loglog(tamaño, memoria,"o-")
plt.hlines(y=8*10**9, xmin=0, xmax=20000, linestyle="--")
plt.xticks(T1, x1, rotation=45)
plt.yticks(m1,y2)
plt.xlim(right=20000)
plt.grid()
plt.xlabel("Tamaño matriz M")
plt.ylabel("Uso memoria (s)")

plt.savefig("Redimiento de inversion")
plt.show()

