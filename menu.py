from ursina import *
from panda3d.core import MovieTexture



app = Ursina()
window.fullscreen = True
window.show_ursina_splash = True
window.borderless = True
window.vsync = True
window.color = color.rgb(0, 0, 0)
window.title = "Flight Simulator - Dogfight Mode"


movie = MovieTexture("hangar_video")
success = movie.read("models/hangar.mp4")


if success:
    movie.set_loop(True)
    movie.play()


aspect_ratio = window.aspect_ratio

background = Entity(
    parent=camera.ui,
    model='quad',
    scale=(1 * aspect_ratio, 1),
    texture=movie,
    z=1
)
transparent_black = color.rgba(0, 0, 0, 0.5)
overlay = Entity(
    model='quad',
    color=transparent_black,  
    scale=(16 * aspect_ratio, 9),
    z=0.5
)
start_button = Button(
    text="START MISSION",
    scale=(0.3, 0.1),
    position=(0, 0.1),
    z=0,
    color=color.azure
)

start_button.on_click = lambda: start_game()
def start_game():
    app.destroy()

camera.orthographic = True
camera.fov = 16
def update():
    start_button.scale = (0.3 + math.sin(time.time()*2)*0.01, 0.1)


app.run()