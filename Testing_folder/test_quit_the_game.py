import unittest
from io import StringIO
from unittest.mock import patch


def player_choice():
    option = input('Do you want to quite the game: yes or no?')
    if option == 'yes':
        print('you entered yes')
    if option == 'no':
        print('you entered no')


class MyTestCase(unittest.TestCase):
    def runTest(self, given_answer, expected_out):
        with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=StringIO()) as fake_out:
            player_choice()
            self.assertEqual(fake_out.getvalue().strip(), expected_out)

    def test_yes(self):
        self.runTest('yes', 'you entered yes')

    def test_no(self):
        self.runTest('no', 'you entered no')
    
if __name__ == '__main__':
    unittest.main()