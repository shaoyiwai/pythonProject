import requests
import csv
import time
import random
import json


def spider(page_num):
    main_url = "https://m.weibo.cn/api/container/getIndex?uid=3641513235&luicode=10000011&" \
               "lfid=231093_-_selffollowed&type=uid&value=3641513235&containerid=1076033641513235"
    # main_url为要爬取博主的主页地址

    if page_num:
        main_url = main_url + '&page=' + str(page_num)
    # 微博的分页机制是每页10条微博

    header = {
        "user-agent": "Mozilla / 5.0(X11; Linux x86_64) AppleWebKit / 537.36(KHTML, likeGecko) "
                      "Chrome / 77.0.3865.120Safari / 537.36",
    }  # 设置请求头

    cookie = {
        'cookies': "输入自己微博的cookie"
    }

    try:
        r = requests.get(url=main_url, headers=header, cookies=cookie)
        r.raise_for_status()
    except Exception as e:
        print("爬取失败", e)
        return 0

    result_json = json.loads(r.content.decode('utf-8'))
    info_list = []
    for card in result_json['data']['cards']:
        info_list_sub = []
        if card.get("mblog"):
            info_list_sub.append(card['mblog']['attitudes_count'])  # 获赞数

            info_list_sub.append(card['mblog']['comments_count'])  # 评论数

            info_list_sub.append(card['mblog']['reposts_count'])  # 转发数

            if page_num == 1:
                info_list_sub.append(card['mblog']['created_at'])  # 发博时间
            elif '2018' not in card['mblog']['created_at']:
                info_list_sub.append(card['mblog']['created_at'])
            else:
                print("2019年微博爬取完毕")
                break

            info_list_sub.append(card['mblog']['weibo_position'])  # 是否原创

            if card['mblog'].get('raw_text'):
                info_list_sub.append(card['mblog']['raw_text'])  # 微博内容
            else:
                info_list_sub.append(card['mblog']['text'])

            # if card['mblog']['source'] == '':
            #     info_list_sub.append(None)
            # else:
            #     info_list_sub.append(card['mblog']['source'])

            time.sleep(random.randint(4, 6))  # 每爬取一条微博暂停4到6秒，防反爬

            info_list.append(info_list_sub)
        else:
            continue
    return info_list


def save_csv(infolist):
    with open('/home/long/Documents/weibo2.csv', 'a+', encoding='utf_8_sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(infolist)


def main(num):
    for i in range(1, num + 1):
        information = spider(i)
        save_csv(information)
        print("第%s页爬取完毕" % i)


if __name__ == '__main__':
    main(500)  # 爬取500页
