# tests/test_basic.py
import unittest
from src.compressor import compress_data, decompress_data

class TestCompressor(unittest.TestCase):

    def test_alpha_compression(self):
        data = "hello"
        compressed = compress_data(data, mode="alpha")
        self.assertTrue(compressed[0] != data[0])  # flag present
        self.assertEqual(decompress_data(compressed), data)

    def test_num_compression(self):
        data = "12345"
        compressed = compress_data(data, mode="num")
        self.assertTrue(compressed[0] != data[0])  # flag present
        self.assertEqual(str(decompress_data(compressed)), data)

    def test_invalid_alpha(self):
        with self.assertRaises(ValueError):
            compress_data("abc123", mode="alpha")
    def test_invalid_num(self):
        with self.assertRaises(ValueError):
            compress_data("12a3", mode="num")


if __name__ == "__main__":
    unittest.main()
