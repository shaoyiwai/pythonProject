import requests
from lxml import etree
import time
import json
import re

cookies = {
    '__jdu': '16697973609861973430686',
    'areaId': '12',
    'PCSYCityID': 'CN_320000_320500_0',
    'shshshfpa': '9d0899d5-6388-329a-8609-770cd3216379-1669797362',
    'shshshfpb': 'i1KgI8ce389g2fheB71juzg',
    'jwotest_product': '99',
    'ipLoc-djd': '12-988-993-58088',
    'mt_xid': 'V2_52007VwMVVVVeWlwdThhUDGADGlRfXVBbGEAebFJkChtTWAxVRk0bS1oZYlBAAUFQUAkaVRsOADdXRgcJW1RZT3kaXQZkHxJSQVpTSx9PElgFbAIXYl9oUmoYTRtdDW4BFFVVaFJcG00^%^3D',
    'TrackID': '1WToSN7zmqakrMHtbX76gikSBQD9RWeQzxWdzDhtVZF-uH7p6zZVYoWVkRNgQ8M-gPegDismSFT_P4y_n4wihYavDYe1a-rnZFyZ7kvCiSg8',
    'pinId': 'Sz8VboC6aGCiZfO1EyMuKLV9-x-f3wj7',
    'pin': 'jd_71df3bd89b42a',
    'unick': 'jd_153700bwf',
    'ceshi3.com': '103',
    '_tp': 'tkeHxNSpnvzEgFFN8W^%^2BanxWerAjl07npU5UV5^%^2Bgf^%^2BD0^%^3D',
    '_pst': 'jd_71df3bd89b42a',
    'unpl': 'JF8EALRnNSttCx5XBRJXThoVQl9RW1gIG0dTP2MCXVsKQlcDGVZLExh7XlVdXhRLFB9uYxRUW1NOUA4bAisSEXtdVV9fD0oeBm5vNWRcNks6cVxpHEBySlw3Vzo4SBczblcFU1pQTVwDGQUaGhlMXVxYXw1JFgRmYDVVbVhDUDUrMh4SEUpcXFlcD0onAl9lBFVYXEpTBBgFK1l-ShBUWVoATR8FbWAEXFRfS1wDGQcZExdCWmRfbQs',
    '__jdv': '76161171^|www.baidu.com^|t_1003608409_^|tuiguang^|bd218dd94834441aaaa5687c8273ea09^|1670233510788',
    'jsavif': '1',
    '__jda': '122270672.16697973609861973430686.1669797361.1670221466.1670233511.10',
    '__jdc': '122270672',
    'shshshfp': 'a21c7946e2e731be7c41b3c56dbb5f26',
    'thor': '731FE249D37B626EBD513C2628B245CE11FABBBE03B1C4C3D43B691149E9D51E36F219791CC665A2DAE764CF695CFBC8FD81B8D6758873D175CCCFD9E9790F459B214AA1B7A0C0E3F6916F56728240C8C8245970F01C2B4A4B088ACD0B8F4B58E131BD2E6BE5034316A82C7A98EB7F20A0E0670946A1D1C0D1EE7016292B93C342895A53D1EC813E0656F4CA7E15949BA6619E124B9E8CB53902D96F789AC4CD',
    '3AB9D23F7A4B3C9B': 'KBZSQCD3ILBEIUIP65WEUW5F7CYWMFZJTRKLEL2CATF5WYWZAG6NW6UMSBFIVLQFTHIH7L3SG343WFESIOQEFHD7HY',
    '__jdb': '122270672.8.16697973609861973430686^|10.1670233511',
    'shshshsID': '6e71ac774ff8a9f3637898ae5697b299_8_1670233984411',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Referer': 'https://search.jd.com/',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'sec-ch-ua': '^\\^Google',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '^\\^Windows^\\^',
}

# 修改链接
response = requests.get(
    'https://search.jd.com/Search?keyword=%E7%81%AB%E9%94%85&enc=utf-8&wq=huoguo&pvid=272fa0f638c645b382dc5b151a977542',
    headers=headers, cookies=cookies)
html = etree.HTML(response.text)
goods_list = html.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li')
for goods in goods_list:
    # 价格
    price = goods.xpath('./div/div[2]/strong/i/text()')[0]
    # 抬头 写了报错
    # title = goods.xpath('.//div[@class="p-name p-name-type-2"]//em')[0]
    # 店铺名
    shop_name = goods.xpath('./div/div[5]/span/a/@title')[0]
    # 详情页链接
    detail = goods.xpath('./div/div[1]/a/@href')[0]
    print(detail)
    # # 商品id
    item_id = detail.split('/')[-1].split('.')[0]
    print(item_id)
    # 评价跑不出来
    # try:
    comment_url = f'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={item_id}&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&rid=0&fold=1'
    resp = requests.get(comment_url, headers=headers, cookies=cookies).text
    print(resp)
    # 查看响应状态码
    # print(resp.status_code)
    # comment_dic = '{' + re.findall(r'\({(.*?)\);', resp)  [0]
    # comment_dic = json.loads(comment_dic)
    # print(comment_dic)
    # # 评论数
    # comment_count = comment_dic['productCommentSummary']['commentCountStr']
    # # 视频晒单
    # video = comment_dic['productCommentSummary']['videoCountStr']
    # # 好评
    # good_comment = comment_dic['productCommentSummary']['goodCountStr']
    # # 中评
    # general_comment = comment_dic['productCommentSummary']['generalCountStr']
    # # 好评率
    # good_rate = comment_dic['productCommentSummary']['goodRate']
    # print(comment_count, video, good_comment, general_comment, good_rate)
    # except Exception as e:
    #     print(e)
