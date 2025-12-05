import pickle
import re 

# ===============================================
# DATOS GLOBALES
# ===============================================

inventario = [
    ['F-A01', 'Manzana Roja', 2.50, 100],
    ['F-B02', 'Pera', 2.00, 80],
    ['F-C03', 'Cambur', 1.80, 120],
    ['F-D04', 'Naranja', 2.20, 90],
    ['V-E05', 'Lechuga Romana', 1.50, 50],
    ['V-F06', 'Tomate Perita', 2.80, 70],
    ['H-V10', 'Harina P.A.N.', 3.25, 250],
    ['H-I12', 'Cereal Kellogg’s', 5.99, 110],
    ['C-V20', 'Diablitos Underwood', 4.10, 150],
    ['C-I21', 'Atún Van Camp’s', 3.80, 200],
    ['C-I22', 'Salsa de Tomate Heinz', 4.90, 130],
    ['B-V30', 'Maltín Polar', 1.95, 350],
    ['B-I31', 'Coca Cola Regular 2L', 3.50, 160],
    ['B-I32', 'Coca Cola Light 1.5L', 3.20, 140],
    ['L-V41', 'Queso Telita', 6.80, 30],
    ['L-V42', 'Queso Duro Rallado', 7.50, 45],
    ['L-V43', 'Queso Guayanés', 8.50, 25],
    ['L-I44', 'Yogurt Danone Fresa', 3.15, 190],
    ['L-I45', 'Yogurt Danone Natural', 3.00, 200],
    ['CF-I46', 'Jamón de Pavo', 7.99, 50]
]

# ===============================================
# FUNCIONES DE PERSISTENCIA
# ===============================================

def guardar_inventario(inventario, nombre_archivo="inventario.bin"):
    with open(nombre_archivo, "wb") as archivo:
        pickle.dump(inventario, archivo)
        print(f"Inventario guardado en '{nombre_archivo}'")

# ===============================================
# FUNCIONES DE VALIDACIÓN
# ===============================================

def validar_codigo(codigo): 
    patron='^[a-zA-Z0-9-]+$'
    return re.search(patron , codigo)

def validar_precio(precio):
    patron=r'^\d*\.?\d+$'
    return re.fullmatch(patron , precio)

def validar_stcok(stock):
    return stock.isdigit()

# ===============================================
# FUNCIONES DE BÚSQUEDA Y UTILIDAD
# ===============================================

def buscar_codigo(inventario, codigo):
    for i, producto in enumerate(inventario):
        if producto[0] == codigo: 
            return producto, i  
    return None, -1

def buscar_por_nombre(inventario): 
    print('\n---- BUSCAR POR NOMBRE ----')
    nombre = input('Introduzca el nombre a buscar: ').strip().lower()
    lista_productos_encontrados = []
    for producto in inventario:
        nombre_producto = producto[1].lower() 
        if nombre in nombre_producto:
            lista_productos_encontrados.append(producto)
    if lista_productos_encontrados:
        print(f'\nSe encontraron {len(lista_productos_encontrados)} producto(s) que contienen "{nombre}":')
        mostrar_productos(lista_productos_encontrados)
    else:
        print(f'ERROR: No se encontró ninguna coincidencia para "{nombre}".')

# ===============================================
# FUNCIONES DE VISUALIZACIÓN
# ===============================================

def mostrar_productos(lista_productos):
    # Corrección de caracteres y alineación de encabezados
    if not lista_productos:
        print("\nEl inventario está vacío. No hay productos para mostrar.")
        return
        
    print("-" * 75)
    print(f"{'CÓDIGO':<10}{'NOMBRE DEL PRODUCTO':<30}{'PRECIO (USD)':>15}{'STOCK':>10}")
    print("-" * 75)
    
    for codigo, nombre, precio, stock in lista_productos:
        # Asegurarse de que el precio se muestre con 2 decimales
        print(f"{codigo:<10}{nombre:<30}{precio:>15.2f}{stock:>10}")
        
    print("-" * 75)

# ===============================================
# FUNCIONES DE GESTIÓN (CRUD PRINCIPAL)
# ===============================================

def agregar_producto(inventario):
    print('\n---- AGREGAR NUEVO PRODUCTO ----')
    codigo = input('Introduzca el código del producto (Alfanumérico): ').strip()
    if not validar_codigo(codigo):
        print('ERROR: El código debe ser alfanumérico y sin espacios. Operación cancelada.')
        return
    producto_existente, _ = buscar_codigo(inventario, codigo)
    if producto_existente is not None:
        print(f'AVISO: El código "{codigo}" ya existe. Stock actual: {producto_existente[3]} unidades.')
        nuevo_stock = input('Introduzca la NUEVA cantidad total de producto: ').strip()
        if not validar_stcok(nuevo_stock): 
            print('ERROR: Cantidad de producto inválida. Debe ser un número entero. Operación cancelada.')
            return  
        stock = int(nuevo_stock)
        if stock < 0: 
            print('ERROR: El nuevo stock no puede ser negativo. Operación cancelada.')
            return
        producto_existente[3] = stock
        print(f'\nStock del producto "{producto_existente[1]}" actualizado a {stock} unidades.')
        return
    nombre_producto = input('Introduzca el nombre del producto: ').title()
    precio_str = input('Introduzca el precio del producto: ').strip()
    if not validar_precio(precio_str): 
        print('ERROR: Precio inválido.')
        return
    precio = float(precio_str)
    if precio <= 0:
        print('ERROR: El precio debe ser mayor que cero.')
        return
    stock_str = input('Introduzca cantidad del producto: ').strip()
    if not validar_stcok(stock_str): 
        print('ERROR: Cantidad de producto inválida.')
        return
    stock = int(stock_str)
    if stock < 0:
        print('ERROR: Cantidad de producto inválida.')
        return

    nuevo_producto = [codigo, nombre_producto, precio, stock]
    inventario.append(nuevo_producto)
    
    print(f'\n¡Producto "{nombre_producto}" ({codigo}) agregado exitosamente!')

# ===============================================
# FUNCIONES DE MODIFICACION
# ===============================================

def modificar_codigo(inventario):
    print('\n---- MODIFICAR CÓDIGO ----')
    codigo_actual = input('Introduzca el código ACTUAL del producto: ').strip()
    producto_a_modificar, indice = buscar_codigo(inventario, codigo_actual)
    if producto_a_modificar is None:
        print(f'ERROR: Código "{codigo_actual}" no encontrado.')
        return
    print(f'Producto encontrado: {producto_a_modificar[1]} (Código actual: {codigo_actual})')
    nuevo_codigo = input('Introduzca el NUEVO código para el producto: ').strip() # Corregido nombre de variable
    if not validar_codigo(nuevo_codigo): # Corregido uso de validación
        print('ERROR: Código inválido.')
        return
    seguridad = input(f'¿Confirma que desea cambiar el código de {producto_a_modificar[0]} a {nuevo_codigo}? (SI/NO): ').strip().lower()
    if seguridad == 'si':
        producto_a_modificar[0] = nuevo_codigo
        print(f'El código de "{producto_a_modificar[1]}" ha sido modificado a {nuevo_codigo}.')
    else:
        print('Operación cancelada por el usuario.')

def modificar_nombre(inventario):
    print('\n---- MODIFICAR NOMBRE ----')
    codigo = input('Introduzca el código del producto: ').strip()
    producto_a_modificar, indice = buscar_codigo(inventario, codigo)
    if producto_a_modificar is None:
        print(f'ERROR: Código "{codigo}" no encontrado.')
        return
    nombre_actual = producto_a_modificar[1]
    print(f'Producto Encontrado: {nombre_actual}')
    nuevo_nombre = input('Introduzca el nuevo nombre del producto: ').title()
    seguridad = input(f'¿Confirma que desea cambiar el nombre de {nombre_actual} a {nuevo_nombre}? (SI/NO): ').strip().lower()
    if seguridad == 'si':
        producto_a_modificar[1] = nuevo_nombre
        print(f'ÉXITO: El nombre del producto "{codigo}" ha sido modificado a "{nuevo_nombre}".')
    else:
        print('Operación cancelada por el usuario.')

def modificar_precio (inventario):
    print('\n---- MODIFICAR PRECIO ----')
    codigo_a_buscar = input('Introduzca el código del producto a modificar: ').strip()
    producto_a_modificar, indice = buscar_codigo(inventario, codigo_a_buscar)
    if producto_a_modificar is None:
        print(f'ERROR: Código "{codigo_a_buscar}" no encontrado.')
        return 
    nombre_producto = producto_a_modificar[1]
    precio_actual = producto_a_modificar[2]
    print(f'Producto encontrado: {nombre_producto} (Precio actual: {precio_actual})')
    nuevo_precio_str = input('Introduzca el NUEVO precio del producto: ').strip()
    if not validar_precio(nuevo_precio_str):
        print('ERROR: Precio inválido.')
        return
    nuevo_precio = float(nuevo_precio_str)
    if nuevo_precio <= 0:
        print('ERROR: precio inválido. ')
        return
    seguridad = input(f'¿Confirma que desea cambiar el precio de {nombre_producto} de {precio_actual} a {nuevo_precio}? (SI/NO): ').strip().lower()
    if seguridad == 'si':
        producto_a_modificar[2] = nuevo_precio
        print(f'ÉXITO: El precio de "{nombre_producto}" ha sido modificado a {nuevo_precio}.')
    else:
        print('Operación cancelada por el usuario.')

def modificar_stock(inventario):
    print('\n---- MODIFICAR STOCK ----')
    codigo_a_buscar = input('Introduzca el código del producto a modificar: ').strip()
    producto_a_modificar, indice = buscar_codigo(inventario, codigo_a_buscar)
    if producto_a_modificar is None:
        print(f'ERROR: Código "{codigo_a_buscar}" no encontrado.')
        return 
    nombre_producto = producto_a_modificar[1]
    stock_actual = producto_a_modificar[3]
    print(f'Producto encontrado: {nombre_producto} (Cantidad actual: {stock_actual})')
    nueva_cantidad= input('Introduzca la nueva cantidad  del producto: ').strip()
    if not validar_stcok(nueva_cantidad):
        print('ERROR: cantidad inválida.')
        return
    nuevo_stock = int(nueva_cantidad)
    if nuevo_stock <= 0:
        print('ERROR: cantidad inválida.')
        return
    seguridad = input(f'¿Confirma que desea cambiar la cantidad de {nombre_producto} de {stock_actual} a {nuevo_stock}? (SI/NO): ').strip().lower()
    if seguridad == 'si':
        producto_a_modificar[3] = nuevo_stock
        print(f'la cantidad de "{nombre_producto}" ha sido modificado a {nuevo_stock}.')
    else:
        print('Operación cancelada por el usuario.')

# ===============================================
# FUNCIONES DE Ordenamiento 
# ===============================================

def _merge_inventario(izquierda, derecha, indice_clave):
    resultado = []
    i = j = 0   
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i][indice_clave] < derecha[j][indice_clave]: 
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1          
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

def _mergesort_inventario(inventario_lista, indice_clave):
    if len(inventario_lista) <= 1:
        return inventario_lista
    punto_medio = len(inventario_lista) // 2
    mitad_izquierda = inventario_lista[:punto_medio]
    mitad_derecha = inventario_lista[punto_medio:]
    izquierda_ordenada = _mergesort_inventario(mitad_izquierda, indice_clave)
    derecha_ordenada = _mergesort_inventario(mitad_derecha, indice_clave)
    return _merge_inventario(izquierda_ordenada, derecha_ordenada, indice_clave)


def quicksort_inventario(arr, indice_clave):
    if len(arr) <= 1:
        return arr
    else:
        pivote_producto = arr[len(arr) // 2]
        pivote_valor = pivote_producto[indice_clave]
        izquierda = []
        centro = []
        derecha = []
        for producto in arr:
            if producto[indice_clave] < pivote_valor:
                izquierda.append(producto)
            elif producto[indice_clave] == pivote_valor:
                centro.append(producto)
            else:
                derecha.append(producto)
        return quicksort_inventario(izquierda, indice_clave) + centro + quicksort_inventario(derecha, indice_clave)

def ordenar_inventario(inventario):
    opcion_criterio = input('¿Desea ordenar por Código (1) o Nombre (2)?: ').strip()
    lista_a_ordenar = inventario[:]
    if opcion_criterio == '1':
        indice_clave = 0 
        print("\nOrdenando por Código.")
        return _mergesort_inventario(lista_a_ordenar, indice_clave)
    elif opcion_criterio == '2':
        indice_clave = 1
        print("\nOrdenando por Nombre.")
        return quicksort_inventario(lista_a_ordenar, indice_clave)
    else:
        print('\n Opción no válida. Mostrando todos los productos sin ordenar.')
        return inventario


# ===============================================
# BLOQUE DE EJECUCIÓN PRINCIPAL
# ===============================================

if __name__ == '__main__':
    # No se usa cargar_inventario, se usa la lista global inicial.
    salir = 'no'
    while salir != 'si':
        print(f'\n=== Simulador de Balanza ===')
        print(f'1. Mostrar Todos los productos.')
        print(f'2. Agregar Producto.')
        print(f'3. Buscar por código')
        print(f'4. Buscar por nombre.')
        print(f'5. Modificar producto')
        print(f'6. Eliminar producto.') 
        print(f'7. Venta.') 
        print(f'8. Salir')
        
        op = input(f'Elige una opcion: ').strip()

        if op == '1':
            print('\n---- Mostrar Inventario ----')
            inventario_a_mostrar = ordenar_inventario(inventario)
            mostrar_productos(inventario_a_mostrar)
            
        elif op == '2':
            agregar_producto(inventario)
            
        elif op == '3':
            print('\n---- BUSCAR POR CÓDIGO ----')
            codigo_a_buscar = input('Introduzca el código a buscar: ').strip()
            producto_encontrado, _ = buscar_codigo(inventario, codigo_a_buscar)
            
            if producto_encontrado:
                print(f'\nProducto Encontrado:')
                mostrar_productos([producto_encontrado])
            else:
                print(f'ERROR: Código "{codigo_a_buscar}" no encontrado.')
            
        elif op == '4':
            print(f'4. Buscar por nombre. ')
            buscar_por_nombre(inventario)
            
        elif op == '5':
            volver_menu_principal = 'no'
            while volver_menu_principal != 'si':
                print(f'\n---- Modificar producto----')
                print(f'1. Modificar nombre. ')
                print(f'2. Modificar precio.  ')
                print(f'3. Modificar Stock.')
                print(f'4. Modificar Código.')
                print(f'5. Volver al menú principal.')
                
                op2 = input('Seleccione una opcion: ').strip()
                
                if op2 == '1':
                    print('----Modificar Nombre---- ')
                    modificar_nombre(inventario)
                elif op2 == '2':
                    print('----Modificar Precio---- ')
                    modificar_precio(inventario)
                elif op2 == '3':
                    print('----Modificar Stock---- ')
                    modificar_stock(inventario)
                elif op2 == '4':
                    print('----Modificar Código---- ')
                    modificar_codigo(inventario)
                elif op2 == '5':
                    print('Regresando al menú principal...')
                    volver_menu_principal = 'si'
                else:
                    print('Opción No Válida. Intente de nuevo.')
                    
        elif op == '6':
            print(f'----Eliminar producto. (Función faltante)---- ')
            
        elif op == '7':
            print('----Ventas (Función faltante)---- ')
            
        elif op == '8':
            guardar_inventario(inventario)
            print("Saliendo del simulador. ¡Hasta pronto!")
            salir = 'si'
            
        else:
            print(f'Opción no válida. Por favor, elija un número del 1 al 8.')