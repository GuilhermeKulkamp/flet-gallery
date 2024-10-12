import flet as ft
import asyncio

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLACK12

    async def animate(e = None):
        while True:
            #img.offset.y=-0.3
            img.rotate.angle = 4
            img.update()
            await asyncio.sleep(5)
            #img.offset.y=0
            img.rotate.angle = 0
            img.update()
            await asyncio.sleep(5)


    img = ft.Image(
        src = "assets/fruto-da-terra-logo.png",
        #offset= ft.Offset(x=0,y=0),
        rotate= ft.Rotate(angle=0),
        animate_rotation= ft.Animation(duration=5000, curve=ft.AnimationCurve.LINEAR),
        #animate_offset= ft.Animation(duration=4000, curve=ft.AnimationCurve.EASE),
    )

    page.add(img)


    page.run_task(animate)
    

if __name__ == '__main__':
    ft.app(target=main)

