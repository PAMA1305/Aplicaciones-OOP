from nicegui import ui

class Demo:
    def __init__(self):
        self.number = 1

demo = Demo()
v = ui.checkbox('visible', value=True)
with ui.column().bind_visibility_from(v, 'evalua'):
    ui.slider(min=1, max=3).bind_value(demo, 'numero')
    ui.toggle({1: '10', 2: '20', 3: '30'}).bind_value(demo, 'numero')
    ui.number().bind_value(demo, 'numero')

ui.run()