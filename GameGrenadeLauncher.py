from GameWeapon import Weapon


class GrenadeLauncher(Weapon):
    arc_of_grenade_being_launched = 0
    angle_of_launcher = 0
    blast_radius = 10
    bounce_off_walls = True
    bounce_off_soils = False

    # methods: assume they are the same as Weapons class
    def change_angle_of_launcher(self):
        pass