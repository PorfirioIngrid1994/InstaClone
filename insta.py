import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLACK

    def clicked(e):
        e.control.selected = not e.control.selected
        e.control.update()

    layout = ft.Container(
        bgcolor=ft.colors.WHITE,
        width=500,
        border_radius=ft.border_radius.all(10),
        shadow=ft.BoxShadow(blur_radius=50, color=ft.colors.TEAL),
        content=ft.Column(
            spacing=0,
            controls=[
                ft.ListTile(
                    title=ft.Text(value="Discovery Furry", color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                    subtitle=ft.Text(value="Panda-Vermelho? Oi?", color=ft.colors.BLACK),
                    leading=ft.Image(
                        src="C:\\Users\\Ingrid\\Desktop\\pandaaa.png",
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    trailing=ft.Icon(name=ft.icons.MORE_HORIZ, color=ft.colors.BLACK)
                ),
                ft.Image(
                    src="C:\\Users\\Ingrid\\Desktop\\panda.jpg",
                    fit=ft.ImageFit.CONTAIN,
                ),
                ft.Container(
                    padding=ft.padding.all(15),
                    content=ft.Column(
                        controls=[
                            ft.ResponsiveRow(
                                columns=12,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.IconButton(
                                        col=1,
                                        icon=ft.icons.FAVORITE_BORDER,
                                        selected_icon=ft.icons.FAVORITE,
                                        selected=False,
                                        on_click=clicked,
                                        icon_color=ft.colors.BLACK,
                                        selected_icon_color=ft.colors.RED
                                    ),
                                    ft.Icon(
                                        col=1,
                                        name=ft.icons.CHAT_BUBBLE_OUTLINE,
                                        color=ft.colors.BLACK,
                                    ),
                                    ft.Icon(
                                        col=1,
                                        name=ft.icons.SEND,
                                        color=ft.colors.BLACK,
                                    ),
                                    ft.Container(col=8),
                                    ft.IconButton(
                                        col=1,
                                        icon=ft.icons.BOOKMARK_BORDER,
                                        selected_icon=ft.icons.BOOKMARK_ROUNDED,
                                        selected=False,
                                        on_click=clicked,
                                        icon_color=ft.colors.BLACK,
                                        selected_icon_color=ft.colors.BLUE,
                                    )
                                ]
                            ),
                            ft.Text(
                                value='Pandas vermelhos e gigantes: apesar da semelhança, são como primos distantes! '
                                      'Enquanto o panda gigante é da família dos ursos, o panda vermelho é mais "raiz" '
                                      'e está na turma dos guaxinins. É a prova de que na natureza, até os parentescos '
                                      'têm suas surpresas! 🐼🌿 #ParentescoSurpreendente',
                                color=ft.colors.BLACK,
                                size=16,
                            ),
                            ft.Text(
                                value='Há 5 dias',
                                color=ft.colors.GREY,
                                size=14,
                                offset=ft.Offset(x=0, y=-0.5),
                            ),
                            ft.Text(
                                spans=[
                                    ft.TextSpan(text='DanielNasc1989 ', style=ft.TextStyle(color=ft.colors.BLACK, size=16)),
                                    ft.TextSpan(text='Surpreendente, não imaginava!', style=ft.TextStyle(color=ft.colors.BLACK, weight=ft.FontWeight.BOLD)),
                                ]
                            ),
                            ft.Text(
                                value='Ver todos os 2.024 comentários',
                                color=ft.colors.GREY,
                                size=14,
                            ),
                            ft.TextField(
                                hint_text='Adicione seu comentário...',
                                hint_style=ft.TextStyle(color=ft.colors.GREY, size=16),
                                border=ft.InputBorder.UNDERLINE,
                                border_color=ft.colors.GREY,
                                border_width=1,
                                color=ft.colors.BLACK,
                            )
                        ]
                    )
                )
            ]
        )
    )

    page.add(layout)

if __name__ == "__main__":
    ft.app(target=main)
