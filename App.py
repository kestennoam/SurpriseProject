from bottle import route, run, HTTPResponse, request
from OutputFlow.SingleSurprise import SingleSurprise
from Stats import Stats
from SetUp import *

# --------------------- Macros-----------------------------------
PORT = 3000
HOST = "localhost"
INVALID_INPUT = "INVALID_INPUT"
NO_SURPRISE = "No surprise for you!"
NO_EXIST_TYPE = -1
INVALID_INPUT = -2


# --------------------- Routes Functions------------------------
@route("/api/surprise")
def surprise():
    """
    This method is responding to http get of /api/surprise.
    call the single surprise to get the matched json output
    and return a response depend on the input
    :return: json frame directly to the web
    """
    # print(dict(request.query.decode()))
    single = SingleSurprise(dict(request.forms),
                            dict(request.query.decode())).flow()
    # Invalid Input
    if single == INVALID_INPUT:
        print("fff")
        return HTTPResponse(status=400)
    # Invalid type
    elif single == NO_EXIST_TYPE:
        return HTTPResponse(status=404, body=NO_SURPRISE)
    # valid
    type_surprise, json_frame = single
    stats.set_stat(type_surprise)  # update stats
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


# --------------------- Main -----------------------------------

if __name__ == '__main__':
    SetUp()
    stats = Stats()
    run(host=HOST, port=PORT)
