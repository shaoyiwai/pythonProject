# import re
#
# import requests
# from lxml import etree
#
# headers = {
#     'authority': 'm.weibo.cn',
#     'cache-control': 'max-age=0',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-mode': 'same-origin',
#     'sec-fetch-dest': 'empty',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'cookie': '_T_WM=59253534889; XSRF-TOKEN=ea0056; WEIBOCN_FROM=1110005030; MLOGIN=0; __bid_n=184c2dba34919198cd4207; FPTOKEN=30^$rqOSxq1K/jWvtaGb6vV6H4UJhRvawwsDfPzDrQKId9E4qaSrXRg1xx25UdmbIokIqG3z9wFCdoyluOffahWtaJlrUjeGnrgKXmXOp8NekCochyA900rnGGzYqYY4akli9MKB/7MnixP+jy4rXXgebQgDzmEX7+qL4a5G2d2qhhp3UUzrOMkW8vakLq2Y4QWUNpyWUGl5aAUIKYNwtl2ecC/iQiXabf/SUUF/FXt+jX6aH7bmtlkskcrt4nTQgcz0SMzKKeoNsDkj6BVvVYHJsRysUibcEMArf7w9WIdzRxmOTfd+yu2ESzf1ORMU/24f3NLPaDvGpMt+3KaLRkS9M4zR/NqEHgFDmy9JOINbP3NXXznu1i+ziGBU0wS/IbcX^|3tkP3Mj81AhycNwwuPfzpVrJ/SDnMJUzVTOqJFzDlUU=^|10^|f2612f9544ad7cd864b56e7d75264467; mweibo_short_token=dd0577892c; M_WEIBOCN_PARAMS=oid^%^3D4839716568177674^%^26luicode^%^3D10000011^%^26lfid^%^3D1076032814929384^%^26uicode^%^3D20000061^%^26fid^%^3D4839716568177674',
# }
#
# response = requests.get('https://list.jd.com/list.html?cat=670,716,722', headers=headers).text
#
# comments = re.findall(r'"comments_count": (.*?),', response)
# report = re.findall(r'"reposts_count": (.*?),', response)
# print(report, comments)



import requests

headers = {
    'authority': 'weibo.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'client-version': 'v2.36.27',
    'cookie': 'PC_TOKEN=d3df5f0042; SUB=_2AkMU2VLxf8NxqwFRmPASyG3haI5zwwHEieKihaMqJRMxHRl-yT92qnQotRB6P1l8HhM9f0TjtLAZsM8yQyBtVgI_ciXD; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5Weg3XUbB2Q1Mwbb6vV5Jz; login_sid_t=e6a556e5b30fb186cb10c7e054f3f320; cross_origin_proto=SSL; WBStorage=4d96c54e^|undefined; _s_tentry=passport.weibo.com; Apache=3680856461271.6865.1669717448081; SINAGLOBAL=3680856461271.6865.1669717448081; ULV=1669717448084:1:1:1:3680856461271.6865.1669717448081:; wb_view_log=1536*8641.25; XSRF-TOKEN=BZSnikMhnX4YQ168ofzXHEHu; WBPSESS=eyDLPcU90tHVPRrsWrtAPpPXz743ICi_SyDLjAoxyGuEo8ooL-izZP9ejYCOrsPsXf6_NtUt4KqwLaaPC28U5Yq18u7sD2M3KAiGVzfNkGNv_RRmbA-4f4cpFZslziHco29GZah4WuGGkDao2aRd712EWpbRp6cjqQTL964Oeyw=',
    'referer': 'https://weibo.com/2814929384/4814370293420669',
    'sec-ch-ua': '^\\^Google',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '^\\^Windows^\\^',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'server-version': 'v2022.11.29.2',
    'traceparent': '00-4824e1d19f178067af34a3cf625c0e89-5a572a72b7fd9c67-00',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'BZSnikMhnX4YQ168ofzXHEHu',
}

params = (
    ('id', '4814370293420669'),
)

response = requests.get('https://weibo.com/ajax/statuses/show?id=4814370293420669', headers=headers,
                        params=params).json()

tag = response["tag_struct"][0]['tag_name']
print(tag)
