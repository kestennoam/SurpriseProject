import requests
import json


class ExternalAPI:
    def __init__(self, result, url):
        self.__result = result
        self.__url = url

    def read_json(self):
        """
        This method is reading a json obj from an external api
        and return it as string
        :return: string of the output from the external api
        """
        content = requests.get(self.__url)
        data = json.loads(content.content)  # save all the json info
        return data[self.__result]  # get only the relevant value
