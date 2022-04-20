import pprint

import requests


def save_resp_to_file(file_name="robots.txt"):
    base_url = "https://api.pushshift.io/reddit/comment/search/"
    req = requests.get(base_url)
    resp = req.text
    print(req)
    with open(file_name, "w") as file:
        file.writelines(resp)


if __name__ == "__main__":
    pprint.pprint(save_resp_to_file())
