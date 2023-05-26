import unittest

import os


class TestCase(unittest.TestCase):
    def test_check(self):
        self.assertIn('common',
                      os.listdir(os.getcwd()),
                      msg="Приложение common не создано")
        print("Приложение common создано")
