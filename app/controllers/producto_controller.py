from app.database import get_connection

def obtener_productos(id: int = None):

    conn = get_connection()
    cursor = conn.cursor()

    if id is not None:
        cursor.execute("SELECT * FROM productos WHERE id = %s;", (id,))
    else:
        cursor.execute("SELECT * FROM productos;")
    resultados = cursor.fetchall()

    productos = []

    for fila in resultados:
        productos.append({
            "id": fila[0],
            "nombre": fila[1],
            "precio": fila[2]
        })

    cursor.close()
    conn.close()

    return productos


def crear_producto(producto):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO productos (nombre, precio)
    VALUES (%s, %s)
    RETURNING id
    """

    cursor.execute(query, (producto.nombre, producto.precio))

    nuevo_id = cursor.fetchone()[0]

    conn.commit()

    cursor.close()
    conn.close()

    return {
        "mensaje": "Producto creado",
        "id": nuevo_id
    }


def actualizar_producto(id, producto):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE productos
    SET nombre = %s, precio = %s
    WHERE id = %s
    """

    cursor.execute(query, (producto.nombre, producto.precio, id))

    conn.commit()

    cursor.close()
    conn.close()

    return {"mensaje": "Producto actualizado"}


def eliminar_producto(id):

    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM productos WHERE id = %s"

    cursor.execute(query, (id,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"mensaje": "Producto eliminado"}
