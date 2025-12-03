## Conceptos

- **Snippets:** ejecutar código desde la terminal.
  ```python
  $ python
  >>> print(”Hola, Juan”)
  ```
- **F-Strings**: cadenas que contienen variables.
  ```python
  name = “Juan”
  f”Hola, {name}”
  ```
- **Métodos**: función que usa los datos contenidos dentro del objeto.
  ```python
  name = “Juan”
  name.title()
  ```
- **Escaping**: método para que un carácter especial sea interpretado literalmente.
  ```python
  \n > Salto en linea
  \t > Tabulación
  ```

---

## Convenciones

Las variables solo deben contener letras, numeros y guiones bajos.

Pueden empezar por letra o guion pero nunca por número.

```python
UpperCamelCase = "Clases"       # Clases
UPPER_SNAKE_CASE = "Constantes" # Constantes
lower_snake_case = "Resto"      # Variables y demás
```

---

## Tipos de datos

```python
entero: int = 10            # Número entero
decimal: float = 10.1       # Número decimal
texto: str = "10"           # Cadena de texto
lista: list = [1, 2]        # Lista ordenada y modificable
tupla: tuple = (1, 2)       # Colección ordenada e inmutable
conjunto: set = {1, 2, 3}   # Colección desordenada sin elementos repetidos
diccionario: dict = {1: 1}  # Pares clave:valor
booleano: bool = True       # Verdadero o falso
nulo: None = None           # Nulo o sin valor
```

---

## Funciones

### Argumentos y parametros

```python
# Se definen argumentos
def foo(arguments: str) -> str:
    print(arguments)
    return arguments

# Se llama con parámetros
foo("parameters")
```

### Condicional y ternario

```python
# Condicional
if age < 18
    return False
else
    return True

# Ternario
return False if age < 18 else True
```

### Valores por defecto

```python
# Se pueden definir valores por defecto
def foo(a, b=1, c=2):
    return a, b, c

# Al llamar la función, esos valores se pueden pasar o no
foo(1)        # 1, 1, 2
foo(1, 2)     # 1, 2, 2
foo(a=3, c=5) # 3, 1, 5
```

### Multiples argumentos

```python
# Usamos * o ** para múltiples argumentos
def foo(a, b, *args, **kwargs):
    return a, b, args, kwargs

# Al llamar la función, no usamos * ni **
foo(1, 2, 3, 3, 3, method="POST") # 1, 2 (3, 3, 3) {'method': 'POST'}
foo(0, 0, 10, 100, 2, rol="user") # 0, 0 (10, 100, 2) {'rol': 'user'}
```

### Llamadas

```python
from typing import Callable

def foo1(text: str) -> str:
    return text

def foo2(foo: Callable) -> str:
    foo("1")
    return "2"

foo2(foo1)
# Salida:
# 1
# 2
```

---

## Desempaquetado

```python
x, y, z = (1, 200, 2.2)

names = ["Juan", "Jose"]
name1, name2 = names

user = {"first_name": "Juan", "last_name": "Perez"}
first_name = user["first_name"]
last_name = user["last_name"]
```

---

## Try - Except

```python
validations = {"is_true": is_true, "is_false": is_false}

try:
    result = validations["is_true"](true)
    return result
except KeyError:
    print("No existe la validación")
```

---

## Archivos

```python
# Abrir
csv = open("file.csv", "r")

for row in csv:
    print(row.strip())

# Cerrar
csv.close()

# Abrir y cerrar
with open("file.csv", "r") as csv:
    for row in csv:
        print(row.strip())
```

---
