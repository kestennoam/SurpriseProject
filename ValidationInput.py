# -*- coding: utf-8 -*-
import datetime


class ValidationInput:
    """
    This class is responsible on the validation of the input that we get
    from the server.
    we get it as dict and need to check every relevant param of it.
    Must note that at this moment we accept more fields than num_of_params
    """
    CURRENT_YEAR = datetime.datetime.today().year
    OLDEST_YEAR = CURRENT_YEAR - 130
    NUM_OF_PARAMS = 2
    RANGE_YEARS = range(OLDEST_YEAR, CURRENT_YEAR + 1)

    def __init__(self, dict_params):
        self.__dict_params = dict_params

    def validate_all_params(self):
        return self.validate_num_of_params() and \
               self.validate_birth_year() and \
               self.validate_username()

    def validate_num_of_params(self):
        """
        This method check if the dictionary has enough params
        :return:
        """
        if not isinstance(self.__dict_params, dict): return False
        return len(self.__dict_params.keys()) >= self.NUM_OF_PARAMS

    def validate_birth_year(self):
        """
        This method check 3 validations:
         1) if the birth_year field is exists
         2) 'birth_year' is numeric
         3) 'birth_year' is in range of real years
        :return: True/False
        """
        return 'birth_year' in self.__dict_params and \
               self.__dict_params['birth_year'].isnumeric() and \
               int(self.__dict_params['birth_year']) in self.RANGE_YEARS

    def validate_username(self):
        """
        This method check 3 validations:
        1) if the 'name' field is a key in the dictionary
        2) if all the chars are alphabetic or one space
        3) if username is empty - False
        4) is it in english or not
        :return: True/False
        """
        if 'name' not in self.__dict_params: return False
        num_of_spaces = 0
        for ch in self.__dict_params['name']:
            if not self.is_english_char(ch):
                return False  # check english
            if ch.isalpha():
                continue
            elif ch.isspace() and num_of_spaces < 1:
                num_of_spaces += 1
            else:
                return False
        if len(self.__dict_params['name']) == 0:
            return False
        return True

    @staticmethod
    def is_english_char(username):
        """
        This method check if the input is in english or not
        :param username:
        :return:
        """
        try:
            username.encode(encoding='utf-8').decode('ascii')
        except UnicodeDecodeError:
            return False
        else:
            return True
