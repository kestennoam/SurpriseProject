import requests
import json

URL_KANYE_WEST = "https://api.kanye.rest"
QUOTE = "quote"
BIRTH_YEAR_VALID = 2000
NOT_VALID_FIRST_CH = 'AZaz'


def is_chuck_norris_type(username, birth_year):
    return (username[0] not in NOT_VALID_FIRST_CH) and \
           (birth_year > BIRTH_YEAR_VALID)


def get_kanye_west_quote():
    content = requests.get(URL_KANYE_WEST)
    data = json.loads(content.content)  # save all the json info
    quote = data[QUOTE]
    print(quote)
    return quote


get_kanye_west_quote()
