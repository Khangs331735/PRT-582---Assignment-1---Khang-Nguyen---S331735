import unittest

def count_score_ties(self, player, computer):
    ties = 0
    if player == computer:
        ties += 1
        return ties

def count_score_wins(self, player, computer):
    wins = 0
    if player == 'rock':
        if computer == "scissors":
            wins += 1
            return wins
    elif player == 'paper':
        if computer == "rock":
            wins += 1
            return wins
    elif player == "scissors":
        if computer == "paper":
            wins += 1
            return wins

def count_score_loses(self, player, computer):
    loses = 0
    if player == 'rock':
        if computer == "paper":
            loses += 1
            return loses
    elif player == 'paper':
        if computer == "scissors":
            loses += 1
            return loses
    elif player == "scissors":
        if computer == "rock":
            loses += 1
            return loses

class MyTestCase(unittest.TestCase):
# compare the options between player and computer

    def test_count_score(self):
        self.assertEqual(count_score_ties('', 'rock', 'rock'), 1)
        self.assertNotEqual(count_score_ties('', 'paper', 'rock'), 1)

    def test_count_score_wins(self):
        self.assertEqual(count_score_wins('', 'rock', 'scissors'), 1)
        self.assertEqual(count_score_wins('', 'paper', 'rock'), 1)
        self.assertEqual(count_score_wins('', 'scissors', 'paper'), 1)
        self.assertNotEqual(count_score_wins('', 'rock', 'rock'), 1)
        self.assertNotEqual(count_score_wins('', 'paper', 'scissors'), 1)

    def test_count_score_loses(self):
        self.assertEqual(count_score_loses('', 'rock', 'paper'), 1)
        self.assertEqual(count_score_loses('', 'paper', 'scissors'), 1)
        self.assertEqual(count_score_loses('', 'scissors', 'rock'), 1)
        self.assertNotEqual(count_score_loses('', 'rock', 'rock'), 1)
        self.assertNotEqual(count_score_loses('', 'rock', 'scissors'), 1)


if __name__ == '__main__':
    unittest.main()