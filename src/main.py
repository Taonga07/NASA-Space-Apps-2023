from ursina import *

class PlanetGenerator(WindowPanel):
    def __init__(self):
        super().__init__(
            title="Planet Generator",
            content=[self], 
            width=400,
            height=400,
            parent=scene,
        )
        self.enabled = False 

    def toggle_panel(self):
        self.enabled = not self.enabled

    def generate_planet(self):

        return Entity(
            model='sphere',
            texture=f'texture{1}.png',  # needs to set to generate texture
            color=color.white,
            position=(0, 0, -distance_from_sun)
        )

    def get_planet_entity(self):
        if self.planet is None:
            self.planet = self.generate_planet()
        return self.planet


class PanelToggle(Button):
    def __init__(self) -> None:
        super().__init__(
            text='+',
            color=color.gray,
            scale=0.05,
            origin=(17, -9),
            on_click=self.toggle_panel
        )

    def toggle_panel(self):
        planet_generator.toggle_panel()
        if self.text == '+':
            self.text = '-'
        else:
            self.text = '+'


if __name__ == "__main__":
    app = Ursina()

    planet_generator = PlanetGenerator()
    panel_toggle = PanelToggle()

    EditorCamera()

    app.run()
