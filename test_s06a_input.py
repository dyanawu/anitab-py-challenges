import s06a_input
import unittest
from unittest import mock

class TestValidateInput(unittest.TestCase):
    def test_validate_input_integer(self):
        self.assertTrue(s06a_input.validate_input("0"))
        self.assertTrue(s06a_input.validate_input("20"))
        self.assertTrue(s06a_input.validate_input("120"))
        self.assertTrue(s06a_input.validate_input("2473"))
        self.assertTrue(s06a_input.validate_input("10000"))

    def test_validate_input_integer_out_of_range(self):
        self.assertFalse(s06a_input.validate_input("-1"))
        self.assertFalse(s06a_input.validate_input("-3546"))
        self.assertFalse(s06a_input.validate_input("10001"))


class TestMain(unittest.TestCase):
    def test_main_valid_input_ok(self):
        with mock.patch('s06a_input.input') as input:
            with mock.patch('s06a_input.print') as print:
                input.return_value = "123"

                s06a_input.main()

                input.assert_called_once_with("Enter a number between 0 and 10000 inclusive: ")
                print.assert_has_calls([
                    mock.call(1),
                    mock.call(2),
                    mock.call(3)
                ])

    def test_main_valid_input_multiple_values(self):
        with mock.patch('s06a_input.input') as input:
            with mock.patch('s06a_input.print') as print:
                input.side_effect = [
                    "invalid",
                    "123",
                    self.failureException("Should not reach here")
                ]

                s06a_input.main()

                input.assert_has_calls([
                    mock.call("Enter a number between 0 and 10000 inclusive: "),
                    mock.call("Enter a number between 0 and 10000 inclusive: ")
                ])
                print.assert_has_calls([
                    mock.call('invalid is not valid input.'),
                    mock.call(1), mock.call(2), mock.call(3)
                ])


if __name__ == '__main__':
    unittest.main()
