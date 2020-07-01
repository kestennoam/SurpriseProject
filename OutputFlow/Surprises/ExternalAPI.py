import requests
import json


class ExternalAPI:
    """
    This class get content from external api (url )
    it get the result which parse the data from the dictionary that will
    receive from the api, and need to request from the url  the content
    """
    ERROR_CONNECTION = -3

    def __init__(self, result, url):
        self.__result = result
        self.__url = url

    def read_json(self):
        """
        This method is reading a json obj from an external api
        and return it as string
        :return: string of the output from the external api
        """

        try:
            content = requests.get(self.__url)
            data = json.loads(content.content)  # save all the json info
            return data[self.__result]  # get only the relevant value
        except requests.ConnectionError:
            return self.ERROR_CONNECTION
