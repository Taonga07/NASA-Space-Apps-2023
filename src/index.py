from ursina import *

app = Ursina()
globe = Entity(model='sphere', color=color.white, heightmap = 'Image')

b = Button(text='Size', color=color.gray, scale=.10, text_origin=(0,0), origin = (8,-4))
b.on_click = application.quit # assign a function to the button.
b.tooltip = Tooltip('exit')

slider = Slider(0, 20, default=10, height=Text.size*3, y=0.3, x=-0.85, step=1, horizontal=True)

b = Button(text='Temperature', color=color.gray, scale=.10, text_origin=(0,0), origin = (8,-2))
b.on_click = application.quit # assign a function to the button.
b.tooltip = Tooltip('exit')

slider = Slider(0, 20, default=10, height=Text.size*3, y=0.1, x=-0.85, step=1, horizontal=True)

b = Button(text='Gravity', color=color.gray, scale=.10, text_origin=(0,0), origin = (8,0))
b.on_click = application.quit # assign a function to the button.
b.tooltip = Tooltip('exit')

slider = Slider(0, 20, default=10, height=Text.size*3, y=-.1, x=-0.85, step=1, horizontal=True)

EditorCamera()
# start running the game
app.run()
