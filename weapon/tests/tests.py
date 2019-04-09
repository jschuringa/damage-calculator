import unittest
from weapon import weapon
class TestCalculator(unittest.TestCase):

    def test_type_does_more_damage(self):
        """
            Asserts attack with matching weapon type does more damage
        """
        axe_with_fire = weapon.Axe(10, 20, 5, "fire", 10)
        axe_without_fire = weapon.Axe(10, 20, 5, "ice", 10)
        aws = axe_with_fire.get_attack_dict("fire", 1, 1, 1)
        awos = axe_without_fire.get_attack_dict("fire", 1, 1, 1)
        self.assertGreater(aws["DPS"], awos["DPS"])

    def test_class_aps_multipliers(self):
        """
            Asserts weapon with equal stats but higher APS does more DPS
        """
        axe = weapon.Axe(10, 20, 5, "fire", 10).get_attack_dict("ice", 1, 1, 1)
        sword = weapon.Sword(10, 20, 5, "fire", 10).get_attack_dict("ice", 1, 1, 1)
        mace = weapon.Mace(10, 20, 5, "fire", 10).get_attack_dict("ice", 1, 1, 1)
        self.assertGreater(axe["DPS"], mace["DPS"])
        self.assertGreater(sword["DPS"], axe["DPS"])

    def test_get_dmg(self):
        """
            Asserts get_dmg properly calculates value
        """
        damage = weapon.Weapon.get_damage(10, 1, 1, 1, 0)
        self.assertEqual(damage, 10)

    def test_build_atk_dict(self):
        """
            Asserts build_akt_dict builds properly
        """
        atk_dict = weapon.Weapon.build_atk_dict(10, 20, 15)
        self.assertEqual(atk_dict["Minimum"], 10)
        self.assertEqual(atk_dict["Maximum"], 20)
        self.assertEqual(atk_dict["DPS"], 15)

    def test_provided_test_case(self):
        """
            Asserts provided test case. 
            Uses almost equal due to possible rounding differences
        """
        axe = weapon.Axe(50, 65, 20, "fire", 10)
        damage = axe.get_damage_dict(10)
        punch = damage["Punch"]
        smite = damage["Smite"]
        cleave = damage["Cleave"]

        self.assertAlmostEqual(60, punch["Minimum"], delta=2)
        self.assertAlmostEqual(78, punch["Maximum"], delta=2)
        self.assertAlmostEqual(82.8, punch["DPS"], delta=2)
        
        self.assertAlmostEqual(59.4, smite["Minimum"], delta=2)
        self.assertAlmostEqual(77.22, smite["Maximum"], delta=2)
        self.assertAlmostEqual(98.366, smite["DPS"], delta=2)

        self.assertAlmostEqual(72, cleave["Minimum"], delta=2)
        self.assertAlmostEqual(93.6, cleave["Maximum"], delta=2)
        self.assertAlmostEqual(89.424, cleave["DPS"], delta=2)

if __name__ == '__main__':
    unittest.main()