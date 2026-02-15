sun = Entity(
    model='sphere',
    color=color.yellow,
    scale=15,
    position=(10000, 10000, -300),
    emissive=True
)

sunlight = DirectionalLight(shadows=True)

# Spawn initial enemies
spawn_enemies(5)

