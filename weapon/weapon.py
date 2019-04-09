class Weapon():
    aps = 1

    def __init__(self, min_dmg, max_dmg, strength, ele_type, ele_dmg):
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.strength = strength
        self.ele_type = ele_type
        self.ele_mod = ele_dmg / 100

    def get_damage_dict(self, pc_lvl):
        strength = (pc_lvl * 10 / 100) + (self.strength / 100)
        damageDict = {}
        damageDict["Punch"] = self.get_attack_dict("physical", 1, 1, strength)
        damageDict["Smite"] = self.get_attack_dict("fire", .9, 1.2, strength)
        damageDict["Cleave"] = self.get_attack_dict("ice", 1.2, .9, strength)
        return damageDict

    def get_attack_dict(self, element, dmg_mod, aps_mod, str_mod):
        use_ele_mod = self.ele_type == element and self.ele_mod > 0
        atk_min_dmg = Weapon.get_damage(self.min_dmg, str_mod, dmg_mod, self.ele_mod, use_ele_mod)
        atk_max_dmg = Weapon.get_damage(self.max_dmg, str_mod, dmg_mod, self.ele_mod, use_ele_mod)
        dps = (atk_min_dmg + atk_max_dmg) / 2 * (self.aps * aps_mod)

        return Weapon.build_atk_dict(atk_min_dmg, atk_max_dmg, dps)

    @staticmethod
    def get_damage(dmg, str_mod, dmg_mod, ele_mod, use_ele_mod):
        return (dmg * (ele_mod + str_mod) if use_ele_mod else dmg * str_mod) * dmg_mod

    @staticmethod
    def build_atk_dict(min_dmg, max_dmg, dps):
        atkDict = {}
        atkDict["Minimum"] = min_dmg
        atkDict["Maximum"] = max_dmg
        atkDict["DPS"]  = dps
        return atkDict

class Mace(Weapon):
    aps = 1

class Axe(Weapon):
    aps = 1.2

class Sword(Weapon):
    aps = 1.4