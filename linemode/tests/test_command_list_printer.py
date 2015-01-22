import unittest

from linemode.drivers.command_list import compile


class TestCommandListPrinter(unittest.TestCase):
    def test_simple_command(self):
        program = compile([
            "reset"
        ])
        self.assertEqual(program, b'reset')
