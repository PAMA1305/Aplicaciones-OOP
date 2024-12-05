from nicegui import ui
from nicegui.events import ValueChangeEventArguments

def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')

ui.button('haz clic', on_click=lambda: ui.notify('clic'))
with ui.row():
    ui.checkbox('Checa la caja', on_change=show)
    ui.switch('Swichea', on_change=show)
ui.radio(['O', 'P', 'Q'], value='O', on_change=show).props('EN LINEA')
with ui.row():
    ui.input('ingresa texto', on_change=show)
    ui.select(['uno', 'dos'], value='uno', on_change=show)
ui.link('tienes mas...', '/documentation').classes('mt-8')

ui.run()