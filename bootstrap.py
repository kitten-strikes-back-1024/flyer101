from ursina import *
from ursina import Quat
import random, math, time
import os, sys
from ursina.prefabs.trail_renderer import TrailRenderer
import socket, json, threading, uuid
import json, time
game_paused = True
def start_game():
    global game_paused
    game_paused = False
y = 4
Text.default_font = "models/orbitron.ttf"

def load_missions(path="missions/missions.json"):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    missions_data = data.get("missions", [])
    if not isinstance(missions_data, list):
        raise ValueError("missions.json format error: 'missions' must be a list")
    return missions_data


def _build_mission_briefing_text(selected_mission):
    objective_lines = []
    for i, objective in enumerate(selected_mission.get("objectives", []), start=1):
        objective_text = objective.get("description", "No objective description")
        objective_lines.append(f"{i}. {objective_text}")

    objectives_block = "\n".join(objective_lines) if objective_lines else "No objectives"
    return (
        f"\n=== MISSION BRIEFING ===\n"
        f"Mission: {selected_mission.get('name', 'Unknown Mission')}\n\n"
        f"Briefing: {selected_mission.get('description', 'No briefing available')}\n\n"
        f"Objectives:\n{objectives_block}"
    )


missions = load_missions()
if not missions:
    raise ValueError("No missions found in missions/missions.json")

mission = random.choice(missions).copy()
mission["objectives"] = [obj.copy() for obj in mission.get("objectives", [])]



missiles = []
enemy_planes = []
flares = []
# Offscreen enemy arrows (HUD)
offscreen_arrows = {}
game_over = False

editor_mode = False
editor_cam = None

cockpit_view = False  # Toggle between external & cockpit view

# Initialize Ursina App
app = Ursina()
window.fullscreen = True
window.show_ursina_splash = True
window.borderless = True
window.vsync = True
window.color = color.rgb(0, 0, 0)
window.title = "Flight Simulator - Dogfight Mode"


def restart_game():
    os.execl(sys.executable, sys.executable, *sys.argv)


black_overlay = Entity(
    parent=camera.ui,
    model='quad',
    scale=(2, 2),
    color=color.black,
    z=-1
)


# HUD text
displayed = Text(
    "",
    parent=camera.ui,
    position=window.center - Vec2(0.5, 0),
    z=-2,
    origin=(-0.5, 0),
    scale=1.3,
    color=color.rgb(0, 255, 100)
)




def typewriter_text(text, base_delay=0.015):
    seq = Sequence()
    displayed.text = ""

    for char in text:
        seq.append(Func(lambda c=char: setattr(displayed, "text", displayed.text + c)))

        if char in ".!?":
            delay = base_delay * 10
        elif char in ",:;":
            delay = base_delay * 5
        elif char == "\n":
            delay = base_delay * 15
        else:
            delay = base_delay

        seq.append(Wait(delay + random.uniform(0, base_delay * 0.5)))

    return seq


def add_text(t):
    displayed.text += t
def clear_displayed():
    displayed.text = ""
def game_intro():
    global game_paused
    game_paused = True

    briefing_text = _build_mission_briefing_text(mission)
    displayed.text = ""

    Sequence(
        Wait(3),
        typewriter_text(briefing_text, base_delay=0.03),
        Wait(10),
        Func(start_game),  
        Wait(10),
        Func(clear_displayed),
        Func(lambda: black_overlay.animate_color(color.rgba(0,0,0,0), duration=2))

    ).start()

invoke(game_intro)
mission_start_time = time.time()
#Physics Constants
g = 9.81  # Gravity (m/s²)
vertical_velocity = 0  # Vertical velocity (m/s)
rho0 = 1.225  # Air density at sea level (kg/m³)
H = 8000  # Scale height for atmosphere (m)
S = 27.87  # Wing area of F-16 (m²)
Sf = 28  # Reference area for drag
mass = 12000  # Max takeoff weight (kg)
T_max = 129000  # Max thrust of F-16 (N)
Cd0 = 0.03  # Zero-lift drag coefficient
k = 0.07  # Induced drag factor
CL0 = 0.2  # Lift coefficient at zero AoA
CL_alpha = 0.12  # Lift curve slope per degree
missile_weight = 85  # Missile weight (kg)
missile_velocity = 300  # Missile speed (m/s)

# Combat Variables
player_health = 100
missile_count = 50
flare_count = 50
gun_ammo = 500
locked_target = None
target_index = 0
lock_progress = 0
lock_time_required = 2.0  # Seconds to achieve lock
is_locking = False
radar_range = 5000
lock_tone_playing = False
radar_enabled = True  # Toggle radar display
# Load Textures & Sounds
runway_texture = load_texture('models/runway.jpg')
cockpit_texture = load_texture('models/cockpit.png')
grass_texture = load_texture('models/terraiin.jpg')
wmap = load_texture('models/no-zoom.jpeg')
plane_engine = Audio('models/plane_engine.mp3', loop=True, volume=0.1, autoplay=True)
crash_sound = Audio('models/crash.mp3', autoplay=False)
terrain_warning = Audio('models/terrain.mp3', autoplay=False)
explosion = Audio('models/explosion.mp3', autoplay=False)
#check for mp3 files ending in "music"
matched_files = []
    # Loop through files in the directory
suffix = "music.mp3"
for filename in os.listdir("models"):

    if filename.lower().endswith(suffix.lower()):
        matched_files.append(os.path.join("/models", filename))
x = len(matched_files)
bgm = Audio(random.choice(matched_files), autoplay=True, loop=True)

