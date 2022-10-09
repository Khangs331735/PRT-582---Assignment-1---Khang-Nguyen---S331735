import random
import unittest


options = ['rock', 'paper', 'scissors']

def computer_choice():
    return random.choice(options)

class test_computer_choice(unittest.TestCase):
    def test_choice(self):
        self.assertTrue(computer_choice(), 'rock')
        self.assertTrue(computer_choice(), 'paper')
        self.assertTrue(computer_choice(), 'scissors')

if __name__ == '__main__':
    unittest.main()
