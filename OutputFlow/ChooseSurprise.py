class ChooseSurprise:
    """
    This class is responsible to understand which query is requried depend
    on the username and birth year .
    if has alot of validations methods and method (choose_type) that run on
    each one of them
    """
    BIRTH_YEAR = 2000
    KANYE_WEST_FIRST_CH = "aAzZ"
    NAME_SUM_FIRST_CH = 'qQ'
    NO_EXIST_TYPE = -1
    TYPE_CHUCK_NORRIS = 1
    TYPE_KANYE_WEST = 2
    TYPE_NUM_SUM = 3
    TYPE_ANIMALS = 4

    def __init__(self, *args):
        self.__username = args[0]
        self.__birth_year = args[1]
        self.surprise_type = self.choose_type()

    # ----------------Validation-----------------------------------

    def choose_type(self):
        """
        This method check all the types that are exist and return a number
        :return:
        """
        if self.is_type_chuck_norris_joke() is True:
            return self.TYPE_CHUCK_NORRIS
        elif self.is_type_kanye_west_quote() is True:
            return self.TYPE_KANYE_WEST
        elif self.is_type_animals() is True:
            return self.TYPE_ANIMALS
        elif self.is_type_name_sum() is True:
            return self.TYPE_NUM_SUM
        # place to add new queries
        else:
            return self.NO_EXIST_TYPE

    def is_type_chuck_norris_joke(self):
        """
        This method check if it's Chuck Norris call
        the condition is if birth year is less than birth year (macro)
        :return: boolean if it's chuck norris type
        """
        return self.__birth_year < self.BIRTH_YEAR

    def is_type_kanye_west_quote(self):
        """
        This method check if it's Kanye West call
        the condition is if the birth year is smaller than BIRTH_YEAR and the
        first letters should not be from kanye_west_first_ch
        :return:
        """
        return self.__birth_year > self.BIRTH_YEAR and \
               self.__username[0] not in self.KANYE_WEST_FIRST_CH

    def is_type_name_sum(self):
        """
        This method check if the username doesnt start with q or Q
        :return:
        """
        return self.__username[0] not in self.NAME_SUM_FIRST_CH

    def is_type_animals(self):
        """
        This method check if the birth_year is equal to 2000
        :return:
        """
        return self.__birth_year == self.BIRTH_YEAR
