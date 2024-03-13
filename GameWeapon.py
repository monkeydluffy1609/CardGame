"""
Weapon Object
Grenades (lethal/tactical)
Grenade Launcher
Knives
Rifle
Scope
Machine Gun

"""


class Weapon:                       # why would a player choose one gun over another?

    number_of_bullets = 0
    type_of_bullets = None
    amount_of_damage_per_shot = 0   # assume 10 HP (health points) is default damage value
    fire_rate = 1                   # how many shots can be made in 1 second
    range_of_shot = 100             # every 100 years amount of damage is reduced by 25
    stability = 0                   # like recoil when not shooting
    recoil = 0                      # ability to have the gun shake/vibrate/move less after fire
    weight_of_weapon = 0            # consequences of weight over loading
    scope_zoom = 1                  # magnification of 1x
    price = 100                     # in coins

    # methods: what does the weapon do?
    def reload(self):
        pass

    def shoot(self):
        pass

    def aim(self):
        pass

    def change_zoom(self):
        pass

    def depreciate_price(self):
        pass


class Grenade(Weapon):
    pass