def runcamera(y=4):
    """Advanced smooth chase camera with inertia & immersion effects"""

    global previous_speed

    if cockpit_view:
        cockpit_pos = (
            plane.world_position
            + plane.up * 1.35
            + plane.forward * 1.8
        )
        camera.position = lerp(camera.position, cockpit_pos, time.dt * 12)
        camera.rotation = lerp(camera.rotation, plane.world_rotation, time.dt * 10)
        camera.fov = lerp(camera.fov, 78, time.dt * 4)

        if 'cockpit_model' in globals():
            cockpit_model.visible = cockpit_model.enabled
        return

    if 'cockpit_model' in globals():
        cockpit_model.visible = False

    desired_pos = plane.position - Vec3(
        math.sin(math.radians(plane.rotation_y)) * camera_offset.z,
        -camera_offset.y,
        math.cos(math.radians(plane.rotation_y)) * camera_offset.z
    )

    g_force = Lift / (mass * g) if mass > 0 and 'Lift' in globals() else 1

    lag_multiplier = clamp(g_force * 0.15, 0, 1.5)

    follow_speed = y - lag_multiplier

    camera.position = lerp(
        camera.position,
        desired_pos,
        time.dt * follow_speed
    )

    camera.look_at(
        lerp(camera.world_position + camera.forward * 10,
             plane.world_position,
             time.dt * y)
    )

    bank_factor = clamp(plane.rotation_z / 45, -1, 1)
    camera.x += bank_factor * 0.02

    base_fov = 90
    max_extra_fov = 20

    speed_ratio = clamp(speed / 600, 0, 1)
    target_fov = base_fov + max_extra_fov * speed_ratio

    camera.fov = lerp(camera.fov, target_fov, time.dt * 2)

    if speed > 400:
        shake_intensity = (speed - 400) / 2000
        camera.position += Vec3(
            random.uniform(-shake_intensity, shake_intensity),
            random.uniform(-shake_intensity, shake_intensity),
            0
        )



def runmissile():
    if missiles:
        camera.position = missiles[0].position - Vec3(
            math.sin(math.radians(plane.rotation_y)) * camera_offset.z,
            -camera_offset.y,
            math.cos(math.radians(plane.rotation_y)) * camera_offset.z
        )
        camera.look_at(missiles[0])

