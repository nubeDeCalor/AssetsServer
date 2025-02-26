import flet as ft
from flet_assets import AssetsServer

server = AssetsServer(directory="src/assets")


def main(page: ft.Page):
    audio = ft.Audio(src=f"{server.assets}/mp3/anime/yamate.mp3")
    page.overlay.append(audio)
    page.add(
        ft.Image(src=f"{server.assets}/icon.png", width=200, height=200),
        ft.Button("Play", on_click=lambda _: audio.play()),
    )


ft.app(main, view=ft.AppView.WEB_BROWSER)
