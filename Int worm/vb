import requests
import time as tm
import json
from datetime import datetime
from datetime import timedelta
headers = {
    'authority': 'weibo.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'client-version': 'v2.37.4',
    'cookie': 'SINAGLOBAL=6077043461805.43.1670483353611; ULV=1670483353613:1:1:1:6077043461805.43.1670483353611:; SSOLoginState=1670830294; XSRF-TOKEN=LHPwna6HTgDKsVbbgMXubApu; PC_TOKEN=4a68281152; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWL5TqjR_-bH_akCNkAPUay5JpX5KMhUgL.FoMfeoz0SheRehq2dJLoI7DKC28lg-LPx-4k; ALF=1673508812; SCF=An-OiVklaBY4o-Vpd0sqzaoJhcysdotu5q8H89hcK3xxZheZQoQjVErR4FBUFzDs1lj-H-Z4qczsXH7cKXmJPVk.; SUB=_2A25OnFqADeRhGeFL6VAS9C3EyzqIHXVt6MtIrDV8PUNbmtAfLXXSkW9NQkXMHSAsRNJ6JgN24Wb7FI4q4S-gqg9C; WBPSESS=mhAVYH3h1H1HWAai7Rl_vG5NxWLcW13Mr8JKTLoWndwBeGgNEAx6w4eI4NSJDCDBURI4yy-A2KTy992_SOtUtatvXuWQJloEvewxplOX_x-pty8fIxeZ3HOyARVRpxA11ZVzKXqnWdwPy7ypUbickw==',
    'pragma': 'no-cache',
    'referer': 'https://weibo.com/u/2645753453',
    'sec-ch-ua': '^\\^Google',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '^\\^Windows^\\^',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'server-version': 'v2022.12.09.1',
    'traceparent': '00-a01b8248be303dc91b2c511b62df17d8-7904aead89e916b1-00',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'LHPwna6HTgDKsVbbgMXubApu',
}
for i in range(0, 2):
    url = f'https://weibo.com/ajax/statuses/mymblog?uid=2645753453&page={i}&feature=0'
    tm.sleep(1)
    resp = requests.get(url, headers=headers).json()
    d_list = resp['data']['list']
    # print(type(d_list))
    for d in d_list:
        user_id = d['user']['id']
        text = d['text_raw']
        user_name = d['user']['screen_name']
        # fans = d['page_info']['media_info']['author_info']['followers_count_str']
        reposts_count = d['reposts_count']
        comments_count = d['comments_count']
        attitudes_count = d['attitudes_count']
        id = str('https://weibo.com/2645753453/') + str(d['id'])
        publish_time = d['created_at']
        time = datetime.strptime(publish_time, "%a %b %d %H:%M:%S +0800 %Y")
        print(user_id, text, user_name, reposts_count, comments_count, attitudes_count, id, time)
