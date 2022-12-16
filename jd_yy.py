import requests
from lxml import etree
import re
import json

headers = {
    'authority': 'img11.360buyimg.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'zh-CN,zh;q=0.9',
    'referer': 'https://list.jd.com/',
    'Cookie': '__jdv=76161171|direct|-|none|-|1669797360987; __jdu=16697973609861973430686; areaId=12; PCSYCityID=CN_320000_320500_0; shshshfpa=9d0899d5-6388-329a-8609-770cd3216379-1669797362; shshshfpb=i1KgI8ce389g2fheB71juzg; jwotest_product=99; ipLoc-djd=12-988-993-58088; mt_xid=V2_52007VwMVVVVeWlwdThhUDGADGlRfXVBbGEAebFJkChtTWAxVRk0bS1oZYlBAAUFQUAkaVRsOADdXRgcJW1RZT3kaXQZkHxJSQVpTSx9PElgFbAIXYl9oUmoYTRtdDW4BFFVVaFJcG00%3D; pinId=7jejvSdKuRqE5tXrK5vzig; unick=%E8%BD%BB%E8%A7%A6%E7%9B%B4%E6%92%AD; _tp=t8maOhOFioqv1AvQ698KtjsXeUPQ8P258O%2F%2BjwXu2RhrcCXCVFyP1K7w%2B4gEYdiF; _pst=%E8%BD%BB%E8%A7%A6%E7%9B%B4%E6%92%AD; TrackID=13Ew45xrK1p_JXP_aMvmoGayP4cTEsmVREBjK6aOR3xENbXId7lbAiHHLVPOb0JGOmyvirz8lexIL2XTYmnqJrTCYpLVjlOro3BfuVpIDuoQ; ceshi3.com=000; pin=%E5%96%84%E5%AD%98%E6%97%97%E8%88%B0%E5%BA%97; bjd.advert.popup=e6ab85babfff7b2414f8e6204fff6d32; jsavif=1; __jda=122270672.16697973609861973430686.1669797361.1669860762.1669873678.5; __jdc=122270672; ip_cityCode=988; shshshfp=a21c7946e2e731be7c41b3c56dbb5f26; token=7d60837f8103179324c30624ad33c19e,3,927712; __tk=9fa0ac6e9dd9bf1bc3d3b569399d6135,3,927712; thor=E8D59764EC0307A7EA79E369127AC2F781C41230CE3EA9F76ECBFDAFAB9283FFE3715FF46E5878F44F305FFCAE1833A438995BDF31AB7275FE50C60A7E2C3C67965960544B69809F254669C2EFC17CC005D714DFEF3413BAB028A1CA93C74251DFBF50824E872C9EB059F9D8F597ADA5ADF14C01121CB008F78CC209FEFEE919; 3AB9D23F7A4B3C9B=KBZSQCD3ILBEIUIP65WEUW5F7CYWMFZJTRKLEL2CATF5WYWZAG6NW6UMSBFIVLQFTHIH7L3SG343WFESIOQEFHD7HY; JSESSIONID=0BD0D8F60A0AD5581EFD3E0CEF1A4D89.s1; shshshsID=0732da1360a3cb1204d52b82f55b8d55_25_1669882945660; __jdb=122270672.31.16697973609861973430686|5.1669873678',
    'sec-ch-ua': '^\\^Google',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '^\\^Windows^\\^',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


def get_data():
    response = requests.get(
        'https://search.jd.com/Search?keyword=inphone14&enc=utf-8&wq=inphone14&pvid=3fff8dc6f8424746a588662410187ebe',
        headers=headers)
    html = etree.HTML(response.text)
    # 可找到需要的数据，转化为xpath后，慢慢删减/
    # /html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li[2]
    goods_list = html.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li')
    index = 0
    for goods in goods_list:
        try:
            price = goods.xpath('./div/div[3]/strong/i/text()')[0]
            title = goods.xpath('./div/div[4]/a/@href')[0]
            shop = goods.xpath('./div/div[7]/span/a/@title')[0]
            # 获取全部内容
            goods_name = goods.xpath('.//div[@class="p-name p-name-type-2"]//em')
            name = goods_name[0].xpath('string(.)').strip()
            goods_id = title[14:-5]
            picture = re.findall(r'data-lazy-img="(.*?)"', response.text)[index]
            # comment_url = f'https://club.jd.com/comment/productCommentSummaries.action?referenceIds={goods_id}&categoryIds=9987,653,655&callback=jQuery5693591'
            # resp = requests.get(comment_url, headers=headers)
            # # 查看网站状态码
            # # print(resp.status_code)
            # comment_count = re.findall(r'"CommentCountStr":(.*?),', resp.text)[0]
            print(price, picture, shop, name)
            index += 2
        except Exception as e:
            print(e)


if __name__ == '__main__':
    get_data()
