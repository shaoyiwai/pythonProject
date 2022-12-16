import json
import requests
import re
from lxml import etree
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.append(['价格', '图片链接', '标题', '评论数'])
headers = {
    'authority': 'img11.360buyimg.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'zh-CN,zh;q=0.9',
    'referer': 'https://list.jd.com/',
    'sec-ch-ua': '^\\^Google',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '^\\^Windows^\\^',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


def get_data(page):
    response = requests.get(
        f'https://list.jd.com/list.html?cat=737,794,798&ev=4155_97865&sort=sort_rank_asc&trans=1&JL=3_%E7%94%B5%E8%A7%86%E7%B1%BB%E5%9E%8B_%E5%85%A8%E9%9D%A2%E5%B1%8F#J_crumbsBar&page={page}',
        headers=headers)
    html = etree.HTML(response.text)
    # /html/body/div[7]/div/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[2]/strong/i

    goods_list = html.xpath('/html/body/div[7]/div/div[2]/div[1]/div/div[2]/ul/li')
    for goods in goods_list:
        title = goods.xpath('./div/div/a/@title')[0]
        # print(title)
        url = goods.xpath('./div/div/a/@href')[0]
        price = goods.xpath('./div/div[2]/strong/i/text()')[0]
        good_id = url.split('/')[-1].split('.')[0]
        if url.split('/')[0] == 'https:':
            pass
        else:
            url = 'https:' + goods.xpath('./div/div/a/@href')[0]
        try:
            comment_url = f'https://club.jd.com/comment/getProductPageFoldComments.action?callback=jQuery3749069&productId={good_id}&score=0&sortType=5&page=0&pageSize=5'
            resp = requests.get(comment_url, headers=headers)
            # print(resp.text)
            # network-response中找对应的响应
            # 字符串转变为字典data = re.findall(r'jQuery3749069\((.*?)\);', resp.text)[0]
            data = json.loads(data)
            print(type(data))
            comment_count = data['productCommentSummary']['commentCountStr']
            print(title, url, price, comment_count)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    for page in range(1, 8, 2):
        print(page)
        get_data(page)
