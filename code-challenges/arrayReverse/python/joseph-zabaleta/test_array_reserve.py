import pytest
from array_reverse import array_reverse


class Test_Array_Reverse:
    def test_array_reverse_without_prebuilt_methods(self):
        input = [1, 2, 3, 4, 5, 6]
        actual = array_reverse(input)
        expected = input[::-1]

        assert actual == expected

    def test_should_handle_list_of_positive_and_negative_numbers(self):
        input = [89, 2354, 3546, 23, 10, -923, 823, -12]
        actual = array_reverse(input)
        expected = input[::-1]

        assert actual == expected

    def test_should_handle_list_of_dictionaries(self):
        input = [
            {
                "name": "bob",
                "house": "white",
            },
            {
                "name": "tim",
                "house": "blue",
            },
        ]
        actual = array_reverse(input)
        expected = input[::-1]

        assert actual == expected

    def test_should_handle_empty_list(self):
        input = []
        actual = array_reverse(input)
        expected = input[::-1]

        assert actual == expected
