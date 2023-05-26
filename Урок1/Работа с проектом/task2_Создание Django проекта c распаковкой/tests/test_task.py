import unittest
import os


class TestCase(unittest.TestCase):
    def test_check(self):
        cwd = os.getcwd()
        print("Папка с проектом", cwd)
        print("Файлы в проекте", os.listdir(cwd))
        self.assertIn('manage.py',
                      os.listdir(cwd),
                      msg="Проект не создан")
        print("Проект создан")

