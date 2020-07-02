import numpy as np
import datetime
import json
from ExternalAPI import ExternalAPI


class Demographics:
    """
    This class is responsible on the demographics stats.
    It map the ages and percentiles of the users, count the probably
    genders of the users.
    """
    CURRENT_YEAR = datetime.datetime.today().year
    ENUM_P = {0: ('P95', 95),
              1: ('P90', 90),
              2: ('P75', 75),
              3: ('P70', 70),
              4: ('P50', 50),
              5: ('P25', 25)}
    NUM_PERCENTILES = 6
    PERCENTILES_TITLE = "Percentiles"
    AGES_TITLE = "Ages"
    GENDERS_TITLE = "Genders"
    URL_GENDER = "https://api.genderize.io?name="
    ERROR_CONNECTION = -3

    def __init__(self):
        self.__dic = {}
        self.__ages = {}
        self.__cache_genders = {}
        self.__all_results = []
        self.__genders = {'male': 0, 'female': 0, 'unknown': 0}
        self.__percentiles = {
            'P95': 0,
            'P90': 0,
            'P75': 0,
            'P70': 0,
            'P50': 0,
            'P25': 0}

    def update_stats(self, dic):
        """
        Updating every valid surprise iteration the stats
        :param dic: dict with username and birth_year
        :return: None
        """
        self.update_age_dict(dic)
        self.update_gender(dic)

    def response_demographics(self):
        """
        This method create a json frame of the response when the user send
        get request with route of the demographics.
        it pack together ages,gender and percentiles dictionaries
        :return:
        """
        self.calc_percentiles()
        data_frame = {self.AGES_TITLE: self.__ages,
                      self.GENDERS_TITLE: self.__genders,
                      self.PERCENTILES_TITLE: self.__percentiles}
        json_dump = json.dumps(data_frame, indent=4)
        return json_dump

    def update_age_dict(self, dic):
        """
        This method update the ages dictionary every iteration.
        it append the age to the list that saves all.
        it update the the dictionary with the ages.
        :param dic: dict that includes birth_year
        :return:
        """
        if 'birth_year' not in dic:
            return
        age = self.CURRENT_YEAR - int(dic['birth_year'])
        self.__all_results.append(age)
        if age not in self.__ages:
            self.__ages[age] = 1
        else:
            self.__ages[age] += 1

    def calc_percentiles(self):
        """
        This method calculate the percentiles pf the total results
        it calculate by numpy the percentiles of :
        95 , 75, 70 ,50 ,25.
        Time Complexity of numpy.percentiles is O(N-K) N(list len) and K(%)
        :return:
        """
        for i in range(self.NUM_PERCENTILES):
            if self.__all_results:
                self.__percentiles[self.ENUM_P[i][0]] = \
                    int(np.percentile(self.__all_results, self.ENUM_P[i][1]))

    def update_gender(self, dic):
        """
        This method just add names to
        :param dic:
        :return:
        """
        if 'name' not in dic:
            return
        gender = self.cache_genders(dic['name'].split()[0])
        if gender == self.ERROR_CONNECTION:
            return self.ERROR_CONNECTION
        self.__genders[gender] += 1
        return True

    def cache_genders(self, name):
        """
        This method is cache for requests to API of recognize gender.
        check if already exists
        :param name: first name
        :return:
        """
        if name in self.__cache_genders:
            return self.__cache_genders[name]
        else:
            parsed_url = self.URL_GENDER + name
            gender = ExternalAPI('gender', parsed_url).read_json()
            if gender == self.ERROR_CONNECTION:
                return self.ERROR_CONNECTION
            # Api didn't recognize which gender
            if not gender:
                gender = 'unknown'
            self.__cache_genders[name] = gender
            return gender
