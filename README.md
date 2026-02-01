# Flight Simulator - Dogfight Mode

A 3D multiplayer combat flight simulator built with Python and Ursina Engine, featuring realistic flight physics, AI-powered enemy aircraft, and intense dogfighting action.

![Game Mode](https://img.shields.io/badge/Mode-Dogfight-red)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Engine](https://img.shields.io/badge/Engine-Ursina-green)

## Features

### Flight Mechanics
- **Realistic Physics**: Advanced aerodynamics simulation including lift, drag, thrust, and atmospheric density calculations
- **Multiple Aircraft Models**: Choose from F-16, Tinker, AC-130, F-167, and X-Wing
- **Dynamic Controls**: Pitch, yaw, throttle control with stall mechanics
- **Autopilot Mode**: Automated flight assistance
- **Dual Camera Views**: External chase camera and immersive cockpit view

### Combat Systems
- **Heat-Seeking Missiles**: Advanced tracking system with flare countermeasures (20 missiles)
- **Machine Gun**: 500 rounds of ammunition for close-range combat
- **Flare Dispensers**: 10 flares to distract incoming missiles
- **Target Lock System**: Progressive lock-on with 2-second acquisition time
- **Radar System**: 5000m range with sweep animation and enemy tracking
- **Health System**: Take damage from enemy fire and impacts

### AI Enemies
- **Intelligent Behavior**: Four-state AI (patrol, engage, circle, evade)
- **Dynamic Tactics**: Enemies adapt based on distance and player position
- **Missile Combat**: AI aircraft fire heat-seeking missiles with lead calculation
- **Formation Flying**: Enemies coordinate to maintain tactical advantage

### Visual Effects
- **3D Explosions**: Multi-stage explosions with fireball, debris, and smoke
- **Missile Trails**: Color-gradient exhaust trails
- **Environmental Lighting**: Dynamic sun and directional shadows
- **Particle Systems**: Flares, explosions, and atmospheric effects

### UI & HUD
- **Comprehensive HUD**: Speed, altitude, throttle, health, ammo counters
- **Radar Display**: Circular radar with enemy markers and distance indicators
- **Target Lock Indicators**: Visual brackets and lock progress bar
- **Warning Systems**: Missile warnings, terrain alerts, stall notifications
- **Mini-Map**: Real-time tactical overview with enemy positions
- **Artificial Horizon**: Orientation reference for instrument flying

### Multiplayer
- **Network Play**: Connect to server for multiplayer dogfights
- **Ghost Players**: See other players' aircraft in real-time
- **Synchronized Missiles**: Network missile tracking across clients

### World Features
- **Multiple Airports**: BLR, ICN, and HND with runways, taxiways, and terminals
- **Terrain Elements**: Mountains, water bodies, and textured ground
- **Night Sky**: Atmospheric skybox with celestial textures

## Controls

### Flight Controls
| Key | Action |
|-----|--------|
| `W` | Pitch Down |
| `S` | Pitch Up |
| `A` | Yaw Left |
| `D` | Yaw Right |
| `Q` | Increase Throttle |
| `E` | Decrease Throttle |
| `O` | Emergency Stop (Zero Throttle) |

### Combat Controls
| Key | Action |
|-----|--------|
| `M` | Fire Missile (when locked) |
| `F` | Deploy Flare |
| `G` | Fire Gun |
| `T` | Lock Next Target |
| `R` | Lock Previous Target |
| `B` | Break Lock |

### Camera & View
| Key | Action |
|-----|--------|
| `C` | Toggle Cockpit View |
| `Z` | Zoom In |
| `X` | Zoom Out |
| `V` | Reset Camera |
| `P` (hold) | Missile Camera |

### System Controls
| Key | Action |
|-----|--------|
| `H` | Toggle Radar |
| `N` | Spawn 3 Enemy Aircraft |
| `F1` | Toggle Editor Mode |
| `ESC` | Quit Game |
| `Space` | Save Current Position |

### Debug Controls
| Key | Action |
|-----|--------|
| `L` | Test Explosion Effect |
| `I` | Reset Ground Position |

## Installation

### Prerequisites
```bash
pip install ursina --break-system-packages
```

### Required Assets
Place the following files in a `models/` directory:
- **Textures**: `runway.jpg`, `cockpit.png`, `terraiin.jpg`, `no-zoom.jpeg`, `rocks.jpg`, `night.jpg`
- **3D Models**: `f16`, `tinker`, `ac130`, `f167`, `xwing`, `missile`
- **Audio**: `plane_engine.mp3`, `crash.mp3`, `terrain.mp3`, `explosion.mp3`, `battle-music.mp3`, `epic-music.mp3`, `chase-music.mp3`

### Running the Game
```bash
python flight_simulator.py
```

The game will start after a 5-second countdown.

## Gameplay Guide

### Starting Out
1. Game launches in fullscreen mode at an airport (BLR)
2. Use `Q` to increase throttle and begin takeoff
3. Pull back (`S`) to lift off when speed reaches ~100

### Engaging Enemies
1. Press `N` to spawn enemy aircraft
2. Use `T` to cycle through targets within radar range (5000m)
3. Keep target in your crosshairs for 2 seconds to achieve lock
4. Fire missiles with `M` when "LOCKED" indicator appears
5. Deploy flares (`F`) when under missile attack

### Combat Tips
- **Energy Management**: Maintain speed above 100 to avoid stalling
- **Defensive Flying**: Use `F` flares early when warned of incoming missiles
- **Positioning**: Circle enemies at 800-1200m range for optimal firing
- **Altitude**: Keep above 100m to avoid terrain warnings
- **Awareness**: Watch the radar for enemy positions and threats

### AI Behavior
- **Patrol**: Enemies circle at long range (1500m+)
- **Engage**: Close to medium range (750-1500m) and maneuver for shots
- **Circle**: Orbit at 1000m to maintain visual and firing position
- **Evade**: Break away when too close (<300m) to avoid collision

## Multiplayer Setup

### Server Configuration
Default server settings:
- **IP**: `127.0.0.1` (localhost)
- **Port**: `5050`

To connect to a remote server, modify these lines:
```python
SERVER_IP = "your.server.ip"
SERVER_PORT = 5050
```

### Running Offline
If no server is available, the game automatically runs in offline mode.

## Physics Model

The simulator uses real-world F-16 specifications:
- **Mass**: 12,000 kg (max takeoff weight)
- **Wing Area**: 27.87 m²
- **Max Thrust**: 129,000 N
- **Drag Coefficients**: Cd0 = 0.03, k = 0.07
- **Lift Model**: Based on angle of attack with stall characteristics
- **Atmospheric Model**: Exponential air density decay (scale height 8000m)

## Technical Details

### Performance
- **VSync**: Enabled for smooth frame delivery
- **Physics Rate**: Real-time delta updates
- **Missile Speed**: 600-750 m/s
- **AI Update Rate**: 60 FPS (frame-dependent)

### Known Limitations
- Collision detection limited to mesh colliders
- Network play requires external server implementation
- Terrain is simplified (flat with placed obstacles)

## Troubleshooting

**Game won't start**: Ensure all asset files are in the `models/` directory

**No sound**: Check that audio files are properly formatted MP3s

**Network connection failed**: Server must be running separately; game continues in offline mode

**Low FPS**: Reduce enemy count or disable shadows in lighting setup

**Stall on takeoff**: Increase throttle to 100% and maintain pitch <20° until airspeed >100

## Credits

Built with the Ursina Engine for Python. Flight physics based on F-16 Fighting Falcon aerodynamic data.

## License

Open source project - feel free to modify and enhance!

---

**Good hunting, pilot! 🛩️**
