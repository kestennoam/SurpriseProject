import numpy as np
import datetime
import json


class Demographics:
    """

    """
    CURRENT_YEAR = datetime.datetime.today().year
    ENUM_P = {0: ('P95', 95),
              1: ('P90', 90),
              2: ('P75', 75),
              3: ('P70', 70),
              4: ('P50', 50),
              5: ('P25', 25)}
    NUM_PERCENTILES = 6
    PERCENTILES_TITLE = "PERCENTILES"
    AGES_TITLE = "ALL AGES"

    def __init__(self):
        self.__dic = {}
        self.__ages = {}
        self.__all_results = []
        self.__percentiles = {
            'P95': 0,
            'P90': 0,
            'P75': 0,
            'P70': 0,
            'P50': 0,
            'P25': 0}
        

    def update_stats(self, dic):
        print(dic)
        if 'birth_year' not in dic:
            return
        age = self.CURRENT_YEAR - int(dic['birth_year'])
        self.__all_results.append(age)
        print(self.__all_results)
        self.update_age_dict(age)

    def update_age_dict(self, age):
        if age not in self.__ages:
            self.__ages[age] = 1
        else:
            self.__ages[age] += 1

    def calc_percentiles(self):
        for i in range(self.NUM_PERCENTILES):
            if self.__all_results:
                self.__percentiles[self.ENUM_P[i][0]] = \
                    int(np.percentile(self.__all_results, self.ENUM_P[i][1]))

    def response_demographics(self):
        print(self.__all_results)
        print(self.__percentiles)
        self.calc_percentiles()
        data_frame = {self.AGES_TITLE: self.__ages,
                      self.PERCENTILES_TITLE: self.__percentiles}
        json_dump = json.dumps(data_frame, indent=4)
        return json_dump
