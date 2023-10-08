from PIL import Image
import noise, json


class ProceduralTerrain:
    def __init__(self, shape) -> None:
        self.noise_array = [[0 for _ in range(shape[0])] for _ in range(shape[1])]
        self.sea_level = 0

    def noise_to_colour(self, layers, shape) -> list:
        altitudes = [int(layer[1] + self.sea_level) for layer in layers]
        colours = [list(layer[0]) for layer in layers]

        colour_indices = [
            [
                next(i for i, alt in enumerate(altitudes) if alt > noise)
                for noise in array
            ]
            for array in self.noise_array
        ]
        colour_array = [[colours[ind] for ind in array] for array in colour_indices]

        return colour_array

    def get_random_noise(self, slider_settings) -> list:
        return [ [ 
                int(
                    ( noise.pnoise2(
                            i / slider_settings["scale"],
                            j / slider_settings["scale"],
                            octaves=slider_settings["octaves"],
                            persistence=slider_settings["persistence"],
                            lacunarity=slider_settings["lacunarity"],
                            base=slider_settings["seed"],
                    ) + 1 ) * 128
                ) for i in range(len(self.noise_array[0]))
            ] for j in range(len(self.noise_array[0]))
        ]

    def array_to_image(colour_array, shape):
        image = Image.new("RGB", shape)
        for x, row in enumerate(colour_array):
            for y, pixel in enumerate(row):
                image.putpixel((x, y), tuple(pixel))
        return image

    def generate_landscape(change):
        shape = (200, 200)
        noise_array = self.get_random_noise(slider_settings, shape)
        colour_array = self.noise_to_colour(
            noise_array, self.slider_settings["sea_level"].value, layers, shape
        )
        image = self.array_to_image(colour_array, shape)
        # image = noise_to_image(noise_array, shape)
        self.render_image(image)
