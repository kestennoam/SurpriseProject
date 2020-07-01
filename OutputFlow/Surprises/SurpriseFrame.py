import json


class SurpriseFrame:
    """
    This class is the father of all kind of surprise types.
    it include the basic methods that we will need to create a surprise
    instance
    """
    TYPE = "type"
    JSON_RESULT = "result"

    def __init__(self):
        self.__args = []

    def response_json(self, type_surprise, result):
        """
        This method encapsulate the the result from the surprise to json dump
        :param type_surprise: the key of the json dump
        :param result: the instance that was returned from single iteration
        :return: json dump
        """
        data_set = {self.TYPE: type_surprise, self.JSON_RESULT: result}
        json_dump = json.dumps(data_set)
        return json_dump

    def set_fields(self, *args):
        """
        this method is responsible on defining all fields that were passed
        to fields of the surprise instance
        :param args: username[0], birth_year[1]. etc...
        :return: None
        """
        for arg in args:
            self.__args.append(arg)

    def get_val(self, index):
        """
        This method return a value from the args of the surprise instance
        :param index:
        :return:
        """
        if index < 0 or index >= len(self.__args):
            raise IndexError
        return self.__args[index]
