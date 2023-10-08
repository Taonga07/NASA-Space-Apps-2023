from ursina import *

class set:
    def __init__(self, pos_x:float, pos_y:float) -> None:
        self.pos:list[float, float] = [pos_x, pos_y]
        self.children: list[object, object] = self.create_set()
    def create_set(self) -> list[object, object]:
        button = Button(text='Size', color=color.gray, scale=.10, text_origin=(0,0), origin = self.pos)
        slider = ThinSlider(0, 20, default=10, y=self.pos[1], x=self.pos[0], step=1, horizontal=True)
        return [button, slider]
    def hidden(self, hidden:bool) -> None:
        for child in self.children:
            child.enabled=hidden

def minimize(b, item) -> None:
    if b.text == "+":
        b.text = "-"
        [set.hidden(False) for set in sets]
    if b.text == "-":
        b.text = "+"
        [set.hidden(True) for set in sets]
app = Ursina()
globe = Entity(model='sphere', color=color.white)
something = Entity(model='sphere', color=color.black,y=0.5,x=0.2,scale=0.1)
something = Entity(model='sphere', color=color.black,y=-0.5,x=0.2,scale=0.1)
button = Button(text='+', color=color.gray, scale=.05, text_origin=(0,0), origin = (17,-9))
button.tooltip = Tooltip('minimise')

sets = [set(8,-3), set(8,-1)]
def update():
    button.on_click = minimize(button, sets)
EditorCamera()
# start running the game
app.run()
