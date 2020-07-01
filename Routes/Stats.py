import json


class Stats:
    """
    This class is responsible on all the stats of the rest server.
    it counts in generally and separately hwo many http get were occurred
    to each one of the surprises
    """
    REQUESTS = "requests"
    BAD_REQUESTS = "bad requests"
    REQUESTS_STATS = "requests_stats"
    TYPE_TITLE = "type"
    COUNT = "count"
    DISTRIBUTION = "distribution"
    DEFAULT_VALUE = 0

    def __init__(self):
        self.__valid_requests = self.DEFAULT_VALUE
        self.__requests_stats = self.DEFAULT_VALUE
        self.__bad_requests = 0
        self.__dict_stats = \
            {
                "chuck-norris-joke": self.DEFAULT_VALUE,
                "kanye-quote": self.DEFAULT_VALUE,
                "name-sum": self.DEFAULT_VALUE,
                'animal in your first letter': self.DEFAULT_VALUE
            }

    def set_stat(self, type_of_surprise):
        """
        this method increase the general stat in 1 and the particular one (this
        is the reason that the method get argument, that will provide the type)
        :param type_of_surprise: type of surprise (it got from server)
        :return: None
        """
        # invalid
        if type_of_surprise not in self.__dict_stats:
            return
        self.__dict_stats[type_of_surprise] += 1
        self.__valid_requests += 1

    def make_distribution(self):
        """
        This function make the second layer in the stat json frame.
        if run on all the surprise types and create a dictionary.
        e.g:
            "type": "chuck-norris-joke",
            "count": 12
        and return the list with all these dictionaries

        :return: list of dictionaries
        """
        distribution = []
        for k, v in self.__dict_stats.items():
            data_frame = {self.TYPE_TITLE: k, self.COUNT: v}
            distribution.append(data_frame)
        return distribution

    def increase_bad_requests(self):
        """
        This method increase counter of bad requests
        :return:
        """
        self.__bad_requests += 1

    def response_stats(self):
        """
        This method build the full packet that will be responded to the web
        first it call make distribution and than make thew big frame
        :return: json frame
        """
        self.__requests_stats += 1
        distribution = self.make_distribution()
        data_frame = {self.REQUESTS_STATS: self.__requests_stats,
                      self.REQUESTS: self.__valid_requests,
                      self.BAD_REQUESTS: self.__bad_requests,
                      self.DISTRIBUTION: distribution}
        json_dump = json.dumps(data_frame)
        return json_dump
