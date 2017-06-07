from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        keys = [1, 2, 3]
        values = [10, 20, 30]
        res = solution(keys, values)

        self.assertEqual(res[1], 10)
        self.assertEqual(res[2], 20)
        self.assertEqual(res[3], 30)
