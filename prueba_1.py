import reflex as rx
#from Maderas.estilo.estilo import Style as estilo
#from Maderas.estilo.color import Color as Color
#from Maderas.estilo.color import text_color as text_color

def Prueba(title:str, body:str) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(
                title,
                font_weight="bold",
                color="black"
            ),
            
            
            f"  {body}",
            font_size="1",
            color="red"
        ) 
           
    )