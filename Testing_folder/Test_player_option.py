import unittest
from io import StringIO
from unittest.mock import patch


def player_choice(): 
    option = input('enter rock, paper or scissors') # player enters the input here
    if option == 'rock':
        print('you entered rock') #software should display this when the user enters 'rock'
    if option == 'paper':
        print('you entered paper')
    if option == 'scissors':
        print('you entered scissors')


class MyTestCase(unittest.TestCase):
    def runTest(self, given_answer, expected_out):
        with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=StringIO()) as fake_out:
            player_choice()
            self.assertEqual(fake_out.getvalue().strip(), expected_out)
        # stringIO module is an in-memory file-like object

    def test_rock(self):
        self.runTest('rock', 'you entered rock')

    def test_paper(self):
        self.runTest('paper', 'you entered paper')

    def test_scissors(self):
        self.runTest('scissors', 'you entered scissors')

if __name__ == '__main__':
    unittest.main()