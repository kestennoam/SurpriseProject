import string
from ValidationInput import ValidationInput
import random

DEFAULT_ITERATIONS = 100


def random_string(string_length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(string_length))


# --------------------_Unit Tests------------------------------
class ValidationInputTest():
    def run_validationInput(self):
        self.test_num_of_params_valid()
        self.test_num_of_params_invalid()
        self.test_username_invalid()
        self.test_username_valid()
        self.test_birth_year_invalid()
        self.test_birth_year_valid()

    def test_num_of_params_invalid(self):
        one_param = {'name': ""}
        in1 = ValidationInput(one_param)
        assert not in1.validate_num_of_params(), "Should be 2 params"

        zero_param = {}
        in2 = ValidationInput(zero_param)
        assert not in2.validate_num_of_params(), "Should be 2 params"

        no_dict_type = [1, [], (), 'a', 2.2]
        for i in no_dict_type:
            in3 = ValidationInput(i)
            assert not in3.validate_num_of_params(), "Should be dictionary"
        print("TEST PASSED- num of params Invalid")

    def test_num_of_params_valid(self):
        for i in range(DEFAULT_ITERATIONS):
            valid_dict = {}
            for i in range(random.randrange(2, 50)):
                valid_dict[i] = 0
            in1 = ValidationInput(valid_dict)
            assert in1.validate_num_of_params(), "Should be dictionary"
        print("TEST PASSED- num of params Valid")

    def test_username_invalid(self):
        empty_name = {'name': "", 'birth_year': '2000'}
        in1 = ValidationInput(empty_name)
        assert not in1.validate_username(), "empty name is an Error"

        double_space = {'name': "John  Smith", 'birth_year': '2000'}
        in2 = ValidationInput(double_space)
        assert not in2.validate_username(), "Double Space is an Error"

        digit_in_name = {'name': "John1", 'birth_year': '2000'}
        in3 = ValidationInput(digit_in_name)
        assert not in3.validate_username(), "Digit in name is an Error"

        special_char_name = {'name': "John%", 'birth_year': '2000'}
        in4 = ValidationInput(special_char_name)
        assert not in4.validate_username(), " name Should be alphabetic"

        print("TEST PASSED- username Invalid")

    def test_username_valid(self):
        one_space = {'name': "John Smith", 'birth_year': '2000'}
        in1 = ValidationInput(one_space)
        assert in1.validate_username(), "Space is valid"
        for i in range(DEFAULT_ITERATIONS):
            valid_string = random_string(random.randrange(1, 100))
            valid_dic = {'name': valid_string, 'birth_year': '2000'}
            in2 = ValidationInput(valid_dic)
            assert in2.validate_username(), "Valid Input"
        print("TEST PASSED- username valid")

    def test_birth_year_invalid(self):
        not_in_range = {'name': "test", 'birth_year': '2030'}
        in1 = ValidationInput(not_in_range)
        assert not in1.validate_birth_year(), "Year Not in range 0- 2020"

        negative_year = {'name': "test", 'birth_year': '-4'}
        in2 = ValidationInput(negative_year)
        assert not in2.validate_birth_year(), "Year Not in range 0- 2020"

        not_numeric = {'name': "test", 'birth_year': 'aa'}
        in3 = ValidationInput(not_numeric)
        assert not in3.validate_birth_year(), "Year Must be an integer 0-2020"
        print("TEST PASSED- birth_year invalid")

    def test_birth_year_valid(self):
        for i in range(DEFAULT_ITERATIONS):
            year = str(random.randrange(0, 2020))
            not_in_range = {'name': "test", 'birth_year': year}
            in1 = ValidationInput(not_in_range)
            assert in1.validate_birth_year(), "Year in range 0-2020 is valid"
        print("TEST PASSED- birth_year valid")


validation_input = ValidationInputTest()
validation_input.run_validationInput()
