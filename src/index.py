from ursina import *

app = Ursina()

globe = Entity(model='sphere', color=color.white, scale_y=2)


def update():
    player.x += held_keys['d'] * time.dt
    player.x -= held_keys['a'] * time.dt

def input(key):
    if key == 'space':
        player.y += 1
        invoke(setattr, player, 'y', player.y-1, delay=.25)


# start running the game
app.run()

