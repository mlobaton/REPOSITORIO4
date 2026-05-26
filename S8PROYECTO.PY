import mysql.connector
def conectar():
    conexion = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "Manuel2203?",
        database = "usuarios"
    )
    return conexion
def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS tareas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR (30),
    estado VARCHAR(30),
    prioridad VARCHAR (30)
    )
    """
    cursor.execute(query)
    conexion.commit()
    cursor.close()
    conexion.close()

def crear_tarea():
    titulo = input("Escribe el titulo de tu tarea: ")
    prioridad = input ("Escribe la prioridad de tu tarea(Alto, Medio,Bajo): ")
    conexion = conectar()
    cursor = conexion.cursor()
    query = """
    INSERT INTO tareas(titulo,estado,prioridad)
    VALUES (%s, %s , %s)
    """
    cursor.execute(query,(titulo,"Pendiente",prioridad))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Tarea agregada con exito")

def ver_tarea():
    conexion = conectar()
    cursor = conexion.cursor()
    query = """
    SELECT * FROM tareas
    """
    cursor.execute(query)
    tareas = cursor.fetchall()
    for i in tareas:
        print("ID:", i[0])
        print("TITULO:",i[1])
        print("ESTADO:",i[2])
        print("PRIORIDAD:", i[3])
    cursor.close()
    conexion.close()

def actualizar_tarea():
    id_titulo= input("Escribe el id a actualizar: ")
    estado_nuevo = input("Escribe el nuevo estado(Completado): ")
    conexion = conectar()
    cursor = conexion.cursor()
    query = """
    UPDATE tareas
    SET estado = %s
    WHERE id = %s
    """
    cursor.execute(query,(estado_nuevo,id_titulo))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Tarea actualizada con exito")

def eliminar_tarea():
    id_titulo= input("Ingresa el id a eliminar:")
    conexion = conectar()
    cursor = conexion.cursor()
    query = """
    DELETE FROM tareas
    where id = %s    
    """
    cursor.execute(query,(id_titulo,))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Tarea eliminada con exito")



crear_tabla()
while True:
    print("1.Crear tarea")
    print("2.Ver tarea")
    print("3.Actualizar tarea")
    print("4.Eliminar tarea")
    print("5.Salir")
    try:
        opcion = int(input("Seleciona una opcion: "))
    except ValueError:
        print("Escriba una opcion valida")
        continue
    if opcion == 1:
        crear_tarea()
    elif opcion == 2:
        ver_tarea()
    elif opcion == 3:
        actualizar_tarea()
    elif opcion== 4:
        eliminar_tarea()
    elif opcion == 5:
        print("Finalizando programa...")
        break
    else:
        print("Selecciona una opcion valida")    



    
    
    







    
    
    



