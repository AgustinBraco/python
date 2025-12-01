## Functiones Built-in

`abs()` → Retorna el valor absoluto de un número.  
`all()` → Retorna True si todos los elementos de un objeto iterable son verdaderos.  
`any()` → Retorna True si al menos un elemento de un objeto iterable es verdadero.  
`ascii()` → Retorna una representación legible de un objeto.  
`bin()` → Retorna la versión binaria de un número (como una cadena).  
`bool()` → Retorna el valor booleano del objeto especificado.  
`bytearray()` → Retorna un objeto array de bytes (mutable).  
`bytes()` → Retorna un objeto de tipo bytes (inmutable).  
`callable()` → Retorna True si el objeto especificado es invocable.  
`chr()` → Retorna el carácter que corresponde al código Unicode entero especificado.  
`classmethod()` → Convierte un método en un método de clase.  
`compile()` → Compila la fuente especificada como un objeto de código, listo para ser ejecutado.  
`complex()` → Retorna un número complejo.  
`delattr()` → Elimina el atributo (propiedad o método) especificado del objeto.  
`dict()` → Retorna un diccionario.  
`dir()` → Retorna una lista de las propiedades y métodos del objeto especificado.  
`divmod()` → Retorna el cociente y el resto como una tupla.  
`enumerate()` → Toma una colección y retorna un objeto enumerate.  
`eval()` → Evalúa y ejecuta una expresión (cadena de texto).  
`exec()` → Ejecuta el código Python especificado.  
`filter()` → Construye un iterador con elementos.  
`float()` → Retorna un número de punto flotante (decimal).  
`format()` → Formatea un valor especificado.  
`frozenset()` → Retorna un objeto frozenset (conjunto inmutable).  
`getattr()` → Retorna el valor del atributo (propiedad o método) especificado del objeto.  
`globals()` → Retorna la tabla actual de símbolos globales como un diccionario.  
`hasattr()` → Retorna True si el objeto tiene el atributo (propiedad/método) especificado.  
`hash()` → Retorna el valor hash de un objeto.  
`help()` → Ejecuta el sistema de ayuda interactivo incorporado.  
`hex()` → Convierte un número entero en una cadena hexadecimal.  
`id()` → Retorna la identidad única de un objeto (su dirección en memoria).  
`input()` → Permite al usuario ingresar datos desde la consola.  
`int()` → Retorna un número entero.  
`isinstance()` → Retorna True si un objeto es una instancia de la clase (o tipo) especificada.  
`issubclass()` → Retorna True si la clase especificada es una subclase.  
`iter()` → Retorna un objeto iterador.  
`len()` → Retorna la longitud (número de elementos) de un objeto.  
`list()` → Retorna un objeto de tipo lista.  
`locals()` → Retorna un diccionario actualizado de la tabla de símbolos locales actual.  
`map()` → Aplica una función especificada a todos los elementos de un iterable.  
`max()` → Retorna el elemento más grande en un iterable o entre varios argumentos.  
`memoryview()` → Retorna un objeto vista de memoria.  
`min()` → Retorna el elemento más pequeño en un iterable o entre varios argumentos.  
`next()` → Retorna el siguiente elemento de un iterador.  
`object()` → Retorna una nueva característica base para todas las clases.  
`oct()` → Convierte un número entero en una cadena octal.  
`open()` → Abre un archivo y retorna un objeto de archivo (stream).  
`ord()` → Retorna un número entero que representa el código Unicode del carácter especificado.  
`pow()` → Retorna el valor de x elevado a la potencia de y (y el módulo z, opcionalmente).  
`print()` → Imprime el objeto(s) especificado(s) al dispositivo de salida estándar.  
`property()` → Retorna un atributo de propiedad.  
`range()` → Retorna una secuencia inmutable de números.  
`repr()` → Retorna una representación de cadena "oficial" de un objeto.  
`reversed()` → Retorna un iterador invertido.  
`round()` → Redondea un número al número de decimales especificado.  
`set()` → Retorna un nuevo objeto de conjunto (set).  
`setattr()` → Establece el valor del atributo (propiedad/método) de un objeto.  
`slice()` → Retorna un objeto slice, utilizado para rebanado (slicing).  
`sorted()` → Retorna una nueva lista ordenada de los elementos en el iterable.  
`staticmethod()` → Convierte un método en un método estático.  
`str()` → Retorna un objeto de tipo cadena (string).  
`sum()` → Suma los elementos de un iterable.  
`super()` → Retorna un objeto proxy que delega llamadas a un método de clase padre o hermana.  
`tuple()` → Retorna un objeto de tipo tupla.  
`type()` → Retorna el tipo del objeto.  
`vars()` → Retorna el atributo **dict** de un objeto.  
`zip()` → Retorna un iterador que combina elementos de dos o más iterables en tuplas.

---

## Identificar tipos de datos

`""` → Cadena de caracteres → `str`

`0` → Número entero → `int`

`0.0` → Número decimal (punto flotante) → `float`

`{clave:valor}` → Diccionario → `dict`

`{item, item}` → Conjunto → `set`

`[item, item]` → Lista → `list`

`(item, item)` → Tupla → `tuple`

---

## Métodos por tipo de dato

### **str**

`capitalize()` → Convierte el primer carácter de la cadena a mayúscula.  
`casefold()` → Convierte la cadena a minúsculas, de forma más agresiva que `lower()`.  
`center()` → Retorna una cadena centrada, rellena con un carácter especificado.  
`count()` → Retorna el número de veces que un valor especificado aparece en la cadena.  
`encode()` → Retorna una versión codificada (encoded) de la cadena.  
`endswith()` → Retorna True si la cadena termina con el valor especificado.  
`expandtabs()` → Establece el tamaño de tabulación de la cadena.  
`find()` → Busca un valor y retorna la posición de la primera ocurrencia (sino, -1).  
`format()` → Formatea valores especificados dentro de una cadena.  
`format_map()` → Formatea valores en una cadena utilizando un diccionario para el mapeo.  
`index()` → Busca un valor y retorna la posición de la primera ocurrencia (sino, excepción).  
`isalnum()` → Retorna True si todos los caracteres son alfanuméricos (letras o números).  
`isalpha()` → Retorna True si todos los caracteres son letras.  
`isascii()` → Retorna True si todos los caracteres de la cadena son ASCII.  
`isdecimal()` → Retorna True si todos los caracteres de la cadena son decimales.  
`isdigit()` → Retorna True si todos los caracteres de la cadena son dígitos.  
`isidentifier()` → Retorna True si la cadena es un identificador válido (ej. nombre de variable).  
`islower()` → Retorna True si todos los caracteres de la cadena están en minúsculas.  
`isnumeric()` → Retorna True si todos los caracteres de la cadena son numéricos.  
`isprintable()` → Retorna True si todos los caracteres de la cadena son imprimibles.  
`isspace()` → Retorna True si todos los caracteres de la cadena son espacios en blanco.  
`istitle()` → Retorna True si la cadena sigue las reglas de un título (inicia con mayúscula).  
`isupper()` → Retorna True si todos los caracteres de la cadena están en mayúsculas.  
`join()` → Convierte los elementos de un iterable en una cadena.  
`ljust()` → Retorna una versión de la cadena justificada a la izquierda.  
`lower()` → Convierte una cadena a minúsculas.  
`lstrip()` → Retorna una versión de la cadena sin espacios a la izquierda.  
`maketrans()` → Retorna una tabla de traducción para ser usada en translate.  
`partition()` → Divide la cadena en tres partes (antes, separador, después) y retorna una tupla.  
`replace()` → Retorna una cadena donde un valor especificado es reemplazado por otro.  
`rfind()` → Busca un valor y retorna la posición de la última ocurrencia (sino, -1).  
`rindex()` → Busca un valor y retorna la posición de la última ocurrencia (sino, excepción).  
`rjust()` → Retorna una versión de la cadena justificada a la derecha.  
`rpartition()` → Divide la cadena en tres partes buscando desde la derecha y retorna una tupla.  
`rsplit()` → Divide la cadena en una lista buscando desde la derecha.  
`rstrip()` → Retorna una versión de la cadena con el trim (eliminación de espacios) a la derecha.  
`split()` → Divide la cadena en una lista usando el separador especificado.  
`splitlines()` → Divide la cadena en una lista de líneas, basándose en los saltos de línea.  
`startswith()` → Retorna True si la cadena comienza con el valor especificado.  
`strip()` → Retorna una versión de la cadena con el trim a la izquierda y a la derecha.  
`swapcase()` → Intercambia mayúsculas por minúsculas y viceversa.  
`title()` → Convierte el primer carácter de cada palabra a mayúscula.  
`translate()` → Retorna una cadena traducida, utilizando una tabla de traducción.  
`upper()` → Convierte una cadena a mayúsculas.  
`zfill()` → Rellena la cadena con el número especificado de ceros a la izquierda.

### **list**

`ppend()` → Agrega un elemento al final de la lista.  
`clear()` → Elimina todos los elementos de la lista.  
`copy()` → Retorna una copia de la lista.  
`count()` → Retorna el número de elementos con el valor especificado.  
`extend()` → Agrega los elementos de un iterable a la lista actual.  
`index()` → Retorna el índice de la primera ocurrencia del elemento con el valor especificado.  
`insert()` → Agrega un elemento en la posición especificada.  
`pop()` → Elimina y retorna el elemento en la posición especificada (o el último).  
`remove()` → Elimina la primera ocurrencia del elemento con el valor especificado.  
`reverse()` → Invierte el orden de los elementos de la lista _in place_.  
`sort()` → Ordena la lista _in place_.

### **dict**

`clear()` → Elimina todos los elementos del diccionario.  
`copy()` → Retorna una copia del diccionario.  
`fromkeys()` → Retorna un nuevo diccionario con las claves especificadas y un valor por defecto.  
`get()` → Retorna el valor de la clave especificada, con un valor por defecto si no existe.  
`items()` → Retorna una vista (lista de tuplas) de los pares clave-valor del diccionario.  
`keys()` → Retorna una vista (lista) de las claves del diccionario.  
`pop()` → Elimina y retorna el valor del elemento con la clave especificada.  
`popitem()` → Elimina y retorna el último par clave-valor insertado.  
`setdefault()` → Retorna el valor de la clave. Si no existe, la inserta con un valor especificado.  
`update()` → Actualiza el diccionario con los pares clave-valor especificados.  
`values()` → Retorna una vista (lista) de todos los valores del diccionario.

### **tuple**

`count()` → Retorna el número de veces que un valor especificado aparece en la tupla.  
`index()` → Busca un valor y retorna la posición (índice) de la primera ocurrencia.

## **set**

`add()` → Agrega un elemento al conjunto.  
`clear()` → Elimina todos los elementos del conjunto.  
`copy()` → Retorna una copia del conjunto.  
`difference()` → Retorna un nuevo conjunto con la diferencia entre el primer y segundo conjunto.  
`difference_update()` → Elimina de este conjunto los elementos que están en otro conjunto.  
`discard()` → Elimina el elemento especificado si está presente (no lanza error si no existe).  
`intersection()` → Retorna un nuevo conjunto con la intersección de este conjunto y otros.  
`intersection_update()` → Conserva en este conjunto los elementos que están en otro conjunto.  
`isdisjoint()` → Retorna True si los dos conjuntos no tienen elementos en común.  
`issubset()` → Retorna True si todos los elementos están presentes en el segundo conjunto.  
`issuperset()` → Retorna True si todos los elementos están presentes en este conjunto.  
`pop()` → Elimina y retorna un elemento arbitrario del conjunto.  
`remove()` → Elimina el elemento especificado (lanza error si no existe).  
`symmetric_difference()` → Retorna un conjunto con los que están en uno, pero no en ambos.  
`symmetric_difference_update()` → Actualiza el conjunto con la diferencia de sí mismo y otro.  
`union()` → Retorna un nuevo conjunto con la unión de todos los conjuntos.  
`update()` → Inserta en este conjunto todos los elementos de otros conjuntos o iterables.

### **file**

`close()` → Cierra el archivo.  
`detach()` → Retorna el flujo sin procesar (raw stream) separado del búfer.  
`fileno()` → Retorna el descriptor de archivo (un número) del sistema operativo.  
`flush()` → Limpia los búferes internos (escribe el contenido en el disco).  
`isatty()` → Retorna True si el flujo de archivo es interactivo (ej. está conectado a una terminal).  
`read()` → Retorna el contenido completo (o la cantidad especificada) del archivo.  
`readable()` → Retorna True si el archivo permite la lectura.  
`readline()` → Retorna una única línea del archivo.  
`readlines()` → Retorna una lista con todas las líneas restantes del archivo.  
`seek()` → Cambia la posición actual del puntero del archivo.  
`seekable()` → Retorna True si el archivo permite cambiar la posición del puntero.  
`tell()` → Retorna la posición actual del puntero del archivo.  
`truncate()` → Reduce o extiende el archivo a un tamaño especificado.  
`writable()` → Retorna True si el archivo permite la escritura.  
`write()` → Escribe la cadena especificada en el archivo.  
`writelines()` → Escribe una lista de cadenas al archivo.

---

## **Keywords**

`and` → Operador lógico booleano (AND).  
`as` → Para crear un alias o dar un nombre alternativo.  
`assert` → Para depuración, comprueba una condición y lanza un `AssertionError` si es falsa.  
`async` → Se usa para definir una función asíncrona (corutina).  
`await` → Pausa la ejecución de una función asíncrona hasta que se complete una operación.  
`break` → Para salir inmediatamente de un bucle.  
`case` → Define un patrón en una sentencia `match`.  
`class` → Para definir una nueva clase.  
`continue` → Para saltar a la siguiente iteración de un bucle.  
`def` → Para definir una función.  
`del` → Para eliminar un objeto o parte de un objeto.  
`elif` → Cláusula de "si no" condicional, después de un `if`.  
`else` → Cláusula que se ejecuta si ninguna condición anterior fue verdadera.  
`except` → Se usa en el manejo de excepciones, define qué hacer cuando ocurre una excepción.  
`False` → Valor booleano de falsedad.  
`finally` → Bloque de código en el manejo de excepciones que se ejecuta siempre.  
`for` → Para crear un bucle de iteración sobre un iterable.  
`from` → Se usa junto con `import` para importar partes específicas de un módulo.  
`global` → Para declarar que una variable dentro de una función es la variable global.  
`if` → Para hacer una sentencia condicional "si".  
`import` → Para importar un módulo.  
`in` → Para comprobar si un valor está presente en un iterable.  
`is` → Para probar si dos variables hacen referencia al mismo objeto en memoria.  
`lambda` → Para crear una función anónima (sin nombre) pequeña.  
`match` → Inicia una sentencia de coincidencia de patrones.  
`None` → Representa la ausencia de valor (valor nulo).  
`nonlocal` → Para declarar una variable de una función anidada que no es local.  
`not` → Operador lógico booleano (NOT).  
`or` → Operador lógico booleano (OR).  
`pass` → Una sentencia nula, se usa como marcador de posición.  
`raise` → Para lanzar (generar) una excepción.  
`return` → Para salir de una función y devolver un valor.  
`True` → Valor booleano de verdad.  
`try` → Inicia un bloque de código para probar errores (manejo de excepciones).  
`while` → Para crear un bucle que se repite mientras una condición sea verdadera.  
`with` → Se usa para envolver la ejecución con un administrador de contexto.  
`yield` → Para retornar un valor de un generador, pausando la función.

---
