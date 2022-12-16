import time
import pandas as pd
import re
from openpyxl import Workbook
import asyncio
import httpx

wb = Workbook()
ws = wb.active
ws.append(['商品ID', '类目'])

headers = {
    'authority': 'item.jd.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie':'__jdu=1661934289632614864786; __jdv=256844112|direct|-|none|-|1666676075351; areaId=12; PushSharp=a8f95803-cb30-e1e5-49e6-12c29d085a0b-1667466504; shshshfpb=tQrn1ZqvVXcUt6hJwHWzFrg; jsavif=1; jsavif=1; __jda=122270672.1661934289632614864786.1661934290.1667459024.1667466498.62; __jdc=122270672; rkv=1.0; token=bf1cb87485b397dcd8572249f4e5bbf9,2,926370; __tk=ickwnZnCnlnKVliJVZaFiZiERxbyV0iJR0RwRlfOWZe,2,926370; ip_cityCode=988; ipLoc-djd=12-988-993-58088; shshshfp=9f21401f6ea65d4ba0c5747c991e715f; wlfstk_smdl=qnibr2rauseu76c8qwh7msf3ryshzbmp; 3AB9D23F7A4B3C9B=VAND3UFNZHWK5VBGJ6NTJPUV7JEEGZR645AEQFXMK52SYDS5MA2GWXOQMESLLR7TDBJ2ES2QHMYK57CP63NR3QGCAQ; TrackID=1kYiOdojEh9bi7K14Ri_0CYQT2R_7yT3Y23ttAYH3_7xLF5liBFBCQaf31yJwAIEVc5-UM2ON_11QUXt861l4TSUFHfpvHEeiWbNoegplkKQ; thor=731FE249D37B626EBD513C2628B245CE11FABBBE03B1C4C3D43B691149E9D51EBD662FBC405087E78448EC2F368E472EC58F4BCBFBF86DFF9DAB75449B458211F8E0A3560E9B10C6EB6A3D928192334643B4B0121E37B1E3D1AEBB93DCF950ACAC9A62F82F32DB5B8A5FF1DD6FFFF292D2EABFDEE7A917B7F88BBBF44D7444012FB8D986C950204EE1F8B9BD5497B7E01F4E51A1785813808996BAF37292137C; pinId=Sz8VboC6aGCiZfO1EyMuKLV9-x-f3wj7; pin=jd_71df3bd89b42a; unick=jd_153700bwf; ceshi3.com=103; _tp=tkeHxNSpnvzEgFFN8W%2BanxWerAjl07npU5UV5%2Bgf%2BD0%3D; _pst=jd_71df3bd89b42a; avif=1; __jdb=122270672.15.1661934289632614864786|62.1667466498; shshshsID=6713f0cea97a762c09b46bc4fbe706b8_8_1667466774851; qrsc=3',
    'pragma': 'no-cache',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/103.0.0.0 Safari/537.36',
}


async def get_data(g_id):
    try:
        async with httpx.AsyncClient(verify=False, timeout=30) as client:
            # 设置了https不验证和超时时间为30秒
            response = await client.get(url=f'https://item.jd.com/{g_id}.html', headers=headers)
            # print(type(response.text))
            category = re.findall(r'catName: (.*?)]', response.text)[0]
            print([g_id, category])
            ws.append([g_id, category])
            wb.save(r'./category/jd_category.xlsx')
    except Exception as e:
        print(e)


async def main():
    tasks = []
    df = pd.read_excel(r'./urls.xlsx')
    g_ids = df['商品ID']
    for g_id in g_ids:
       tasks.append(asyncio.create_task(get_data(g_id)))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    # async_start = time.time()
    asyncio.run(main())
    # async_end = time.time()
    # print(async_end - async_start)



