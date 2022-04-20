import requests
import pprint
import json


def save_resp(file_name="redit.json"):
    base_url = "https://api.pushshift.io/reddit/comment/search/"
    params = {"q": "programming", "sort": "asc", "sort_type": "created_utc", "size": 10}
    req = requests.get(base_url,params=params)
    print(req.status_code)
    with open(file_name,"w") as file:
        json.dump(req.json(),file)
    return req.json()
if __name__=="__main__":
    pprint.pprint(save_resp())