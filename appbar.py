import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE
    page.theme_mode = ft.ThemeMode.DARK
    page.title = 'Navegações'
    page.window_width = 450
    page.window_height = 700

    page.horizontal_alignment = page.vertical_alignment = "center"
    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD,bgcolor=ft.colors.BLUE_ACCENT_700)
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    def btn_main(e):
        _stack_main.controls.clear()
        _stack_main.controls.append(_main)
        _stack_main.update()

    def btn_edit(e):
        _stack_main.controls.clear()
        _stack_main.controls.append(editar)
        _stack_main.update()

    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.WHITE70,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.HOME, icon_color=ft.colors.BLUE_ACCENT,icon_size=32, on_click=btn_main),
                ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.BLUE_ACCENT,icon_size=32),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.icons.EDIT, icon_color=ft.colors.BLUE_ACCENT,icon_size=32,on_click=btn_edit),
                ft.IconButton(icon=ft.icons.DELETE, icon_color=ft.colors.BLUE_ACCENT,icon_size=32),
            ]    
        )
    )

    #container principal
    _main = ft.Container(
        width=400,
        height=600,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.WHITE70,
        border_radius=16,
        shadow=ft.BoxShadow(blur_radius=10,color=ft.colors.with_opacity(opacity=0.5,color=ft.colors.BLACK)),
        content= ft.Text(
            value="INÍCIO",
            color=ft.colors.BLACK,
            size=32,
        )
    )

    #container editar
    editar = ft.Container(
        width=400,
        height=600,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.WHITE70,
        border_radius=16,
        shadow=ft.BoxShadow(blur_radius=10,color=ft.colors.with_opacity(opacity=0.5,color=ft.colors.BLACK)),
        content= ft.Text(
            value="EDITAR",
            color=ft.colors.BLACK,
            size=32,
        )
    )

    #stack principal
    _stack_main = ft.Stack(
        controls=[
            _main,
        ]
        )

    page.add(_stack_main)

if __name__ == '__main__':
    ft.app(target=main)