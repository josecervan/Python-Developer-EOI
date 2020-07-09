-------
Título
-------
Algoritmo babilónico / método de Herón

------------
Descripción
------------
Cálculo iterativo de la raíz cuadrada de un número real N >= 1, en dos pasos:
	
	1.- Algoritmo para calcular una estimación del valor inicial (x_0) para el algoritmo babilónico.
	2.- Algoritmo babilónico para calcular el valor sqrt(N).

----------------------
1.- Estimación de x_0
----------------------
Sea D el número de dígitos a la izquierda del punto decimal de N:
	- Si D impar ==> z = (D - 1) / 2, x_0 = 2ez = 2 * 10^z
	- Si D par   ==> z = (D - 2) / 2, x_0 = 6ez = 6 * 10^z

-----------------------
2.- Cálculo de sqrt(N)
-----------------------
Partiendo del x_0 estimado, se itera el siguiente cálculo iterativo hasta que la diferencia entre x_{n+1} y x_{n} sea menor que un determinado error de precisión (\epsilon):

	x_{n+1} = (x_{n} + N / x_{n}) / 2

------------------------
3.- Valores de \epsilon
------------------------
Probar los siguientes valores:

	e = 1e-5
	e = 1e-6

