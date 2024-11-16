import file_reader
import unittest
import weather_functions
import random

from pathlib import Path

class TestSum(unittest.TestCase):
    def test_empty_list(self):
        """
        Tests that an empty list as a parameter to when_is_it_spring returns an invalid index: -1
        """
        temp_list = []
        spring_index = weather_functions.when_is_it_spring(temp_list)

        message = 'Expected -1 to be returned for empty list'
        self.assertEqual(spring_index, -1, message)

    def test_zeroes_list(self):
        """
        Tests than a list of only zeroes as a parameter to when_is_it_spring will return an invalid index: -1
        """
        temp_list = [0]*365
        spring_index = weather_functions.when_is_it_spring(temp_list)

        message = 'Only values larger than zero should be counted'
        self.assertEqual(spring_index, -1, message)

    def test_rand_neg(self):
        """
        Tests that the function returns -1 for a list of negative temperatures pulled at random
        """
        temp_list = [random.randrange(-10, 0) for n in range(40)]

        spring_index = weather_functions.when_is_it_spring(temp_list)

        message = 'Only values larger than zero should be counted'
        self.assertEqual(spring_index, -1, message)

    def test_few_pos_temps(self):
        """
        Tests that a for a list with 3 pos temps at the end, the index that is returned is -1
        """
        temp_list = [-1] * 10 + [4] * 3
        spring_index = weather_functions.when_is_it_spring(temp_list)

        message = 'Too few positive temperatures to find the beginning of spring!'
        self.assertEqual(spring_index, -1, message)


    def test_reset_at_zero(self):
        """
        Tests that the counter in when_is_it_spring is reset when the temperature is 0 degrees
        """
        temp_list = [0, 1, 2, 3, 4, 5, 6, 0, 8, 9, 10, 11, 12, 13, 14]
        spring_index = weather_functions.when_is_it_spring(temp_list)

        message = 'All variables should be reset when the temperature is at or below 0 degrees C'
        self.assertEqual(spring_index, 8, message)

    def test_reset_at_negative(self):
        """
        Tests that the counter in when_is_it_spring is reset when the temperature is negative
        """
        temp_list = [0, 1, 2, 3, 4, 5, 6, -1, 8, 9, 10, 11, 12, 13, 14]
        spring_index = weather_functions.when_is_it_spring(temp_list)

        message = 'All variables should be reset when the temperature is at or below 0 degrees C'
        self.assertEqual(spring_index, 8, message)

    def test_all_months(self):
        """
        Tests that the correct value is returned from when_is_it_spring for every month
        """
        path = Path(__file__).parent / 'temperature_data.csv'

        month_answers = {'Full year': 11, 'January': 11, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 'July': 0, 'August': 0, 'September': 0, 'October': 0, 'November': 0, 'December': 24}
        month_nbr = 0

        for key in month_answers:
            temp_list = file_reader.read_from_file(path, month_nbr)
            spring_index = weather_functions.when_is_it_spring(temp_list)
            month_nbr += 1

            message = f'Month {key} failed. Expected index {month_answers[key]}, got index {spring_index}'
            self.assertEqual(spring_index, month_answers[key], message)

if __name__ == '__main__':
    unittest.main()
