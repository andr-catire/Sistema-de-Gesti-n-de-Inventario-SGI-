🛒 Sistema de Gestión de Inventario (SGI)
Este proyecto simula un sistema básico de gestión de inventario para una tienda, desarrollado en Python. Su enfoque principal es la implementación de algoritmos de ordenamiento avanzados y la persistencia de datos mediante archivos binarios.

✨ Características Principales
El sistema está diseñado para manejar la gestión completa de productos a través de la terminal, incluyendo las siguientes funcionalidades clave:

Gestión CRUD (Crear, Revisar, Actualizar, Eliminar): Permite la administración completa de los productos.

Crear (Agregar): Permite registrar un producto nuevo o actualizar el stock de uno existente.

Revisar (Mostrar): Lista el inventario, con opciones de ordenamiento.

Update (Modificar): Permite actualizar el código, nombre, precio o stock de un producto.

Delete (Eliminar): Permite dar de baja un producto.

Persistencia de Datos: El inventario se carga y se guarda en un archivo binario (inventario.bin) utilizando la librería pickle, asegurando la persistencia de los datos entre diferentes sesiones de uso.

Búsqueda Avanzada: Permite buscar productos de forma específica por su código o mediante una palabra clave contenida en el nombre del producto.

Ventas / Descarga: Incluye una función para simular el egreso (descarga) de productos del inventario (ventas), verificando la disponibilidad de stock antes de realizar la operación.

Ordenamiento Avanzado: Implementación de dos algoritmos de ordenamiento vistos en clase para listar los productos:

Mergesort: Utilizado para ordenar el inventario por Código (Alfanumérico).

Quicksort: Utilizado para ordenar el inventario por Nombre del producto.

📦 Estructura de Datos del Producto
El inventario se gestiona mediante una lista de listas (matriz). Cada producto es una lista que mantiene la siguiente información en orden:

Código: Alfanumérico (ej. F-A01). Es la clave para el ordenamiento Mergesort.

Nombre: String. Es la clave para el ordenamiento Quicksort.

Precio: Flotante (Precio de venta).

Stock: Entero (Cantidad en inventario).

⚙️ Requisitos y Ejecución
Requisitos
Este proyecto requiere Python 3.x y utiliza las siguientes librerías estándar:

Python 3.x

Librería pickle (para el manejo de archivos binarios).

Librería re (para la validación de formatos, como el código alfanumérico).

Ejecución
Asegúrate de tener Python 3 instalado en tu sistema.

Navega hasta el directorio donde se encuentra el archivo principal de Python (ej. proyecto.py).

Ejecuta la aplicación desde la terminal con el siguiente comando:

Bash

python [Tu_Archivo_Principal].py
💻 Menú de Opciones
El sistema opera a través de un menú principal interactivo en la terminal, que ofrece las siguientes opciones:

Mostrar Todos los productos: Lista el inventario, permitiendo ordenar por Código (Mergesort) o Nombre (Quicksort).

Agregar Producto: Permite ingresar un producto nuevo o actualizar el stock de uno existente.

Buscar por código: Búsqueda exacta de un producto por su código.

Buscar por nombre: Búsqueda por coincidencia de sub-cadena (palabra clave).

Modificar producto: Sub-menú para actualizar el código, nombre, precio o stock.

Eliminar producto.

Venta: Simula la descarga de productos del inventario.

Salir: Guarda los datos en el archivo binario (inventario.bin) y finaliza la aplicación.

Autor: Andres Gonzalez; UCAB, Algoritmos y Programación
