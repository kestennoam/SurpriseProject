from OutputFlow.ChooseSurprise import ChooseSurprise
from OutputFlow.Surprises.ChuckNorris import ChuckNorris
from OutputFlow.Surprises.KanyeWest import KanyeWest
from OutputFlow.Surprises.NumSum import NumSum
from ValidationInput import ValidationInput
import bottle
from OutputFlow.Surprises.Animals import Animals


class SingleSurprise:
    """
    This class is responsible on one full iteration of getting surprise.
    the input that
    """
    TYPE_CHUCK_NORRIS = 1
    TYPE_KANYE_WEST = 2
    TYPE_NUM_SUM = 3
    TYPE_ANIMALS = 4
    NO_EXIST_TYPE = -1
    INVALID_INPUT = -2
    ERROR_CONNECTION = -3
    NO_SURPRISE = "No surprise for you!"
    DICT_SURPRISES = \
        {
            TYPE_CHUCK_NORRIS: ChuckNorris,
            TYPE_KANYE_WEST: KanyeWest,
            TYPE_NUM_SUM: NumSum,
            TYPE_ANIMALS: Animals
        }

    def __init__(self, *args):
        self.__payload = {}
        self.read_query_params(*args)
        self.__username = ""
        self.__birth_year = 0

    def flow(self):
        """
        This method is make a full iteration of a single surprise
        it check validation, existing type and then active the method
        to get the required surprise
        :return:
        """
        #  check if the input is valid
        if not ValidationInput(self.__payload).validate_all_params():
            return bottle.HTTPResponse(status=400), False

        self.set_fields(self.__payload)
        surprise_type = ChooseSurprise(self.__username,
                                       self.__birth_year).surprise_type
        # check if exists- Invalid
        if surprise_type == self.NO_EXIST_TYPE:
            return bottle.HTTPResponse(status=404,
                                       body=self.NO_SURPRISE), False
        # valid
        obj = self.DICT_SURPRISES[surprise_type]()  # init instance
        obj.set_fields(self.__username, self.__birth_year)
        res = obj.get_query()
        # No internet connection
        if res == self.ERROR_CONNECTION:
            return bottle.HTTPResponse(status=502), False

        return obj.TYPE, obj.response_json(obj.TYPE, res)

    def read_query_params(self, *args):
        """
        This method is reading all the json params that were passed by the url.
        it convert it to a dictionary that the keys are the fields (e.g 'name)
        and the values are the values of the fields (e.g specific name)
        :param args:
        """
        for dictionary in args:
            self.__payload.update(dictionary)

    def set_fields(self, payload):
        """
        This method is setting all the fields that are required for a surprise
        :param payload:
        :return:
        """
        self.__username = payload['name']
        self.__birth_year = int(payload['birth_year'])
