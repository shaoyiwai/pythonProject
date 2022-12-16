import requests
import json
import re
import string
from datetime import datetime
from datetime import timedelta
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.append([
    '文章内容',
    '用户名',
    '粉丝数',
    '评论量',
    '转发数',
    '点赞数',
    '文章链接',
    '发文时间',
])
headers = {
    'authority': 'js.t.sinajs.cn',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://s.weibo.com/',
    'sec-ch-ua': '^\\^Google',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '^\\^Windows^\\^',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'cookie': 'SINAGLOBAL=6077043461805.43.1670483353611; SSOLoginState=1670830294; XSRF-TOKEN=LHPwna6HTgDKsVbbgMXubApu; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWL5TqjR_-bH_akCNkAPUay5JpX5KMhUgL.FoMfeoz0SheRehq2dJLoI7DKC28lg-LPx-4k; ALF=1673508812; SCF=An-OiVklaBY4o-Vpd0sqzaoJhcysdotu5q8H89hcK3xxZheZQoQjVErR4FBUFzDs1lj-H-Z4qczsXH7cKXmJPVk.; SUB=_2A25OnFqADeRhGeFL6VAS9C3EyzqIHXVt6MtIrDV8PUNbmtAfLXXSkW9NQkXMHSAsRNJ6JgN24Wb7FI4q4S-gqg9C; _s_tentry=weibo.com; Apache=2295195075121.6167.1670922700595; ULV=1670922700604:2:2:1:2295195075121.6167.1670922700595:1670483353613; WBPSESS=mhAVYH3h1H1HWAai7Rl_vG5NxWLcW13Mr8JKTLoWndwBeGgNEAx6w4eI4NSJDCDBURI4yy-A2KTy992_SOtUtcg8REroBdFf3Bha9lK_omy-uyRVfESPyTWDul7wn_fOLMVWGzZBwuxBnPsAIdnZMw==',
}


def get_vb(keyword_vb, page):
    resp = requests.get(
        f'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D{keyword_vb}&page_type=searchall&page={page}',
        headers=headers).json()
    info_list = resp['data']['cards']
    # print(info_list)
    for i in info_list:

        if 'card_group' in i.keys() and 'mblog' in i['card_group'][0].keys():
            info = i['card_group'][0]['mblog']['text']
            user_id = i['card_group'][0]['mblog']['user']['screen_name']
            fans = i['card_group'][0]['mblog']['user']['followers_count']
            comments_count = i['card_group'][0]['mblog']['comments_count']
            id1 = i['card_group'][0]['mblog']['id']
            created_at = i['card_group'][0]['mblog']['created_at']
            time = datetime.strptime(created_at, "%a %b %d %H:%M:%S +0800 %Y")
            id2 = 'https://m.weibo.cn/detail/' + id1
            reposts_count = i['card_group'][0]['mblog']['reposts_count']
            attitudes_count = i['card_group'][0]['mblog']['attitudes_count']
            scheme = i['card_group'][0]['scheme']
            text = re.sub(r'<.*?>', '', info)
            print(text, user_id, fans, comments_count, reposts_count, attitudes_count, id2, time)
        elif 'mblog' in i.keys():
            info = i['mblog']['text']
            user_id = i['mblog']['user']['screen_name']
            fans = i['mblog']['user']['followers_count']
            comments_count = i['mblog']['comments_count']
            comments_count = i['mblog']['comments_count']
            reposts_count = i['mblog']['reposts_count']
            id1 = i['mblog']['id']
            created_at = i['mblog']['created_at']
            time = datetime.strptime(created_at, "%a %b %d %H:%M:%S +0800 %Y")
            id2 = 'https://m.weibo.cn/detail/' + id1
            attitudes_count = i['mblog']['attitudes_count']
            text = re.sub(r'<.*?>', '', info)
            print(text, user_id, fans, comments_count, reposts_count, attitudes_count, id2, time)
        ws.append(
            [text, user_id, fans, comments_count, reposts_count, attitudes_count, id2, time])
        wb.save(r'C:\Users\qchd\Desktop\圣诞.xlsx')


if __name__ == '__main__':
    keyword_vb = '圣诞'
    for page in range(1, 3):
        print(page)
        get_vb(keyword_vb, page)
