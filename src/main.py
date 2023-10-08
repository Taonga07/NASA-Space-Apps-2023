from json import dump, load
from random import randint
from PIL import Image
from ursina import *
import noise

class GameEngine:
    def __init__(self) -> None:
        pass
    def __call__(self, planet_data: dict) -> None:
        pass

class Oragnism:
    def __init__(self) -> None:
        self.temperature = [0,1]
        self.size = 0 

class Planet:
    def __init__(self) -> None:
        self.distance_from_sun = 1
        self.temperature = 1
        self.surface_pressure = 1
        self.sea_level = 0
        self.texture = 1
        self.mass = 1
        self.size = 100
    
    def generate_tetxure(self) -> Image:
        [int((noise.pnoise2(i / self.size,
                            j / self.size,
                            octaves=5
                            persistence=0.5
                            lacunarity=2.0,
                            base=random.randint(0,100),
                    ) + 1 ) * 128
                ) for i in range(4096)
            ] for j in range(2046)
        ]

if __name__ == "__main__":
    GameEngine()()