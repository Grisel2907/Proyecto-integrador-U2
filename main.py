import flet as ft
from product_card import ProductCard

productos = [
    {"id": 1, "nombre": "Laptop Gamer",     "descripcion": "Ryzen 7, 16GB RAM, RTX 3060",     "precio": 25000, "ruta_imagen": "laptop.png"},
    {"id": 2, "nombre": "Mouse Gamer",      "descripcion": "Mouse inalámbrico RGB 16000 DPI",  "precio": 350,   "ruta_imagen": "mouse.png"},
    {"id": 3, "nombre": "Teclado Mecánico", "descripcion": "Switch blue, retroiluminado RGB",  "precio": 1200,  "ruta_imagen": "teclado.png"},
    {"id": 4, "nombre": "Audifonos Gamer",  "descripcion": "Sonido envolvente 7.1, microfono", "precio": 900,   "ruta_imagen": "audifonos.png"},
    {"id": 5, "nombre": "Monitor 24",       "descripcion": "Full HD 144Hz, 1ms, IPS",          "precio": 4200,  "ruta_imagen": "monitor.png"},
    {"id": 6, "nombre": "Silla Gamer",      "descripcion": "Reclinable 180, soporte lumbar",   "precio": 3800,  "ruta_imagen": "silla.png"},
]

def main(page: ft.Page):
    page.title      = "PixelShop"
    page.scroll     = "auto"
    page.bgcolor    = "#F0F2F8"
    page.padding    = 0
    page.assets_dir = "assets"

    carrito   = []
    favoritos = []

    carrito_count   = ft.Text("🛒 0", size=14, weight="bold", color="#3742FA")
    favoritos_count = ft.Text("❤️ 0", size=14, weight="bold", color="#FF4757")

    def mostrar_mensaje(msg, color="#3742FA"):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(msg, color="white", size=14),
            bgcolor=color
        )
        page.snack_bar.open = True
        page.update()

    def on_agregar(nombre, precio):
        carrito.append(nombre)
        carrito_count.value = f"🛒 {len(carrito)}"
        carrito_count.update()
        mostrar_mensaje(f"✅ {nombre} agregado al carrito")

    def on_favorito(nombre, es_fav):
        if es_fav:
            favoritos.append(nombre)
            mostrar_mensaje(f"❤️ {nombre} en favoritos", "#FF4757")
        else:
            if nombre in favoritos:
                favoritos.remove(nombre)
            mostrar_mensaje(f"🤍 {nombre} quitado de favoritos", "#747D8C")
        favoritos_count.value = f"❤️ {len(favoritos)}"
        favoritos_count.update()

    header = ft.Container(
        content=ft.Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                ft.Column(
                    spacing=2,
                    controls=[
                        ft.Text("💻 PixelShop", size=30, weight="bold", color="#2F3542"),
                        ft.Text("Catalogo de productos tecnologicos", size=13, color="#747D8C")
                    ]
                ),
                ft.Row(
                    spacing=12,
                    controls=[
                        ft.Container(
                            content=favoritos_count,
                            padding=10,
                            border_radius=10,
                            bgcolor="white",
                            border=ft.border.all(1, "#FFD6DD")
                        ),
                        ft.Container(
                            content=carrito_count,
                            padding=10,
                            border_radius=10,
                            bgcolor="white",
                            border=ft.border.all(1, "#C8CCFF")
                        ),
                    ]
                )
            ]
        ),
        padding=20,
        bgcolor="white",
        shadow=ft.BoxShadow(blur_radius=12, color="#12000000", offset=ft.Offset(0, 3))
    )

    titulo = ft.Container(
        content=ft.Column([
            ft.Text("Nuestros Productos", size=22, weight="bold", color="#2F3542"),
            ft.Text(f"{len(productos)} productos disponibles", size=13, color="#747D8C")
        ], spacing=2),
        padding=ft.padding.only(left=30, top=28, bottom=10)
    )

    tarjetas = [
        ProductCard(
            nombre      = p["nombre"],
            descripcion = p["descripcion"],
            precio      = p["precio"],
            imagen      = p["ruta_imagen"],
            on_agregar  = on_agregar,
            on_favorito = on_favorito
        )
        for p in productos
    ]

    grid = ft.Container(
        content=ft.Row(
            controls=tarjetas,
            wrap=True,
            spacing=22,
            run_spacing=22,
            alignment="start"
        ),
        padding=30
    )

    footer = ft.Container(
        content=ft.Text(
            "© 2026 PixelShop · Proyecto Integrador Unidad 2",
            size=12,
            color="#A4A8B0",
            text_align="center"
        ),
        padding=20
    )

    page.add(header, titulo, grid, footer)

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")