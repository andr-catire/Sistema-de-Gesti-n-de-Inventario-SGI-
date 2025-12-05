SISTEMA DE GESTIÓN DE INVENTARIO (SGI)
Este es un proyecto de simulación de un sistema básico de gestión de inventario para una tienda, desarrollado en Python, con un enfoque en la implementación de algoritmos de ordenamiento y persistencia de datos mediante archivos binarios.
CARACTERÍSTICAS PRINCIPALES
El sistema está diseñado para manejar la gestión completa de productos en la terminal, incluyendo las siguientes funcionalidades clave:

Gestión CRUD: Permite Crear (Agregar), Revisar (Mostrar), Update (Modificar) y Delete (Eliminar) productos.

Persistencia de Datos: El inventario se carga y guarda en un archivo binario (inventario.bin) utilizando la librería pickle, asegurando que los datos persistan entre sesiones.

Búsqueda Avanzada: Permite buscar productos por su código o mediante una palabra clave contenida en el nombre del producto.

Ventas/Descarga: Cuenta con una función para simular egreso (descarga) de productos del inventario (ventas), verificando la disponibilidad de stock.

Ordenamiento Avanzado: Implementación de dos algoritmos de ordenamiento vistos en clase para listar productos:

Mergesort: Utilizado para ordenar el inventario por Código (Alfanumérico).

Quicksort: Utilizado para ordenar el inventario por Nombre del producto.
REQUISITOS Y EJECUCIÓNRequisitosEste proyecto requiere Python 3.x y utiliza librerías estándar:Python 3.xLibrería pickle (para manejo de archivos binarios)Librería re (para validación de formatos, como el código alfanumérico)EjecuciónAsegúrate de tener Python 3 instalado en tu sistema.Navega hasta el directorio donde se encuentra el archivo principal de Python (ej. proyecto.py).Ejecuta la aplicación desde la terminal:Bashpython [Tu_Archivo_Principal].py
ESTRUCTURA DEL INVENTARIOEl inventario se gestiona mediante una lista de listas (matriz), donde cada producto sigue la siguiente estructura:ÍndiceCampoTipo de DatoCriterios/Uso0CódigoAlfanumérico (ej. F-A01)Clave para Mergesort1NombreStringClave para Quicksort2PrecioFlotantePrecio de venta3StockEnteroCantidad en inventarioMENÚ DE OPCIONESEl sistema opera a través de un menú principal interactivo en la terminal:Mostrar Todos los productos: Lista el inventario, permitiendo ordenar por Código (Mergesort) o Nombre (Quicksort).Agregar Producto: Permite ingresar un producto nuevo o actualizar la cantidad de uno existente.Buscar por código: Búsqueda exacta del producto.Buscar por nombre: Búsqueda por coincidencia de sub-cadena (palabra clave).Modificar producto: Sub-menú para actualizar el código, nombre, precio o stock.Eliminar producto.Venta: Simula la descarga de productos del inventario.Salir: Guarda los datos en el archivo binario y finaliza la aplicación.AUTOR:Andres Gonzalez; UCAB, Algoritmos y Programación]
