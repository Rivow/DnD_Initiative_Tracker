import unittest
from Initiative_Tracker import *


class TestTracker(unittest.TestCase):

    def test_check_if_integer_false(self):
        self.assertFalse(check_if_inter('e'), 'Expected to return False when something other than Integer is given')

    def test_if_inter_true(self):
        self.assertTrue(check_if_inter(2), 'Expected to return True when something other than Integer is given')

    #def test_enemy_dic_size(self):
    #    actual = len(number_per_typ(5))
    #    expected = 5
    #    self.assertEqual(actual, expected, 'Expected length of dictonary to be 5')

    def test_dice_roll_range_max(self):
        max = 21
        for i in range(0, 100):
            roll = enemy_initiative(0)
            self.assertLess(roll, max, 'Dice Roll expected to be at max 20')

    def test_dice_roll_range_min(self):
        min = 0
        for i in range(0, 100):
            roll = enemy_initiative(0)
            self.assertGreater(roll, min, 'Dice Roll expected to be at min 1')

    def test_dice_roll_complete_range(self):
        roll_range = []
        for i in range(1, 21):
            roll_range.append(i)

        for j in range(0, 100):
            roll = enemy_initiative(0)
            if roll in roll_range:
                roll_range.remove(roll)

        self.assertEqual(len(roll_range), 0, f'Missing numbers from roll: {roll_range}')

    def test_dice_roll_range_max_with_initbonus(self):
        max = 21 + 3
        for i in range(0, 100):
            roll = enemy_initiative(3)
            self.assertLess(roll, max, 'Initiative expected to be at max 23')

    def test_dice_roll_range_min_with_initbonus(self):
        min = 0
        for i in range(0, 100):
            roll = enemy_initiative(5)
            self.assertGreater(roll, min, 'Initiative expected to be at min 6')




