import unittest
from ..apps import RunChord, RunScale, RunAnalyze

class TestRunChord(unittest.TestCase):
    def setUp(self):
        self.args = {
            "tuts": "C",
            "notasi": "sharp",
            "interval": "mayor",
            "verbose": False
        }
        self.chord = RunChord(args=self.args)

    def test_validate_string(self):
        self.assertTrue(self.chord.validate_string())

    def test_olah_data(self):
        data = self.chord.olah_data()
        self.assertIn("judul", data)
        self.assertIn("kunci", data)
        self.assertIn("notasi", data)
        self.assertIn("tangga_nada", data)

class TestRunScale(unittest.TestCase):
    def setUp(self):
        self.args = {
            "tuts": "C",
            "notasi": "flat",
            "interval": "minor",
            "verbose": True
        }
        self.scale = RunScale(args=self.args)

    def test_validate_string(self):
        self.assertTrue(self.scale.validate_string())

    def test_buat_interval(self):
        interval = self.scale.buat_interval("minor")
        self.assertEqual(interval["nama_interval"], "minor")
        self.assertIsInstance(interval["interval"], list)

class TestRunAnalyze(unittest.TestCase):
    def setUp(self):
        self.args = {
            "tuts": "C E G",
            "notasi": "sharp"
        }
        self.analyze = RunAnalyze(args=self.args)

    def test_validate_string(self):
        self.assertTrue(self.analyze.validate_string())

    def test_cek_akor(self):
        result = self.analyze.cek_akor("C E G")
        self.assertIsInstance(result, list)
        self.assertGreaterEqual(len(result), 1)

if __name__ == "__main__":
    unittest.main()
