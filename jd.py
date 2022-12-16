import re

import requests
from lxml import etree

headers = {
    'authority': 'list.jd.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '__jdu=16697882635001885418633; TrackID=1Keq0gHMmQOzrdykZrSqA3CJuJcgCFwsCljge9ZMajdOnopGzeVcaU2nb798L4PtALtmeMJgMxxK5tto9l7KnzFc6Tp7arsZn30USHhiDcjw; pinId=7jejvSdKuRqE5tXrK5vzig; unick=%E8%BD%BB%E8%A7%A6%E7%9B%B4%E6%92%AD; _tp=t8maOhOFioqv1AvQ698KtjsXeUPQ8P258O%2F%2BjwXu2RhrcCXCVFyP1K7w%2B4gEYdiF; _pst=%E8%BD%BB%E8%A7%A6%E7%9B%B4%E6%92%AD; pin=%E5%96%84%E5%AD%98%E6%97%97%E8%88%B0%E5%BA%97; unpl=JF8EAMlnNSttXkwEBk8EHRtFQw5RW1gIGURUOGUMUQkITwEEGlETExJ7XlVdXhRLFx9tZhRUWFNOVw4YBisSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAhwVGE1UXV1aCk8WAm9uDFBYWEJTBxkyGiIXe21kV1kNSxQzblcEZB8MF1YHGgUdG11LWlNWWwFCFARtYwRVXVFCUAAbCxwQEntcZF0; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_76a2e778d9b4441cbff384ea5d00b903|1669790547293; areaId=12; PCSYCityID=CN_320000_320500_0; bjd.advert.popup=e45a485f14375434c29c8cb1e8469ca7; smb_track=5523CAD63FF641258A935E10B6B1F37D; __jda=122270672.16697882635001885418633.1669788263.1669788263.1669790547.2; __jdc=122270672; jsavif=1; jsavif=1; shshshfp=a21c7946e2e731be7c41b3c56dbb5f26; shshshfpa=854816b9-b219-8c3b-1d1d-e0aaa0fa932d-1669790704; shshshfpb=sUQ1nAtAEZnydQdreRRQtNA; avif=1; token=24989b55cea6426c1ac01a7900782995,2,927661; __tk=e2cb625f78fedfe40c2471d59ccd0bf6,2,927661; ip_cityCode=988; ipLoc-djd=12-988-993-58088; 3AB9D23F7A4B3C9B=X4VBCPNXTOSM7EDFWBT3OHAGOJO7L5IFVGC4H5IYXJRH3EXOK7QQG4XJZ2WJC6QQLGNFQ2SPPUS6RKP5PQOSKPVY5A; __jdb=122270672.14.16697882635001885418633|2.1669790547; shshshsID=7a9e8ae92360a74d3ae9e0ad847d9179_7_1669791611800',
    'referer': 'https://list.jd.com/list.html?cat=670,716,722',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

response = requests.get('https://list.jd.com/list.html?cat=670,716,722', headers=headers)
# print(response.text)
price = re.findall(r'data-price="10048912518848">\((.*?)</i>', response.text)[0]
print(price)

