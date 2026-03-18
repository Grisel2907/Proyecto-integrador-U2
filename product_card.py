import flet as ft

class ProductCard(ft.Container):
    def __init__(self, nombre, descripcion, precio, imagen,
                 on_agregar=None, on_favorito=None):
        super().__init__()

        self.nombre_producto = nombre
        self._on_agregar     = on_agregar
        self._on_favorito    = on_favorito
        self._es_favorito    = False

        self.width         = 260
        self.padding       = 15
        self.border_radius = 16
        self.bgcolor       = "white"
        self.border        = ft.border.all(1, "#E8ECF0")
        self.shadow        = ft.BoxShadow(
            blur_radius=14,
            color="#1A000000",
            offset=ft.Offset(2, 4)
        )
        self.on_hover = self._hover

        self._fav_text = ft.Text("🤍", size=20)
        self._fav_btn  = ft.Container(
            content=self._fav_text,
            on_click=self._favorito,
            padding=ft.padding.all(6),
            border_radius=8,
            bgcolor="#FFF0F3"
        )

        self._add_btn = ft.Container(
            content=ft.Row([
                ft.Text("🛒", size=14),
                ft.Text("Agregar", color="white", size=12, weight="bold")
            ], spacing=5, tight=True),
            bgcolor="#3742FA",
            padding=ft.padding.symmetric(horizontal=12, vertical=8),
            border_radius=8,
            on_click=self._agregar
        )

        self.content = ft.Column(
            spacing=10,
            horizontal_alignment="center",
            controls=[
                ft.Image(
                    src=imagen,
                    width=230,
                    height=150,
                    fit="cover",
                    border_radius=10,
                ),
                ft.Text(
                    nombre,
                    size=17,
                    weight="bold",
                    color="#2F3542",
                    text_align="center",
                    max_lines=2,
                    overflow="ellipsis"
                ),
                ft.Text(
                    descripcion,
                    size=12,
                    color="#747D8C",
                    text_align="center",
                    max_lines=2,
                    overflow="ellipsis"
                ),
                ft.Text(
                    f"${precio:,.2f}",
                    size=18,
                    weight="bold",
                    color="#2ED573",
                    text_align="center"
                ),
                ft.Container(
                    content=ft.Row(
                        alignment="spaceBetween",
                        vertical_alignment="center",
                        controls=[self._fav_btn, self._add_btn]
                    ),
                    width=230,
                    padding=ft.padding.only(top=4)
                )
            ]
        )

    def _hover(self, e):
        self.bgcolor = "#F0F3FF" if e.data == "true" else "white"
        self.update()

    def _favorito(self, e):
        self._es_favorito = not self._es_favorito
        self._fav_text.value  = "❤️" if self._es_favorito else "🤍"
        self._fav_btn.bgcolor = "#FFD6DD" if self._es_favorito else "#FFF0F3"
        self._fav_text.update()
        self._fav_btn.update()
        if self._on_favorito:
            self._on_favorito(self.nombre_producto, self._es_favorito)

    def _agregar(self, e):
        if self._on_agregar:
            self._on_agregar(self.nombre_producto, 0)