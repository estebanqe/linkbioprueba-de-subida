import reflex as rx
from pruebadeerrores.info_text import info_text
from pruebadeerrores.prueba_1 import Prueba


class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.vstack(
        rx.flex(
            info_text("+4", "años de experiencia"),
            rx.spacer(),  # Espacio entre texto
            info_text("atención", "al detalle"),
            rx.spacer(),  # Espacio adicional
            info_text("trabajo", "certificado"),
            width="100%",
            # spacing="1"  # Espaciado entre elementos del flexbox
        ),
        rx.flex(
            Prueba("+4", "años de experiencia"),
            rx.spacer(),  # Espacio entre texto
            Prueba("atención", "al detalle"),
            rx.spacer(),  # Espacio adicional
            Prueba("trabajo", "certificado"),
            width="100%",
            # spacing="1"  # Espaciado entre elementos del flexbox
        ),    
    )

app = rx.App()  # Corrige la creación de app
app.add_page(index)