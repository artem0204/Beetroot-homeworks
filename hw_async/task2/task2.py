import asyncio
import json
import pprint
import time

import aiohttp


async def save_data_to_file(name, comment):
    try:
        with open(name, "r") as file:
            data = json.load(file)
    except:
        data = {}
    data.update(comment)
    with open(name, "w") as file:
        json.dump(data, file, indent=4)


async def get_response(url, params):
    name = "Comments from reddit task2.json"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            data = await response.json()
            data_dict = data["data"]
            comment = {params['q']: [con.get('body') for con in data_dict]}
            pprint.pprint(data)
    await save_data_to_file(name, comment)

async def main():
    url = "https://api.pushshift.io/reddit/comment/search/"
    params1 = {'q':'digital','subreddit':'technology','sort':'asc','sort_type':'created_utc','size':3}
    params2 = {'q':'programming','subreddit':'technology','sort':'asc','sort_type':'created_utc','size':3}
    await asyncio.gather(get_response(url,params=params1),get_response(url,params=params2))

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time() - start_time
    print(f"ended time for operation:{end_time}")
    
