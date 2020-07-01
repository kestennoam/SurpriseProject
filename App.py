from bottle import route, run, request
from Surprise.SingleSurprise import SingleSurprise
from Stats import Stats
from Demographics import Demographics

# --------------------- Macros-----------------------------------
PORT = 3000
HOST = "localhost"
INVALID_INPUT = "INVALID_INPUT"
NO_SURPRISE = "No surprise for you!"
NO_EXIST_TYPE = -1
INVALID_INPUT = -2
ERROR_CONNECTION = -3


# --------------------- Routes Functions------------------------
@route("/api/surprise")
def surprise():
    """
    This method is responding to http get of /api/surprise.
    call the single surprise to get the matched json output
    and return a response depend on the input
    :return: json frame directly to the web
    """
    dict_queries = dict(request.query.decode())
    res = SingleSurprise(dict(request.forms), dict_queries).flow()
    if not res[1]:  # check if the input is invalid
        return res[0]

    # valid
    type_surprise, json_frame = res
    stats.set_stat(type_surprise)  # update stats
    demographics.update_stats(dict_queries)
    return json_frame


@route("/api/stats")
def stats():
    """
    This method ic responding to http get of /api/stats.
    it call Stats class (that already created on main) and return json
    frame that include all the stats.
    :return:json frame
    """
    return stats.response_stats()


@route("/api/demographics")
def demographics():
    """
    This method ic responding to http get of /api/stats.
    it call Stats class (that already created on main) and return json
    frame that include all the stats.
    :return:json frame
    """
    return demographics.response_demographics()


# --------------------- Main -----------------------------------

if __name__ == '__main__':
    stats = Stats()
    demographics = Demographics()
    run(host=HOST, port=PORT)
