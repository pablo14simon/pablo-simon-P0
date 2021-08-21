# pablo-simon-P0
*MCOC2021-P1*

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

*MCOC2021-P2*

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

*MCOC2021-P3*

En esta entrega se realizó un codigo para para definir la función de laplace y así construir las matrices correspondientes con 2 en la diagonal y -1 en las diagonales secundarias. Luego se realizaron 12 codigos que permitieran medir cual era el rendimiento al hacer la matriz y al invertirla, así para cada caso ya explicado en el enunciado. Luego se realizó un codigo que permitía gráficar este rendimiento de inversión y memoria para cada caso. 

Hubieron algunos casos en los que el codigo no funcionaba, cuando se trataba de medir el desempeño con np.longdouble o bien dicho usando el comando float128. Esto fue porque mi python específico no poseia en la libreria numpy esta opción. Es un error muy común en donde muestra en la consola FileNotFound[Errno 2]. También ocuriió especificamente para el caso 1 de numpy.linalg.inv usando el np.half osea flow16. Esto ocurrió porque python o bien el computador no aguantaba esto, ya que el comando linalg no lo soportaba.

Además de todo esto se entregaron otras dos carpetas, una con los textos entregados por los codigos, los que fueron necesarios para graficar de forma ordenada. Y otra carpeta con la imagen de los gráficos obtenidos. 
Por último se hizo la entrega correspondiente por canvas.


¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)? Justifique claramente su respuesta.

El comando scipy con overwrite = True es el más rapido, luego el mismo pero con False y por ultimo el numpy. Esto ocurre porque el numpy recorre la matriz entera en cambio scipy ocupa una funcion de la matriz. Luego para los distintos flows es decir, half, single, double y longdouble. Estos son comandos que permiten que el computador funcione con una memoria específica, por ejemplo el half reducirá a la mitad los bytes utilizado. Esto puede afectar entonces en la rapidez.

¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? Justifique su comentario en base al uso de procesadores y memoria observado durante las corridas. 

Aca podemos ver como es que tanto la memoria como el cpu aumenta rotundxamente en el momento en que abro una aplicación. Este proceso fue mientras corría el codigo. Esto es porque tanto el cache como el paralelismo quitan espacio y rendimiento, debido a que se realizan varios procesos al mismo tiempo. Si bien la memoria caché es la más baja, si afecta.

![image](https://user-images.githubusercontent.com/88359228/130005010-762367c1-97d2-4a5c-8cbb-0d6c4c1b9400.png)
![image](https://user-images.githubusercontent.com/88359228/130005020-1011a951-7ff9-4017-bee5-6294da62a270.png)

*MCOC2021-P4*
