class Weapon():
    aps = 1

    def __init__(self, min_dmg, max_dmg, strength, ele_type, ele_dmg):
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.strength = strength
        self.ele_type = ele_type
        self.ele_mod = ele_dmg / 100
    
    def get_min_dmg(self, str_mod, use_ele_mod):
        return self.min_dmg * (self.ele_mod + str_mod) if use_ele_mod else self.min_dmg * str_mod

    def get_max_dmg(self, str_mod, use_ele_mod):
        return self.max_dmg * (self.ele_mod + str_mod) if use_ele_mod else self.max_dmg * str_mod

    def get_dps(self, min_dmg, max_dmg, aps):
        return (min_dmg + max_dmg) / 2 * aps

    def get_damage_dict(self, pc_lvl):
        strength = (pc_lvl * 10 / 100) + (self.strength / 100)
        damageDict = {}
        damageDict["Punch"] = self.get_attack_dict("physical", 1, 1, strength)
        damageDict["Smite"] = self.get_attack_dict("fire", .9, 1.2, strength)
        damageDict["Cleave"] = self.get_attack_dict("ice", 1.2, .9, strength)
        return damageDict

    def get_attack_dict(self, element, dmg_mod, aps_mod, str_mod):
        use_ele_mod = self.ele_type == element
        atk_min_dmg = self.get_min_dmg(str_mod, use_ele_mod) * dmg_mod
        atk_max_dmg = self.get_max_dmg(str_mod, use_ele_mod) * dmg_mod

        return Weapon.build_atk_dict(atk_min_dmg, atk_max_dmg, self.get_dps(atk_min_dmg, atk_max_dmg, self.aps * aps_mod))

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