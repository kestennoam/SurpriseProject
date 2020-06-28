import json
import requests


def main():
    content = requests.get("http://localhost:3000/api/surprise?")
    data = json.loads(content.content)  # save all the json info
    print(data)


main()
