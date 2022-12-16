import requests
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.append([
    '达人名',
    '场均销售额',
    '直播销售总额',
    '直播场次',
    '平均UV价值',
    '带货转化率',
    '粉丝总量',
    '平均场观',
    '平均停留时间'
])
headers = {
    'authority': 'api-service.chanmama.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'CMM_A_C_ID=fa48b49e-7c21-11ed-ab02-c6fd23be218c; Hm_lvt_1f19c27e7e3e3255a5c79248a7f4bdf1=1670401891,1671072089; LOGIN-TOKEN-FORSNS=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6MTAwMDAsImV4cGlyZV90aW1lIjoxNjcxNjQ5MjAwLCJpYXQiOjE2NzEwOTY1NjEsImlkIjo1MDkyNTgxLCJyayI6IlB6SDZWIn0.6pUWxZTDrDbvW2XkPtOEkuFwQrCaZxm19jPa25pIC-k; Hm_lpvt_1f19c27e7e3e3255a5c79248a7f4bdf1=1671097087; Authorization-By-CAS=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBfaWQiOjEwMDAwLCJleHAiOjE2NzE2NDkyMDAsImlhdCI6MTY3MTA5NzE0NywicmsiOiJPM0RBUyIsInVuaXF1ZV9pZCI6IlVTRVItQlZUNkk2UzBUWFE4LUZGMDA3TiJ9._LAj4I6fUcCLltFK91YMNSH_5ihN7hwsJfxB-lyXDJY',
    'origin': 'https://www.chanmama.com',
    'pragma': 'no-cache',
    'referer': 'https://www.chanmama.com/bloggerRank?keyword=',
    'sec-ch-ua': '^\\^Google',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '^\\^Windows^\\^',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-client-id': '114589791',
}


def chanmama(page):
    response = requests.get(f'https://api-service.chanmama.com/v2/home/author/search?keyword=&author_type=1&goods_cat=&star_category=&star_sub_category=&gender=-1&age=&province=&fans_gender=-1&fans_age=&fans_province=&live_price_preference=&aweme_price_preference=&live_purchase_intention=&aweme_purchase_intention=&follower_count=&take_product_method=0&verification_type=0&author_level=&is_brand_self_author=0&is_shop_author=0&is_star_author=0&is_low_fans_high_gmv=0&is_commerce=0&author_self_play=0&take_product_level=&take_product_price=&reputation_level=-1&live_watch_count=&live_average_amount_30_v2=&gpm=&digg_count=&is_ignore_government=1&contact=0&similar_author_id=&page={page}&size=50&sort=live_average_amount_30_v2&bring_product_brand=&order_by=desc&from=detail',headers=headers).json()
    info_list = response['data']['list']
    for i in info_list:
        nickname=i['nickname']
        live_average_amount_30_v2_text=i['live_average_amount_30_v2_text']
        live_total_amount_30_text=i['live_total_amount_30_text']
        live_count_30=i['live_count_30']
        live_average_uv_30=i['live_average_uv_30']
        live_rate_30=i['live_rate_30']
        live_average_user_30=i['live_average_user_30']
        live_average_online_30=i['live_average_online_30']
        seconds = live_average_online_30
        m, s = divmod(seconds, 60)
        live_rate_31=str(live_count_30)+str('%')
        follower_count = i['follower_count']
        print(nickname,live_average_amount_30_v2_text,live_total_amount_30_text,live_count_30,live_average_uv_30,live_rate_31,follower_count,live_average_user_30,"%02d:%02d" % (m, s))
        ws.append(
            [nickname,live_average_amount_30_v2_text,live_total_amount_30_text,live_count_30,live_average_uv_30,live_rate_31,follower_count,live_average_user_30,"%02d:%02d" % (m, s)])
        wb.save(r'C:\Users\qchd\Desktop\蝉爬虫.xlsx')
if __name__ == '__main__':
    for page in range(1, 3):
        print(page)
        chanmama(page)