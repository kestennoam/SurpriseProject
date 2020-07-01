from final.ExternalAPI import ExternalAPI
from OutputFlow.Surprises.SurpriseFrame import SurpriseFrame


class ChuckNorris(SurpriseFrame):
    """
    This class ChuckNorris is type of Surprise, (option 1).
    if randomize joke of Chuck Norris joke from external API.
    it heritage from surprise most of attributes.
    work with ExternalAPI class (importing it) to read json from http request
    """
    URL = "https://api.chucknorris.io/jokes/random"
    RESULT = "value"
    TYPE = "chuck-norris-joke"

    def __init__(self):
        super().__init__()

    def get_query(self):
        """
        This method make the query- return a random joke.
        it call externalAPI class to use the method of reading json file
        :return: string- joke of chuckNorris
        """
        external = ExternalAPI(self.RESULT, self.URL)
        return external.read_json()
