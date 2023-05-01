from unittest import TestCase, main
from whiteboard import solution


class MatchTestCase(TestCase):
    
    def test_1_p1_win(self):
        self.assertEqual(solution(
        ["15t", "16t", "17t", "18t", "19t", "20t", "bd", "bs"],
        ["15d","12","0" "16t", "17t", "18t", "19t", "20t", "bd", "b"]
        ), "Player 1 Wins")

    def test_2_p2_win(self):
        self.assertEqual(solution(
            ["15d","12","0", "16t", "17t", "18t", "19t", "20t", "bd", "b"],
            ["15t", "16t", "17t", "18t", "19t", "20t", "bd", "bs"]),
             "Player 2 Wins")

    def test_3_incomplete(self):
        self.assertEqual(solution(
            ["15d","12s","0s", "16t", "17t", "18t", "19t", "20t", "bd", '14t', '10s', '12d', '2s', '10t', '2t', '9s', '11d', '4s', '12d', '14d', '10s', '9s', '14s', '2d', '5t', '7s', '4d', '3t', '13d', '11d', '14d', '11d', '2t', '13t', '5t', '4t', '2d', '8t', '7d', '10t', '14d', '2t', '2d', '3s', '12s', '7t', '9s', '8t', '3t', '9s', '4d', '12t', '5d', '12t', '8d', '10d', '7d', '5t', '14d', '10d'],
            [ "17s", "18d", "19t", "20t", "bd", "18s", '3s', '14s', '14s', '9d', '4d', '12s', '14s', '14s', '3s', '12s', '13t', '11s', '8t', '8s', '12s', '8d', '14d', '5t', '1s', '11d', '2t', '9d', '4d', '4t', '11s', '11t', '3d', '12s', '2s', '8t', '14s', '1t', '4s', '1s', '13s', '6d', '12d', '13s', '4d', '9t', '2t', '12t', '6d', '1t', '2s', '11t', '9d', '6t', '3t', '5s', '9t', '4t', '9s', '4t']),
             "Incomplete")


if __name__ == "__main__":
    main()