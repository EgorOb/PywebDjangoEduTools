import unittest

import os


class TestCase(unittest.TestCase):
    def test_check(self):
        cwd = os.getcwd()
        os.chdir('project')
        print("Папка с проектом", os.getcwd())
        print("Файлы в проекте", os.listdir(os.getcwd()))
        self.assertIn('manage.py',
                      os.listdir(os.getcwd()),
                      msg="Проект не создан")
        print("Проект создан")
