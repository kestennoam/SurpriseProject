from OutputFlow.Surprises.ExternalAPI import ExternalAPI
from OutputFlow.Surprises.SurpriseFrame import SurpriseFrame


class KanyeWest(SurpriseFrame):
    """
    This class KanyeWest is type of Surprise, (option 2).
    if randomize joke of Kanye West quote from external API.
    it heritage from surprise most of attributes.
    work with ExternalAPI class (importing it) to read json from http request
    """
    URL = "https://api.kanye.rest"
    RESULT = "quote"
    TYPE = "kanye-quote"

    def __init__(self):
        super().__init__()

    def get_query(self):
        """
        This method make the query- return a random quote.
        it call externalAPI class to use the method of reading json file
        :return:
        """
        external = ExternalAPI(self.RESULT, self.URL)
        return external.read_json()
