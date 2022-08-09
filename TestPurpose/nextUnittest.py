import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print("I am running browser")
    def test_something(self):
        print("Test Something running")
        # self.assertEqual(True, False)  # add assertion here
    def test_new(self):
        print("Test new running")

    def testsomething(self):
        print("I may not be running")
    def tearDown(self) -> None:
        print("I am closing")


if __name__ == '__main__':
    unittest.main()
