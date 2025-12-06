# Multiple assignment
x, y, z = 10, 2, 66

print(x, y, z)

# Dado un diccionario {team: founded_year}, obtener el equipo más antiguo.
teams_founded = {
    "River Plate": 1901,
    "Boca Juniors": 1905,
    "Racing Club": 1903,
    "Independiente": 1905,
    "San Lorenzo": 1908,
    "Huracán": 1908,
}

oldest_team = min(teams_founded, key=teams_founded.get)
print(f"The oldest team is {oldest_team}, founded in {teams_founded[oldest_team]}.")

# Dada una lista de tuplas (team, goals), encontrar el máximo y mínimo.
team_goals = [
    ("River Plate", 58),
    ("Boca Juniors", 52),
    ("Racing Club", 49),
    ("Independiente", 40),
    ("San Lorenzo", 46),
    ("Huracán", 35),
]

max_goals_team = max(team_goals, key=lambda item: item[1])
min_goals_team = min(team_goals, key=lambda item: item[1])

print(f"{max_goals_team} is max. {min_goals_team} is min.")

# Dada una lista de nombres, eliminar duplicados sin usar set().
team_names = [
    "River Plate",
    "Boca Juniors",
    "Racing Club",
    "River Plate",
    "San Lorenzo",
    "Boca Juniors",
    "Huracán",
    "Racing Club",
]

unique_team_names = []

for team in team_names:
    if team not in unique_team_names:
        unique_team_names.append(team)

print(unique_team_names)

# Crear una función que reciba una lista de equipos y devuelva solo los que tengan más de 100 años.
teams_years = [
    ("River Plate", 1901),
    ("Boca Juniors", 1905),
    ("Racing Club", 1903),
    ("Defensa y Justicia", 1935),
    ("Tigre", 1902),
    ("Arsenal", 1957),
]

from datetime import date


def older_than_100(teams_list: list) -> list:
    teams_older = []
    for team, founded in teams_list:
        current_year = date.today().year
        team_years = current_year - founded
        if team_years > 100:
            teams_older.append((team, founded))

    return teams_older


print(older_than_100(teams_years))

# Crear un diccionario que agrupe equipos por ciudad.
teams_cities = {
    "River Plate": "Buenos Aires",
    "Boca Juniors": "Buenos Aires",
    "Racing Club": "Avellaneda",
    "Independiente": "Avellaneda",
    "San Lorenzo": "Buenos Aires",
    "Rosario Central": "Rosario",
    "Newell's Old Boys": "Rosario",
    "Talleres": "Córdoba",
    "Belgrano": "Córdoba",
}

cities_dict = {}

for team, city in teams_cities.items():
    if city not in cities_dict:
        cities_dict[city] = []
    cities_dict[city].append(team)

print(cities_dict)

# Try - Except
teams = {"River": "Monumental", "Boca": "Bombonera"}

try:
    stadium = teams["San Lorenzo"]
    print(stadium)
except KeyError:  # ValueError para inputs
    print("The team doesn't exist")  # 1 -> The team doesn't exist


# Funciones y llamadas
def get_stadium(team_name: str) -> str:
    return teams.get(team_name, "unknown")


def show_team_info(team_name: str):
    stadium = get_stadium(team_name)
    (
        print("No team info.")  # 3 -> No team info.
        if stadium == "unknown"
        else print(f"{team_name} plays at {stadium}")  # 2 -> River plays at Monumental
    )
    return (
        "No team info." if stadium == "unknown" else f"{team_name} plays at {stadium}"
    )


show_team_info("River")  # -> River plays at Monumental
show_team_info("Racing")  # -> Racing plays at Unknown

# Desempaquetado
team_info = ("River", "Monumental", 1901)
name, stadium, founded = team_info
print(
    f"{name} was founded in {founded} and plays at {stadium}."
)  # 4 -> River was founded in 1901 and plays at Monumental.

# Bucle + lógica básica
teams_info = [
    ("River", "Monumental", 1901),
    ("Boca", "Bombonera", 1903),
    ("Huracán", "Ducó", 1927),
]

for name, stadium, founded in teams_info:
    print(
        f"{name} was founded in {founded} and plays at {stadium}."
    )  # 5 -> River was founded in ...


# Funciones - Diccionarios - Lista de tuplas - Bucle - Desempaquetado - Try
## Funciones
def is_adult(age):
    return False if age < 18 else True


def sex(value):
    return "Male" if value == "M" else "Female"


## Diccionario
validations = {"is_adult": is_adult, "sex": sex}

## Lista
items = [
    ## Tuplas
    ("is_adult", 85),
    ("is_adult", 2),
    ("sex", "F"),
    ("sex", "M"),
    ("is_bigger", 1761193193),
]

## Bucle
for item in items:
    ## Desempaquetado
    validation, value = item

    # Try
    try:
        ## Funcion en diccionario
        result = validations[validation](value)
        print(result)  # -> True False Female Male
    except KeyError:
        print(f"No existe la validación {validation}")  # -> No existe la validación

# Tema: “Gestor de tareas”
# Objetivo: Crear un programa de consola que permita gestionar tareas pendientes.

# Requisitos:
## Las tareas deben tener:
## ID (autoincremental)
## Título
## Descripción
## Estado (pendiente, en progreso, completada)
## Fecha de creación

# Funcionalidades mínimas:
## Agregar una tarea
## Listar todas las tareas
## Cambiar el estado de una tarea
## Eliminar una tarea

import datetime

# Lista para guardar las tareas
tasks = []

# Estados disponibles
statuses = ["pendiente", "en progreso", "completada"]

# Contador para el ID autoincremental
id_counter = 1


# Validar si hay tareas
def is_empty():
    if tasks:
        return False
    else:
        print("\nNo hay tareas.\n")
        return True


# Función para agregar tarea
def add_task():
    global id_counter

    title = input("Ingrese el título de la tarea: ")
    description = input("Ingrese la descripción de la tarea: ")
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    task = {
        "ID": id_counter,
        "Título": title,
        "Descripción": description,
        "Estado": "pendiente",
        "Fecha de creación": created_at,
    }

    tasks.append(task)
    id_counter += 1

    print(f"Tarea agregada.\n")


# Función para listar tareas
def list_tasks():
    if is_empty():
        return

    for task in tasks:
        print("----------")
        for key, value in task.items():
            print(f"{key}: {value}")
        print("----------")
    return


# Función para cambiar estado
def update_status():
    if is_empty():
        return

    task_id = int(input("Ingrese el ID de la tarea que quiere actualizar: "))

    for task in tasks:
        if task["ID"] != task_id:
            continue

        print(f"Estados disponibles: {statuses}")
        new_status = input("Ingrese el nuevo estado: ").lower()

        if new_status not in statuses:
            print("Estado inválido.\n")
            return

        task["Estado"] = new_status
        print("Estado actualizado correctamente.\n")
        return

    print("Tarea no encontrada.\n")
    return


# Función para eliminar tarea
def delete_task():
    if is_empty():
        return

    task_id = int(input("Ingrese el ID de la tarea que quiere eliminar: "))

    for task in tasks:
        if task["ID"] == task_id:
            tasks.remove(task)
            print("Tarea eliminada correctamente.\n")
            return

    print("Tarea no encontrada.\n")
    return


# Función para ejecutar el script
def run():
    while True:
        print("--- Gestor de tareas ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Cambiar estado de tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        option = input("\nSeleccione una opción: ")

        if option == "1":
            add_task()
        elif option == "2":
            list_tasks()
        elif option == "3":
            update_status()
        elif option == "4":
            delete_task()
        elif option == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.\n")


# Ejecutar script
run()
