# pablo-simon-P0
MCOC2021-P1
Marca/Modelo: Toshiba Satellite

Tipo: Notebook

Año adquisición: 2017

Procesador:
- Marca/Modelo: Intel Core i5 2450M
- Velocidad Base: 99.76 MHz
- Velocidad Máxima: 2843 MHz
- Numero de núcleos: 2
- Número de hilos: 4
- Arquitectura: x64
- Set de instrucciones:MMX, SSE, SSE2, SSE3, SSE4.1, SSE4.2, EM64T, VT-x, AES, AVX

Tamaño de las cachés del procesador
- L1d: 32KB
- L1i: 32KB
- L2: 256KB
- L3: 3MB

Memoriaq
- Total: 8 GB
- Tipo memoria: DDR3
- Velocidad 665.1 MHz
- Numero de (SO)DIMM: 10

Tarjeta Gráfica
- Marca / Modelo: Intel HD Graphics 3000
- Memoria dedicada: 8192 MB
- Resolución: 1366 x 768

Disco 1:
- Marca: CT480BX500SSD1
- Tipo: Disco duro fijo
- Tamaño: 445GB
- Particiones: 1
- Sistema de archivos: NTFS

Dirección MAC de la tarjeta wifi: 24:FD:52:47:25:80

Dirección IP (Interna, del router): 192.168.0.8

Dirección IP (Externa, del ISP): 190.161.68.119

Proveedor internet: VTR Banda Ancha S.A.

MCOC2021-P2
¿Cómo difiere del gráfico del profesor/ayudante?
Son gráficos muy similares ya que ambos se encuentran entre parametros similares y possen curvas muy parecidas. Mi curva se puede observar que tiende a ser más plano y posee pocas alteraciones o saltos, viendo que demoró en comenzar, asi significa que el computador trabaja de manera constante, pero puede ser lenta.
No como en el caso del profesor donde hay un momento que desacelera más en los saltos bruscos, osea recorre más lento la matriz en los momentos medios, pero aun así su tiempo es menor en varias operaciones y los saltos parecen menos altos, siendo asi su rendimiento igual o mejor que el mio. Además comienza con mayor rapidez.

¿A qué se pueden deber las diferencias en cada corrida?
Al ser un proceso iterativo donde recorre distintas matrices usando la memoria de nuestro computador, si bien cada operación se efectúa de la misma manera, se podrá diferenciar cambios en el tiempo de cada operación sabiendo que los elementos que ocupa el computador varía en cada calculo, o sea,
como la memoria se debe compartir para las matrices, en cada una se distribuye de la manera más equitativa posible, por lo que permite demorarse más o menos, según la mempria correspondiente a dicha matriz. Esto se explica conociendo las distintas memorias que posee el computador. 

El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
el de el tiempo transcurrido no o és ya que como se explicó en la pregunta anterior, el proceso para recorrer la operacion de matrices varía según la memoria que se ocupa en ese momento, por lo que varía siendo una curva no lineal. En cambio el uso de memoria se comprende de manera lineal debido a que se va acumulando.
Cada memoria utilizada en las operaciones de matrices se va acumulando según el tiempo y las matrices aumentan, por lo que va incrementando de la forma más constante posible. 

¿Qué versión de python está usando?
3.7.3

¿Qué versión de numpy está usando?
1.16.4

Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen (screenshot) de su uso de procesador durante alguna corrida para confirmar. 

![image](https://user-images.githubusercontent.com/88359228/128463141-4ebdb61f-b4a2-4c50-b32c-215d837ab60b.png)

MCOC2021-P3
