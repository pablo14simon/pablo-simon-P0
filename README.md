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

Este proceso es aún más largo que los de las tareas anteriores, esto es debido a que se obtiene la inversa de A de una forma más completa con una operacion con un bector "b" de 1s. Por ende se realiza todo el proceso considerado en algebra lineal. Esto lo hace primero de la forma común usando el comando solve de scipy. Se fue diferenciando en los codigos de overwrite y assume. Además de diferenciar estos mismos según si es simple o double, funciones que afectan en la memoria del computador. 
Luego respecto a Eigh es un proceso similar pero se enfoca en los vectores y valores propios. A partir de esto se logra el proceso.


La variabilidad de tiempo es muy similar para cada caso, algunos son mas eficientes por ser mas simples o por asumir aspectos en la matriz. En el caso de solve es un proceso eficiente pero que va perdiendo rapidez a medida de que las matrices crecen, esto es debido a que operar con matrices grandes es dificil. Mientras que para eigh es dificil encontrar diferencias ya que son procesos muy parecidos, aunque es afectado por usar float32, relantizando todo, no como en solve que no afecta.


Los algoritmos de solve son muy eficacez comparados con los de eigh ya que trabaja con una matriz de puros unos y no con todos los valores y vectores propios posibles. Es un proceso simple, que si bien pareciera que la primera funcion de multiplicación es la mas rapida, no lo es. Scipy logra un algoritmo mas rapido con todos las otras funciones de solve. Especialmente en assume_a, así definiendo el caso A.3 el mejor. Los eigh son todos demasiado parecidos para poder compararlos.

El tamaño de la matriz si afecta en el proceso, para solve el Ax=b se vuelve muy ineficiente por lo que se opta por el comando solve. Luego en eigh demora más pero entre cada comando no hay diferencias al aumentar las matrices.

La superioridad del caso A.3 como se dijo es porque se asumen los valores positivos, que son los mas comunes, por lo que se salta varios pasos.Respecto a eigh lo que mas afecta es el float32 y double, donde el float al ocupar menos memoria el tiempo es menor.


Se ocupan 2 nucleos y 4 procesadores para cada proceso. En las imagenes se puede ver como funciona el computador en el momento de ejecución de los codigos aumenta rapidamente el CPU de uso. Tambien si nos fijamos en la memoria que es similar para todos los procesos se observa que rondea los 4.8 GB la diferencia se nota cuando va aumentando el tamaño de las matrices, viendo como en peridos el grafico sube. Aumenta más también al ocupar double.

![image](https://user-images.githubusercontent.com/88359228/130309101-5c05e2fb-8e65-4916-97ad-089e0fc24704.png)

![image](https://user-images.githubusercontent.com/88359228/130308854-4deeb27e-b7f0-4f40-8052-a845db61dc39.png)


*MCO2021-P05*

Primero se definieron las matrices laplacianas tanto para el lleno como para la dispersa, esto se puede ver en el pricnipio de cada codigo. También se ocupó para ambos la forma double, ya que fue pedido y tiene buen rendimiento. Esto se expresó mediante float64.

Analizando el metodo de calculo y ensamblaje de una matriz llena es un proceso algo lento ya que se preocupa de cada valor, este funciona mejor para N mas bajos. Esto se puede ver en los gráficos donde a medida que es menor el N^º más rapido se realiza el proceso. Un N^2 lo hace más rapido que el de N^4. Se trabajó con los n de siempre para poder comparar con procesos anteriores. 

Luego para la forma dispersa es un proceso eficáz ya que no toma en cuanta los ceros de las matrices, por lo que todo se hace más rapido. Esto se puede demostrar con los resultados obtenidos donde para ensamblar una matriz esta solo se dmoraba aproximadamente 1 segundo para M(N)=22, y el calculo tardadaba unos cuantos milisegundos. En cambio para el lleno se realizó el proceso más lento. Por lo menos en el ensamblaje fue muy parecido, también se demoró aproximadamente 1 segundo, pero para el calculo de este se demoró 10 segundos, por ende para cualquier caso es mejor escoger un proceso de calculo de matrices mediante metodo disperso. También si aumentamos el M(N) este proceso será muy eficáz no como la de lleno que le afecta drasticamente que se aumente esta variable. Ahora se puede observar el rendimiento del computador y la memoria al realizar estos dos procesos.


Matriz llena
![image](https://user-images.githubusercontent.com/88359228/131205185-657771eb-db96-45ea-91fc-777785d435c7.png)

En el momento de realizar el proceso hay un uso que pasa de 29% a 70%, siendo lento.

![image](https://user-images.githubusercontent.com/88359228/131205190-e2246cbb-7e73-4bc5-bddd-9699198d32bc.png)
Podemos ver que ocupa bastante memoria debido a que utiliza más numeros.

Matriz dispersa
![image](https://user-images.githubusercontent.com/88359228/131205207-19550e09-fc20-48ae-97a2-3b80c0e50f59.png)
Aca en cambio llega a un uso de 60% mucho más util, no necesita tanto esfuerzo ni potencia del computador para realizar el proceso.

![image](https://user-images.githubusercontent.com/88359228/131205214-ec904993-2ce9-45f4-8094-30673de0ef92.png)
La memoria disminuye un poco debido a que se ocupan menos numeros.

