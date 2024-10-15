import flet as ft

def main(page: ft.Page):
    page .bgcolor = ft.colors.BLACK87
    page.theme_mode = ft.ThemeMode.DARK
    page.title = 'Navegações'
    page.window_width = 450
    page.window_height = 700

    page.horizontal_alignment = page.vertical_alignment = "center"
    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD,bgcolor=ft.colors.BLUE_ACCENT_700)
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.WHITE70,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.EDIT, icon_color=ft.colors.BLUE_ACCENT,icon_size=32),
                ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.BLUE_ACCENT,icon_size=32),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.icons.SHARE, icon_color=ft.colors.BLUE_ACCENT,icon_size=32),
                ft.IconButton(icon=ft.icons.SETTINGS, icon_color=ft.colors.BLUE_ACCENT,icon_size=32),
            ]
      
        )
    )

    #container principal
    _main = ft.Container(
        width=400,
        height=600,
        bgcolor=ft.colors.WHITE70,
        border_radius=16,
    )

    #stack principal
    _stack_main = ft.Stack(
        controls=[
            _main
        ]
        )
    

    page.add(_stack_main)

if __name__ == '__main__':
    ft.app(target=main)