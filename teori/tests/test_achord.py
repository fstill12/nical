import unittest
from ..achord import rotate_left, gets_data_arr, rotate_array, achord

# Unit test
class TestMusicFunctions(unittest.TestCase):
    def setUp(self):
        self.NOTE_NAMES = ['C', 'Db', 'D', 'Eb', 'E', 'F',
                           'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

    def test_rotate_left(self):
        result = rotate_left(self.NOTE_NAMES, 2)
        expected = ['D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db']
        self.assertEqual(result, expected)

    def test_gets_data_arr_found(self):
        index = gets_data_arr(self.NOTE_NAMES, 'F')
        self.assertEqual(index, 5)

    def test_gets_data_arr_not_found(self):
        result = gets_data_arr(self.NOTE_NAMES, 'Z')
        self.assertEqual(result, self.NOTE_NAMES)

    def test_rotate_array(self):
        result = rotate_array(self.NOTE_NAMES, 'Eb')
        expected = ['Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D']
        self.assertEqual(result, expected)

    def test_achord(self):
        result = achord(self.NOTE_NAMES, 'C', [0, 4, 7, 10, 14])
        expected = ['C', 'E', 'G', 'Bb', 'D']  # 14 % 12 = 2 -> D
        self.assertEqual(result, expected)

# Menjalankan unit test
if __name__ == '__main__':
    unittest.main()
