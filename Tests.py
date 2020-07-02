import string
from ValidationInput import ValidationInput
from Routes.Surprise.ChooseSurprise import ChooseSurprise
import random
import datetime

CURRENT_YEAR = datetime.datetime.today().year
OLDEST_YEAR = CURRENT_YEAR - 130
DEFAULT_ITERATIONS = 1000
NO_EXIST_TYPE = -1
TYPE_CHUCK_NORRIS = 1
TYPE_KANYE_WEST = 2
TYPE_NUM_SUM = 3
TYPE_ANIMALS = 4
BIRTH_YEAR_DEFAULT = 2000
NAME_SUM_FIRST_CH = 'qQ'
KANYE_WEST_FIRST_CH = "aAzZ"


def random_string():
    """
    This method randomize string in len 1-20 with upper and lower letters.
    :return:
    """
    range_random = random.randrange(1, 20)
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(range_random))


# --------------------_Unit Tests------------------------------
class TestValidationInput:
    """
    This class test the validation input.
    it check a lot of sanity and edge cases of each function.
    """

    def run_validation_input(self):
        """
        this method run all the tests of the class
        :return:
        """
        self.test_num_of_params_valid()
        self.test_num_of_params_invalid()
        self.test_username_invalid()
        self.test_username_valid()
        self.test_birth_year_invalid()
        self.test_birth_year_valid()

    @staticmethod
    def test_num_of_params_invalid():
        """
        This method check the num of params edge cases.
        1)empty name
        2) zero params
        3) one param
        4) invalid types in the dict
        :return:
        """
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

    @staticmethod
    def test_num_of_params_valid():
        """
        check default iterations num of valid params
        :return:
        """
        for i in range(DEFAULT_ITERATIONS):
            valid_dict = {}
            for i in range(random.randrange(2, 50)):
                valid_dict[i] = 0
            in1 = ValidationInput(valid_dict)
            assert in1.validate_num_of_params(), "Should be dictionary"
        print("TEST PASSED- num of params Valid")

    @staticmethod
    def test_username_invalid():
        """
        This method check specifcily the username validation function
        1) rmpty name
        2) double spaces
        3) numeric char in the name
        4) special char in the name
        :return:
        """
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

    @staticmethod
    def test_username_valid():
        """
        This method check sanity checks of the username
        :return:
        """
        one_space = {'name': "John Smith", 'birth_year': '2000'}
        in1 = ValidationInput(one_space)
        assert in1.validate_username(), "Space is valid"
        for i in range(DEFAULT_ITERATIONS):
            valid_string = random_string()
            valid_dic = {'name': valid_string, 'birth_year': '2000'}
            in2 = ValidationInput(valid_dic)
            assert in2.validate_username(), "Valid Input"
        print("TEST PASSED- username valid")

    @staticmethod
    def test_birth_year_invalid():
        """
        This method check invalid edge cases of birth year
        1) not in the range of years
        2) negative year
        3) float year
        4) not numeric
        :return:
        """
        msg_failed = f"Year Not in range {OLDEST_YEAR}- {CURRENT_YEAR}"
        not_in_range = {'name': "test", 'birth_year': '2030'}
        in1 = ValidationInput(not_in_range)
        assert not in1.validate_birth_year(), msg_failed

        negative_year = {'name': "test", 'birth_year': '-4'}
        in2 = ValidationInput(negative_year)
        assert not in2.validate_birth_year(), msg_failed

        float_year = {'name': "test", 'birth_year': '2000.2'}
        in3 = ValidationInput(float_year)
        assert not in3.validate_birth_year(), msg_failed

        not_numeric = {'name': "test", 'birth_year': 'aa'}
        in4 = ValidationInput(not_numeric)
        assert not in4.validate_birth_year(), \
            f"Year Must be an integer {OLDEST_YEAR}-{CURRENT_YEAR}"
        print("TEST PASSED- birth_year invalid")

    @staticmethod
    def test_birth_year_valid():
        """
        This method check sanity checks of valid randomized years
        :return:
        """
        for i in range(DEFAULT_ITERATIONS):
            year = str(random.randrange(OLDEST_YEAR, CURRENT_YEAR + 1))
            not_in_range = {'name': "test", 'birth_year': year}
            in1 = ValidationInput(not_in_range)
            assert in1.validate_birth_year(), \
                F"Year in range {OLDEST_YEAR}-{CURRENT_YEAR} is valid"
        print("TEST PASSED- birth_year valid")


class TestChooseSurprise:
    """
    This class test all the ChooseSurprise functions by unit tests
    of every possible option
    """

    def run_tests(self):
        """
        This method run all the tests
        :return:
        """
        self.test_chuck_norris()
        self.test_kanye_west()
        self.test_num_sum()
        self.test_animals_surprise()

    @staticmethod
    def test_chuck_norris():
        """
        This method check randomized years and names
         that the result should be chuck norris
        :return:
        """
        for i in range(DEFAULT_ITERATIONS):
            username = random_string()
            birth_year = random.randrange(OLDEST_YEAR, BIRTH_YEAR_DEFAULT)
            assert ChooseSurprise(username, birth_year).choose_type() \
                   == TYPE_CHUCK_NORRIS, "Should be Chuck Norris"
        print("TEST PASSED- Chuck Norris Valid")

    @staticmethod
    def test_kanye_west():
        """
        This method check randomized years and names
         that the result should be kanye west
        :return:
        """
        for i in range(DEFAULT_ITERATIONS):
            username = random_string()
            if username[0] in KANYE_WEST_FIRST_CH:
                username = 'h' + username
            birth_year = random.randrange(BIRTH_YEAR_DEFAULT + 1,
                                          CURRENT_YEAR + 1)
            assert ChooseSurprise(username, birth_year).choose_type() \
                   == TYPE_KANYE_WEST, "Should be Kanye West"
        print("TEST PASSED- Kanye West Valid")

    @staticmethod
    def test_num_sum():
        """
        This method check randomized years and names
         that the result should be nun_sum
        :return:
        """
        for i in range(DEFAULT_ITERATIONS):
            username = random_string()
            birth_year = random.randrange(BIRTH_YEAR_DEFAULT + 1,
                                          CURRENT_YEAR + 1)
            res = ChooseSurprise(username, birth_year).choose_type()
            if username[0] in NAME_SUM_FIRST_CH or \
                    username[0] not in KANYE_WEST_FIRST_CH:
                assert res != TYPE_NUM_SUM, "Should not be num-sum"
            else:
                assert res == TYPE_NUM_SUM, "Should be num-sum"
        print("TEST PASSED- num-sum Valid")

    @staticmethod
    def test_animals_surprise():
        """
        This method check randomized years and names
         that the result should be animals
        :return:
        """
        for i in range(DEFAULT_ITERATIONS):
            username = random_string()
            assert ChooseSurprise(username, BIRTH_YEAR_DEFAULT).choose_type() \
                   == TYPE_ANIMALS, "Should be Animals type"


if __name__ == '__main__':
    TestValidationInput().run_validation_input()
    TestChooseSurprise().run_tests()
    print("ALL TESTS PASSED")
