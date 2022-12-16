import json
import re
import time

import requests
from lxml import etree
from xlrd import sheet
from openpyxl import Workbook
from pymysql import *

# conn = connect(host='rm-uf664y8bsz73u37odio.mysql.rds.aliyuncs.com', port=3306, database='jd_notes', user='luming',
#                password='Luming1314', charset='utf8')
# cursor = conn.cursor()

wb = Workbook()
ws = wb.active
ws.append([
    '标题',
    '价格',
    '店铺',
    '商品ID',
    '备注',
    '详情页网址',
    '商品图片网址',
    '所有评论',
    '视频晒单',
    '好评',
    '中评',
    '差评',
    '追评',
    '好评率(%)',
])

headers = {
    # 'authority': 'item.jd.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '__jdu=16522482835401340221388; shshshfpa=76c25328-0cc5-ad08-acc1-cf2b162a0a61-1652248285; shshshfpb=mtdSJv___ru3iBB2r3XR1VA; qrsc=3; pinId=PCUQqh2gZl-xWgI7hwRYvLV9-x-f3wj7; mba_muid=16522482835401340221388; visitkey=30410634254219337; TrackID=1_IHRF6ZY8HfTd3RsN3MlZBmZHywoIEy_5TJZ0BpSKe4OnrIZCa03-Gj8kBtf5rOox2-r8SVaY9HHxEt6QkndO1yUapzpB0CIQDhq4ammRCZkN9C0M6aYBACI0xjLsi9E; retina=0; cid=9; webp=1; __wga=1664266944237.1664266944237.1664266944237.1664266944237.1.1; sc_width=1920; _gia_s_local_fingerprint=2edcecf5b155c94013568f1fd7397b24; _gia_s_e_joint={"eid":"WIU2U435OV5RTO6JZY6R7QHUM4E5VZHLJ3JDIHJTCABS4HKSIPTPE3A6ALJVTRH4RHAAKZ53CN3Q24H7GXN3YUXRJM","ma":"","im":"","os":"Mac OS X","ip":"49.75.177.217","ia":"","uu":"","at":"5"}; equipmentId=WIU2U435OV5RTO6JZY6R7QHUM4E5VZHLJ3JDIHJTCABS4HKSIPTPE3A6ALJVTRH4RHAAKZ53CN3Q24H7GXN3YUXRJM; fingerprint=2edcecf5b155c94013568f1fd7397b24; deviceVersion=105.0.0.0; deviceOS=; deviceOSVersion=; deviceName=Chrome; jsavif=1; jsavif=1; __jda=122270672.16522482835401340221388.1652248284.1664266808.1665729006.42; __jdc=122270672; __jdv=122270672|direct|-|none|-|1665729006394; areaId=12; token=0ac1347e35202c7e5ac51b47c4a5f414,2,925405; __tk=90d308bea572ab1224d4a9a85ddcf59e,2,925405; ip_cityCode=988; ipLoc-djd=12-988-993-58088; avif=1; rkv=1.0; shshshfp=933db9f3956d7ce8e7ed49edf83b8176; __jdb=122270672.10.16522482835401340221388|42.1665729006; shshshsID=e85044e7403d3128eb11f9eed7b0eb90_10_1665731048424; 3AB9D23F7A4B3C9B=WIU2U435OV5RTO6JZY6R7QHUM4E5VZHLJ3JDIHJTCABS4HKSIPTPE3A6ALJVTRH4RHAAKZ53CN3Q24H7GXN3YUXRJM',
    'referer': 'https://list.jd.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
}


def get_data(keyword, page):
    list_url = f'https://search.jd.com/Search?keyword={keyword}&page={page}&enc=utf-8'
    # list_url = f'https://search.jd.com/Search?keyword={keyword}&qrst=1&psort=3&wq=%E9%A5%AE%E7%94%A8%E6%B0%B4&stock=1&psort=3&page={page}'
    # list_url = f'https://search.jd.com/search?keyword={keyword}&qrst=1&psort=3&stock=1&ev=exbrand_%E6%AC%A7%E8%8E%B1%E9%9B%85%5E&psort=3&pvid=428abed412974f4692c1305c9ad7023a&page={page}&s=61&click=0'

    resp = requests.get(list_url, headers=headers)
    # print(resp.text)
    # 创建etree对象
    tree = etree.HTML(resp.text)
    # titles= tree.xpath('//div[@id="J_searchWrap"]//div[@class="gl-i-wrap"]//div[@class="p-name p-name-type-2"]//em')
    # print(len(titles))
    # for title in titles:
    #     print(title.xpath('string(.)').strip())
    lis = tree.xpath('//ul[@class="gl-warp clearfix"]/li')
    for index, li in enumerate(lis):
        title_r = li.xpath('.//div[@class="p-name p-name-type-2"]//em')
        # print(title.xpath('string(.)').strip())
        title = title_r[0].xpath('string(.)').strip()
        title = title.replace('\n', '')
        # print(title.replace('\n',''))
        price = li.xpath('.//div[@class="p-price"]//i/text()')[0].strip()  # 价格

        # print(price)
        data_sku = li.xpath('./@data-sku')[0].strip()  # 商品唯一id
        # print(data_sku)
        # comment = li.xpath('.//div[@class="p-commit"]//a')  # 评论数
        shop_name = li.xpath('.//div[@class="p-shop"]//a//text()')[0].strip()  # 商铺名字
        # print(shop_name)
        icons = li.xpath('.//div[@class="p-icons"]/i/text()')  # 备注
        # comment = comment[0] if comment != [] else ''
        icons_n = ''
        for x in icons:
            icons_n = icons_n + x.replace('\n', '')
            icons_n = icons_n + ';'
        # print(icons_n)
        detail_url = li.xpath('.//div[@class="p-name p-name-type-2"]/a/@href')[0]  # 详情页网址
        detail_url = 'https:' + detail_url
        # print(re.findall(r'data-lazy-img="(.*?)"', resp.text)[1])
        image_url = 'https:' + re.findall(r'data-lazy-img="(.*?)"', resp.text)[index]  # 图片网址

        # print(detail_url)
        with open("cookies.txt", "r") as f:
            headers['cookie'] = json.load(f)
        comment_url = f'https://club.jd.com/comment/productCommentSummaries.action?referenceIds={data_sku}'
        time.sleep(1)
        comments = requests.get(comment_url, headers=headers).json()
        # print(comments)
        info = {}
        commentscount = comments['CommentsCount'][0]
        all_comments = commentscount['CommentCountStr']
        videocount = commentscount['VideoCountStr']
        poorcount = commentscount['PoorCountStr']
        aftercount = commentscount['AfterCountStr']
        goodcount = commentscount['GoodCountStr']
        generalcount = commentscount['GeneralCountStr']
        goodrate = commentscount['GoodRate'] * 100
        item = [title, price, shop_name, data_sku, icons_n, detail_url, image_url, all_comments, videocount, goodcount,
                generalcount, poorcount, aftercount, goodrate]
        print(item)
        ws.append(
            [title, price, shop_name, data_sku, icons_n, detail_url, image_url, all_comments, videocount, goodcount,
             generalcount, poorcount, aftercount, goodrate])
        wb.save(rf'./data/jd_{keyword}.xlsx')


if __name__ == '__main__':
    # '晨光', '猫太子', '蒙马特', '天文', '齐心', '广博', '国誉', '百乐', '斑马', '三菱', '科密'
    keyword = 'iPhone14'
    try:
        for page in range(1, 3):
            get_data(keyword, page)
            time.sleep(1)
    except Exception as e:
        print(e)
