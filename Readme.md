**Proyecto Integrador Unidad 2**  
Desarrollo de un Catálogo de Productos Reutilizable  
Materia: Tópicos Avanzados de Programación  
Instituto Tecnológico de Cuautla  

---|

## Descripción General

PixelShop es una aplicación de escritorio y web desarrollada con **Python** y el framework **Flet**. Muestra un catálogo de 6 productos tecnológicos donde cada producto se presenta en una tarjeta visual personalizada con imagen, nombre, descripción, precio y botones de acción (favorito y agregar al carrito).

El proyecto aplica el concepto de **componentes reutilizables** mediante la creación de una clase personalizada `ProductCard` que hereda de `ft.Container`, evitando la repetición de código y facilitando el mantenimiento.

---

## Estructura del Proyecto
```
PixelShop/
├── main.py              # Archivo principal: modelo de datos e interfaz
├── product_card.py      # Clase reutilizable ProductCard
├── assets/              # Carpeta de imágenes locales
│   ├── laptop.png       # Imagen de Laptop Gamer
│   ├── mouse.png        # Imagen de Mouse Gamer
│   ├── teclado.png      # Imagen de Teclado Mecánico
│   ├── audifonos.png    # Imagen de Audífonos Gamer
│   ├── monitor.png      # Imagen de Monitor 24"
│   └── silla.png        # Imagen de Silla Gamer
└── dist/                # Carpeta generada por flet publish (despliegue web)
```

---

## 1. 📊 Diagrama de Clases

El siguiente diagrama muestra cómo se relacionan las clases del proyecto:
```
                    ┌──────────────────────────────────┐
                    │          ft.Container            │
                    │       (Clase Base de Flet)       │
                    │                                  │
                    │  Propiedades heredadas:          │
                    │  + width                         │
                    │  + padding                       │
                    │  + border_radius                 │
                    │  + bgcolor                       │
                    │  + shadow                        │
                    │  + border                        │
                    │  + content                       │
                    │  + on_hover                      │
                    └──────────────┬───────────────────┘
                                   │
                                   │  «hereda»
                                   │
                    ┌──────────────▼───────────────────┐
                    │          ProductCard             │
                    │      (product_card.py)           │
                    ├──────────────────────────────────┤
                    │  ATRIBUTOS PROPIOS:              │
                    │  - nombre_producto : str         │
                    │  - _on_agregar : function        │
                    │  - _on_favorito : function       │
                    │  - _es_favorito : bool = False   │
                    │  - _fav_text : ft.Text           │
                    │  - _fav_btn : ft.Container       │
                    │  - _add_btn : ft.Container       │
                    ├──────────────────────────────────┤
                    │  ATRIBUTOS HEREDADOS:            │
                    │  - width = 260                   │
                    │  - padding = 15                  │
                    │  - border_radius = 16            │
                    │  - bgcolor = "white"             │
                    │  - shadow = ft.BoxShadow(...)    │
                    │  - border = ft.border.all(...)   │
                    ├──────────────────────────────────┤
                    │  MÉTODOS PROPIOS:                │
                    │  + __init__(nombre, descripcion, │
                    │    precio, imagen,               │
                    │    on_agregar, on_favorito)      │
                    │  + _hover(e) : void              │
                    │  + _favorito(e) : void           │
                    │  + _agregar(e) : void            │
                    └──────────────┬───────────────────┘
                                   │
                                   │  «instanciada en»
                                   │
                    ┌──────────────▼───────────────────┐
                    │             main.py              │
                    ├──────────────────────────────────┤
                    │  MODELO DE DATOS:                │
                    │  - productos : list[dict]        │
                    │    (id, nombre, descripcion,     │
                    │     precio, ruta_imagen)         │
                    │  - carrito : list                │
                    │  - favoritos : list              │
                    ├──────────────────────────────────┤
                    │  CONTROLES UI:                   │
                    │  - carrito_count : ft.Text       │
                    │  - favoritos_count : ft.Text     │
                    │  - header : ft.Container         │
                    │  - grid : ft.Container           │
                    │  - footer : ft.Container         │
                    ├──────────────────────────────────┤
                    │  FUNCIONES:                      │
                    │  + main(page) : void             │
                    │  + on_agregar(nombre, precio)    │
                    │  + on_favorito(nombre, es_fav)   │
                    │  + mostrar_mensaje(msg, color)   │
                    └──────────────────────────────────┘
```

### Explicación del diagrama:

- **`ft.Container`** es la clase base que provee Flet. Tiene propiedades visuales como ancho, padding, colores y sombras.
- **`ProductCard`** hereda de `ft.Container` y agrega su propia lógica para mostrar un producto específico.
- **`main.py`** instancia (crea) una `ProductCard` por cada producto del arreglo usando un ciclo `for`.

---

## 2. Explicación de la Herencia

### ¿Qué es la herencia?

La herencia es un principio de la Programación Orientada a Objetos (POO) que permite crear una clase nueva basada en una clase existente. La clase nueva **hereda** todas las propiedades y métodos de la clase padre, y puede agregar los suyos propios.

### ¿Qué clase base se utilizó?

Se utilizó **`ft.Container`** como clase base. Esta clase de Flet es un contenedor visual que puede:
- Tener dimensiones fijas (`width`, `height`)
- Tener estilos visuales (`bgcolor`, `border_radius`, `shadow`, `border`)
- Contener otros controles dentro (`content`)
- Detectar eventos del mouse (`on_hover`, `on_click`)

### ¿Cómo se implementó?
```python
# product_card.py

import flet as ft

class ProductCard(ft.Container):   # ← ProductCard hereda de ft.Container
    def __init__(self, nombre, descripcion, precio, imagen,
                 on_agregar=None, on_favorito=None):
        
        super().__init__()   # ← Llama al constructor de ft.Container
                             #   Esto inicializa todas las propiedades heredadas
        
        # Atributos propios de ProductCard
        self.nombre_producto = nombre
        self._on_agregar     = on_agregar
        self._on_favorito    = on_favorito
        self._es_favorito    = False
        
        # Propiedades heredadas de ft.Container que se personalizan
        self.width         = 260        # Ancho fijo para uniformidad
        self.padding       = 15         # Espacio interno
        self.border_radius = 16         # Bordes redondeados
        self.bgcolor       = "white"    # Fondo blanco
        self.border        = ft.border.all(1, "#E8ECF0")  # Borde sutil
        self.shadow        = ft.BoxShadow(               # Sombra suave
            blur_radius=14,
            color="#1A000000",
            offset=ft.Offset(2, 4)
        )
        self.on_hover = self._hover     # Evento al pasar el mouse
```

### ¿Por qué es mejor usar herencia que repetir código?

| Sin herencia ❌ | Con herencia ✅ |
|----------------|----------------|
| Se repite el mismo código de tarjeta 6 veces | Se crea UNA clase y se instancia 6 veces |
| Si hay un cambio, hay que modificar 6 lugares | Si hay un cambio, solo se modifica la clase |
| Código largo y difícil de mantener | Código limpio y reutilizable |

---

## 3.  Gestión de Recursos (carpeta assets)

### ¿Qué es la carpeta assets?

La carpeta `assets/` es un directorio local donde se almacenan los recursos estáticos de la aplicación, en este caso las imágenes de los productos.

### ¿Cómo se configura en Flet?

Se configura en **dos lugares** dentro de `main.py`:
```python
# 1. Dentro de la función main(), para que la página reconozca la carpeta
def main(page: ft.Page):
    page.assets_dir = "assets"

# 2. Al ejecutar la app, para el modo web también
if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
```

### ¿Cómo se referencia cada imagen?

En el modelo de datos, cada producto tiene una clave `ruta_imagen` con el nombre del archivo:
```python
productos = [
    {
        "id": 1,
        "nombre": "Laptop Gamer",
        "descripcion": "Ryzen 7, 16GB RAM, RTX 3060",
        "precio": 25000,
        "ruta_imagen": "laptop.png"    # ← nombre del archivo en /assets
    },
    {
        "id": 2,
        "nombre": "Mouse Gamer",
        "descripcion": "Mouse inalámbrico RGB 16000 DPI",
        "precio": 350,
        "ruta_imagen": "mouse.png"     # ← nombre del archivo en /assets
    },
    # ... más productos
]
```

En `ProductCard`, la imagen se carga con `ft.Image`:
```python
ft.Image(
    src=imagen,      # recibe el valor de ruta_imagen, ej: "laptop.png"
    width=230,
    height=150,
    fit="cover",     # la imagen cubre todo el espacio sin distorsionarse
)
```

Flet busca automáticamente `laptop.png` dentro de la carpeta `assets/` configurada.

### ¿Qué pasa si no encuentra la imagen?

Se muestra un placeholder con un ícono y el texto "Sin imagen":
```python
error_content=ft.Container(
    content=ft.Column([
        ft.Text("🖼️", size=40),
        ft.Text("Sin imagen", size=11, color="#AAAAAA")
    ]),
    bgcolor="#F4F5F7",
)
```

---
## Despliegue en Netlify

### ¿Qué es Netlify?
Netlify es una plataforma gratuita que permite publicar aplicaciones web en internet con solo arrastrar una carpeta.

### ¿Cómo se preparó la app para web?

Flet permite convertir una aplicación de escritorio en web usando el comando `flet publish`. Este comando genera una carpeta `dist/` con todos los archivos necesarios para el despliegue.

Se ejecutó el siguiente comando en la terminal dentro de la carpeta del proyecto:
```bash
flet publish main.py
```

Esto generó automáticamente:
- `dist/index.html` — página principal
- `dist/manifest.json` — configuración de la app
- `dist/version.json` — versión de Flet
- `dist/app.tar.gz` — código comprimido de la app

### Pasos para desplegar en Netlify:

**Paso 1** — Entrar a [netlify.com](https://netlify.com) e iniciar sesión

**Paso 2** — En el panel principal ir a:
```
Sites → Add new project → Deploy manually
```

**Paso 3** — Arrastrar la carpeta `dist/` generada por `flet publish` a la zona de deploy de Netlify

**Paso 4** — Netlify procesa los archivos automáticamente y genera un link único:
```
https://nombre-aleatorio.netlify.app
```

**Paso 5** — Se puede personalizar el nombre del sitio desde:
```
Site configuration → Site details → Change site name
```

### Resultado:
La app quedó disponible públicamente en internet sin necesidad de un servidor propio.

## 4.  Capturas de Pantalla

### Interfaz principal con los 6 productos:
<img width="1363" height="713" alt="Captura1" src="https://github.com/user-attachments/assets/79c3df97-7f02-4bb6-a29f-c80ea380553a" />


### Agregar producto al carrito:
<img width="73" height="71" alt="Captura2" src="https://github.com/user-attachments/assets/2ff89e37-7f25-4722-a5e7-4717103ce5b2" />


### Botón favorito activo (corazón rojo):
<img width="71" height="68" alt="Captura3" src="https://github.com/user-attachments/assets/d09a0b95-06b7-449a-b98f-6c644d98194e" />


### Contador de carrito actualizado:
<img width="63" height="78" alt="Captura4" src="https://github.com/user-attachments/assets/86c78666-50e6-418b-9e76-c6dd001fe297" />

---

## 5. Preparación para el Futuro 

El código está diseñado de forma **modular** para que despues solo se necesite cambiar la fuente de datos, sin modificar la interfaz ni el componente `ProductCard`.

### Estructura actual — datos locales:
```python
# main.py - los datos están hardcodeados en el código
productos = [
    {"id": 1, "nombre": "Laptop Gamer", "precio": 25000, ...},
    {"id": 2, "nombre": "Mouse Gamer",  "precio": 350,   ...},
]
```

### Estructura futura  — datos desde API:
```python
# main.py - solo se cambia esta parte
import requests
productos = requests.get("https://api.pixelshop.com/productos").json()

# O desde una base de datos
import sqlite3
conn = sqlite3.connect("productos.db")
productos = conn.execute("SELECT * FROM productos").fetchall()
```

`ProductCard`, el encabezado, el grid y toda la interfaz **no necesitan ningún cambio** porque reciben los datos como parámetros, no los tienen hardcodeados.

---

##  Tecnologías Utilizadas

| Tecnología | Versión | Uso en el proyecto |
|-----------|---------|-------------------|
| Python | 3.x | Lenguaje de programación principal |
| Flet | 0.82.0 | Framework para crear la interfaz gráfica |
| Git | - | Control de versiones del código |
| GitHub | - | Repositorio remoto del proyecto |
| Netlify | - | Despliegue de la app en web |

---

##  Cómo ejecutar el proyecto

### Requisitos:
- Python 3.x instalado
- Flet 0.82.0

### Pasos:
```bash
# 1. Clona el repositorio
git clone https://github.com/Grisel2907/Proyecto-integrador-U2.git

# 2. Entra a la carpeta
cd Proyecto-integrador-U2

# 3. Instala Flet
pip install flet==0.82.0

# 4. Ejecuta la app
python main.py
```

---

## 🔗 Links

- 🐙 **GitHub:** https://github.com/Grisel2907/Proyecto-integrador-U2
- 🌐 **Netlify:** https://cosmic-strudel-b0f7c8.netlify.app/

---

**Alumna:** Grisel Pliego   
**Materia:** Tópicos Avanzados de Programación  
**Semestre:** 4to  
**Instituto Tecnológico de Cuautla — TecNM**
