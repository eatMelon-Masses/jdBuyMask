# -*- coding=utf-8 -*-
'''
京东抢购口罩程序
'''
import requests
import time
import json
import sys
import random
from bs4 import BeautifulSoup
from jdlogger import logger
from message import message
import traceback

'''
需要修改
'''
# cookie 网页获取
cookies_String = '__jda=187205033.15853681959841992115139.1585368196.1586061947.1586074246.4; __jdb=187205033.10.15853681959841992115139|4.1586074246; __jdc=187205033; __jdu=15853681959841992115139; _distM=111968085399; 3AB9D23F7A4B3C9B=KG6ZONOU6TBVCG44CBZRFEGBKGTIJKYPPVBYBJTT4ID3DX7KE5UQV6XQ3PDZRTYTGZBO6JQBPR63KU6DBGYFBUVLX4; cn=2; ipLoc-djd=22-1930-50949-52154.2062088666; __tak=7fd2f674a85f73cc6af476f5199a6267fe2a06f64f018953c6128967cd23f3638b76e4c994ad0e13fca3b904c7ba45458d73ce77de25289ea7a46a83fbf680a960274276d3da5f0b07001127f0eb1559; ipLocation=%u56db%u5ddd; thor=6EF796BC324FB923104802A01A24B5D03DE1A720BAF379CEE89FC618559FF8EB042F29F02D87EF0D59954DF63185B77D2816CEC480009CC0A6E7F5BFD111DEA61EF0CD905A33643689CAB234940F71317CF6B74494428216140127BCDD9379393E3747558CAAC23249F77091EE521C9D7DB8CA6A6072A3DD59DFBC48E0FEE4D1BC6CC8BC82FAF9312EAB58106ED49DA75F261E9D0B205CEC61DC259D4ACF4B83; shshshfpa=34bb4323-bc7f-16ae-b1df-2c3271bc652a-1584281871; shshshfpb=ds9NXG5zKnOVPqNL3tucwRA%3D%3D; shshshsID=42cefd70d93647ca61bed4b7ec22f26e_2_1586074556020; shshshfp=1c595395dbe8a4b6a82f7f767d5cd924; TrackID=1qgV6g1CVBbaRLwvKYMVQYZtRW7vFz2_n1VbM5Gi5LKxDDMIT8GsikrL5S5sFV98vvjHSA6CzKtFWCBwCl8dH4tr-RI7KCdNrhLHyjPTVJmJ-8DKw_-DlUic84KRfF9SE1mAfpG397r74FYhmYtPzMw; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_ccdffbaff1b64a5cab414aec05e9fc9c|1586074462869; _pst=jd_5276257e79e2f; _tp=1xiBcyVp1IF%2BI7s2yDplp3ehHjVDLKdqrOM%2FAkurU9k%3D; ceshi3.com=000; pin=jd_5276257e79e2f; pinId=sRTBeGHwumPzwQLkRX8p67V9-x-f3wj7; unick=jd_199832jlw; wlfstk_smdl=sx81j0nn1lfmpqbg510j6rpyiinvmwsf; CCC_SE=ADC_GKjFdfq9LTSaN58aU%2fk4INGKFdWjcdwgkjKhGG0AjzsISxlLHlscNJQCTYv3HA0nKeGph42p0dCxKBndM7WImbiNMIaa9a26WmPVSIVgA38G26FW2rwwYFXgCSdFKVIYwVhgaUSmVnhC9ic2ghfh%2fz%2f1jfwdI2hzS1YTJXLK9LpPSzCL9yFRGQJgdhUEDuMvTez%2bJPm9ZbxUaRkCtkx%2bd1JkHEIQBO%2bEtYwxAKg16oX0WZsAgzsnsBfxeHsOCTblRTxhtMRT%2b2X34SLAuK%2f2CR3Pk75aQQAeJXGZmKzQV9V%2bhlv7dx%2fiYDz1gv7PiTALeQR5EkvSJxuzz5mEqB40WCGtl3hYiEYcZUnYfbsRPS%2flu6dlTTXKEGO1NGJHyIi577%2biH0TRvd75%2b2qGdkJVQfEtR%2bJKuvkzrkDKGWdytYTCKhEKrDVbiZzFgsRDzpq17xQUtDwtPpjoowSUL%2fPO9ahvKYF%2fVPoiyhTrO3xpLhX5h76tobS3aTX4yIHr5vjNy88uLC2081Y7UhXz7sNebMmYV9DHwJLJklkv2LCkC%2beXBFG%2bu4p5MmCnumrFLQTT14IEC4usU2KLbbzmKRCr0x6fXXhkxdecgWUzazoB7dPQ%2fv7ThRvtQw2JrsPtYl%2bI; unpl=V2_ZzNtbRAFFkIiWxYDLBkPAmJTFg8SBEYVcFgSBnodCA0wURoPclRCFnQUR1FnGFgUZwQZXUNcRhFFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsdVQFlBBtdSlNLHHAITlx4GVwBZwEabXJQcyVFCEZTchpcNWYzE20AAx8XdwBDUH1UXAFuBxBaS1dLEX0BQ1RzEV8FZwcSX0pnQiV2; cid=NW1UMTUyNmxPMTUyN2haMzUwOHNDMDc0MXhHMzk0MnFZMjU0M21RNzc0NHVINTM4; user-key=8c3dee21-02e8-442d-b959-38b8b134783f; PCSYCityID=CN_510000_510100_510116; areaId=22'

# 推送方式 1（mail）或 2（wechat）
messageType = 2

# 有货通知 收件邮箱
mail = '11764404@qq.com'

# 方糖微信推送的key  不知道的请看http://sc.ftqq.com/3.version
sc_key = 'SCU89262Tfe2687cea35f7423094724914be1ae9f5e6b912ce914a'

# 商品的url
urls = [
    # 'https://c0.3.cn/stock?skuId=1336984&area=19_1607_4773_0&venderId=1000078145&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=jd_7c3992aa27d1a&pduid=1580535906442142991701&ch=1&callback=jQuery6715489',
    # 'https://c0.3.cn/stock?skuId=4642656&area=19_1607_4773_0&venderId=1000006724&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=jd_7c3992aa27d1a&pduid=1580535906442142991701&ch=1&callback=jQuery4552086',
    # 'https://c0.3.cn/stock?skuId=65466451629&area=19_1607_4773_0&venderId=127922&buyNum=1&choseSuitSkuIds=&cat=9855,9858,9924&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=jd_7c3992aa27d1a&pduid=1580535906442142991701&ch=1&callback=jQuery2790674',
    # 'https://c0.3.cn/stock?skuId=65437208345&area=19_1607_4773_0&venderId=127922&buyNum=1&choseSuitSkuIds=&cat=9855,9858,9924&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=jd_7c3992aa27d1a&pduid=1580535906442142991701&ch=1&callback=jQuery1749958',
    # 'https://c0.3.cn/stock?skuId=7498169&area=19_1607_4773_0&venderId=1000128491&buyNum=1&choseSuitSkuIds=&cat=9855,9858,9924&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=jd_7c3992aa27d1a&pduid=15631231857651045904648&ch=1&callback=jQuery4102801',
    # 'https://c0.3.cn/stock?skuId=7498165&area=19_1607_4773_0&venderId=1000128491&buyNum=1&choseSuitSkuIds=&cat=9855,9858,9924&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=jd_7c3992aa27d1a&pduid=15631231857651045904648&ch=1&callback=jQuery9614479',
    'https://c0.3.cn/stock?skuId=7263128&area=19_1607_4773_0&venderId=1000128491&buyNum=1&choseSuitSkuIds=&cat=9855,9858,9924&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=jd_7c3992aa27d1a&pduid=15631231857651045904648&ch=1&callback=jQuery8872960',
    # 'https://c0.3.cn/stock?skuId=1739089&area=19_1607_4773_0&venderId=1000017287&buyNum=1&choseSuitSkuIds=&cat=15248,15250,15278&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=jd_7c3992aa27d1a&pduid=1580535906442142991701&ch=1&callback=jQuery4479703'
]

'''
备用
'''


# eid
eid = ''
fp = ''
# 支付密码
payment_pwd = ''
message = message(messageType=messageType, sc_key=sc_key, mail=mail)
session = requests.session()
session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Connection": "keep-alive"
}
manual_cookies = {}


def get_tag_value(tag, key='', index=0):
    if key:
        value = tag[index].get(key)
    else:
        value = tag[index].text
    return value.strip(' \t\r\n')


def response_status(resp):
    if resp.status_code != requests.codes.OK:
        print('Status: %u, Url: %s' % (resp.status_code, resp.url))
        return False
    return True


for item in cookies_String.split(';'):
    name, value = item.strip().split('=', 1)
    # 用=号分割，分割1次
    manual_cookies[name] = value
    # 为字典cookies添加内容

cookiesJar = requests.utils.cookiejar_from_dict(manual_cookies, cookiejar=None, overwrite=True)
session.cookies = cookiesJar


def validate_cookies():
    for flag in range(1, 3):
        try:
            targetURL = 'https://order.jd.com/center/list.action'
            payload = {
                'rid': str(int(time.time() * 1000)),
            }
            resp = session.get(url=targetURL, params=payload, allow_redirects=False)
            if resp.status_code == requests.codes.OK:
                logger.info('登录成功')
                return True
            else:
                logger.info('第【%s】次请重新获取cookie', flag)
                time.sleep(5)
                continue
        except Exception as e:
            logger.info('第【%s】次请重新获取cookie', flag)
            time.sleep(5)
            continue


def getUsername():
    userName_Url = 'https://passport.jd.com/new/helloService.ashx?callback=jQuery339448&_=' + str(
        int(time.time() * 1000))
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Referer": "https://order.jd.com/center/list.action",
        "Connection": "keep-alive"
    }
    resp = session.get(url=userName_Url, allow_redirects=True)
    resultText = resp.text
    resultText = resultText.replace('jQuery339448(', '')
    resultText = resultText.replace(')', '')
    usernameJson = json.loads(resultText)
    logger.info('登录账号名称' + usernameJson['nick'])


'''
检查是否有货
'''


def check_item_stock(itemUrl):
    response = session.get(itemUrl)
    if (response.text.find('无货') > 0):
        return True
    else:
        return False


'''
取消勾选购物车中的所有商品
'''


def cancel_select_all_cart_item():
    url = "https://cart.jd.com/cancelAllItem.action"
    data = {
        't': 0,
        'outSkus': '',
        'random': random.random()
    }
    resp = session.post(url, data=data)
    if resp.status_code != requests.codes.OK:
        print('Status: %u, Url: %s' % (resp.status_code, resp.url))
        return False
    return True


'''
购物车详情
'''


def cart_detail():
    url = 'https://cart.jd.com/cart.action'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Referer": "https://order.jd.com/center/list.action",
        "Host": "cart.jd.com",
        "Connection": "keep-alive"
    }
    resp = session.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")

    cart_detail = dict()
    for item in soup.find_all(class_='item-item'):
        try:
            sku_id = item['skuid']  # 商品id
        except Exception as e:
            logger.info('购物车中有套装商品，跳过')
            continue
        try:
            # 例如：['increment', '8888', '100001071956', '1', '13', '0', '50067652554']
            # ['increment', '8888', '100002404322', '2', '1', '0']
            item_attr_list = item.find(class_='increment')['id'].split('_')
            p_type = item_attr_list[4]
            promo_id = target_id = item_attr_list[-1] if len(item_attr_list) == 7 else 0

            cart_detail[sku_id] = {
                'name': get_tag_value(item.select('div.p-name a')),  # 商品名称
                'verder_id': item['venderid'],  # 商家id
                'count': int(item['num']),  # 数量
                'unit_price': get_tag_value(item.select('div.p-price strong'))[1:],  # 单价
                'total_price': get_tag_value(item.select('div.p-sum strong'))[1:],  # 总价
                'is_selected': 'item-selected' in item['class'],  # 商品是否被勾选
                'p_type': p_type,
                'target_id': target_id,
                'promo_id': promo_id
            }
        except Exception as e:
            logger.error("商品%s在购物车中的信息无法解析，报错信息: %s，该商品自动忽略", sku_id, e)

    logger.info('购物车信息：%s', cart_detail)
    return cart_detail


'''
修改购物车商品的数量
'''


def change_item_num_in_cart(sku_id, vender_id, num, p_type, target_id, promo_id):
    url = "https://cart.jd.com/changeNum.action"
    data = {
        't': 0,
        'venderId': vender_id,
        'pid': sku_id,
        'pcount': num,
        'ptype': p_type,
        'targetId': target_id,
        'promoID': promo_id,
        'outSkus': '',
        'random': random.random(),
        # 'locationId'
    }
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Referer": "https://cart.jd.com/cart",
        "Connection": "keep-alive"
    }
    resp = session.post(url, data=data)
    return json.loads(resp.text)['sortedWebCartResult']['achieveSevenState'] == 2


'''
添加商品到购物车
'''


def add_item_to_cart(sku_id):
    url = 'https://cart.jd.com/gate.action'
    payload = {
        'pid': sku_id,
        'pcount': 1,
        'ptype': 1,
    }
    resp = session.get(url=url, params=payload)
    if 'https://cart.jd.com/cart.action' in resp.url:  # 套装商品加入购物车后直接跳转到购物车页面
        result = True
    else:  # 普通商品成功加入购物车后会跳转到提示 "商品已成功加入购物车！" 页面
        soup = BeautifulSoup(resp.text, "html.parser")
        result = bool(soup.select('h3.ftx-02'))  # [<h3 class="ftx-02">商品已成功加入购物车！</h3>]

    if result:
        logger.info('%s  已成功加入购物车', sku_id)
    else:
        logger.error('%s 添加到购物车失败', sku_id)


def get_checkout_page_detail():
    """获取订单结算页面信息

    该方法会返回订单结算页面的详细信息：商品名称、价格、数量、库存状态等。

    :return: 结算信息 dict
    """
    url = 'http://trade.jd.com/shopping/order/getOrderInfo.action'
    # url = 'https://cart.jd.com/gotoOrder.action'
    payload = {
        'rid': str(int(time.time() * 1000)),
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Referer": "https://cart.jd.com/cart.action",
        "Connection": "keep-alive",
        'Host': 'trade.jd.com',
    }
    try:
        resp = session.get(url=url, params=payload, headers=headers)
        if not response_status(resp):
            logger.error('获取订单结算页信息失败')
            return ''

        soup = BeautifulSoup(resp.text, "html.parser")
        risk_control = get_tag_value(soup.select('input#riskControl'), 'value')

        order_detail = {
            'address': soup.find('span', id='sendAddr').text[5:],  # remove '寄送至： ' from the begin
            'receiver': soup.find('span', id='sendMobile').text[4:],  # remove '收件人:' from the begin
            'total_price': soup.find('span', id='sumPayPriceId').text[1:],  # remove '￥' from the begin
            'items': []
        }

        logger.info("下单信息：%s", order_detail)
        return order_detail
    except requests.exceptions.RequestException as e:
        logger.error('订单结算页面获取异常：%s' % e)
    except Exception as e:
        logger.error('下单页面数据解析异常：%s', e)
    return risk_control


def submit_order(risk_control,sku_id):


    """提交订单

    重要：
    1.该方法只适用于普通商品的提交订单（即可以加入购物车，然后结算提交订单的商品）
    2.提交订单时，会对购物车中勾选✓的商品进行结算（如果勾选了多个商品，将会提交成一个订单）

    :return: True/False 订单提交结果
    """
    url = 'https://trade.jd.com/shopping/order/submitOrder.action'
    # js function of submit order is included in https://trade.jd.com/shopping/misc/js/order.js?r=2018070403091

    # overseaPurchaseCookies:
    # vendorRemarks: []
    # submitOrderParam.sopNotPutInvoice: false
    # submitOrderParam.trackID: TestTrackId
    # submitOrderParam.ignorePriceChange: 0
    # submitOrderParam.btSupport: 0
    # riskControl:
    # submitOrderParam.isBestCoupon: 1
    # submitOrderParam.jxj: 1
    # submitOrderParam.trackId:

    data = {
        'overseaPurchaseCookies': '',
        'vendorRemarks': '[]',
        'submitOrderParam.sopNotPutInvoice': 'false',
        'submitOrderParam.trackID': 'TestTrackId',
        'submitOrderParam.ignorePriceChange': '0',
        'submitOrderParam.btSupport': '0',
        'riskControl': risk_control,
        'submitOrderParam.isBestCoupon': 1,
        'submitOrderParam.jxj': 1,
        'submitOrderParam.trackId': '9643cbd55bbbe103eef18a213e069eb0',  # Todo: need to get trackId
        # 'submitOrderParam.eid': eid,
        # 'submitOrderParam.fp': fp,
        'submitOrderParam.needCheck': 1,
    }

    def encrypt_payment_pwd(payment_pwd):
        return ''.join(['u3' + x for x in payment_pwd])

    if len(payment_pwd) > 0:
        data['submitOrderParam.payPassword'] = encrypt_payment_pwd(payment_pwd)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Referer": "http://trade.jd.com/shopping/order/getOrderInfo.action",
        "Connection": "keep-alive",
        'Host': 'trade.jd.com',
    }
    for count in range(1, 2):
        logger.info('第[%s/%s]次尝试提交订单', count, 3)
        try:
            resp = session.post(url=url, data=data, headers=headers)
            resp_json = json.loads(resp.text)

            # 返回信息示例：
            # 下单失败
            # {'overSea': False, 'orderXml': None, 'cartXml': None, 'noStockSkuIds': '', 'reqInfo': None, 'hasJxj': False, 'addedServiceList': None, 'sign': None, 'pin': 'xxx', 'needCheckCode': False, 'success': False, 'resultCode': 60123, 'orderId': 0, 'submitSkuNum': 0, 'deductMoneyFlag': 0, 'goJumpOrderCenter': False, 'payInfo': None, 'scaleSkuInfoListVO': None, 'purchaseSkuInfoListVO': None, 'noSupportHomeServiceSkuList': None, 'msgMobile': None, 'addressVO': None, 'msgUuid': None, 'message': '请输入支付密码！'}
            # {'overSea': False, 'cartXml': None, 'noStockSkuIds': '', 'reqInfo': None, 'hasJxj': False, 'addedServiceList': None, 'orderXml': None, 'sign': None, 'pin': 'xxx', 'needCheckCode': False, 'success': False, 'resultCode': 60017, 'orderId': 0, 'submitSkuNum': 0, 'deductMoneyFlag': 0, 'goJumpOrderCenter': False, 'payInfo': None, 'scaleSkuInfoListVO': None, 'purchaseSkuInfoListVO': None, 'noSupportHomeServiceSkuList': None, 'msgMobile': None, 'addressVO': None, 'msgUuid': None, 'message': '您多次提交过快，请稍后再试'}
            # {'overSea': False, 'orderXml': None, 'cartXml': None, 'noStockSkuIds': '', 'reqInfo': None, 'hasJxj': False, 'addedServiceList': None, 'sign': None, 'pin': 'xxx', 'needCheckCode': False, 'success': False, 'resultCode': 60077, 'orderId': 0, 'submitSkuNum': 0, 'deductMoneyFlag': 0, 'goJumpOrderCenter': False, 'payInfo': None, 'scaleSkuInfoListVO': None, 'purchaseSkuInfoListVO': None, 'noSupportHomeServiceSkuList': None, 'msgMobile': None, 'addressVO': None, 'msgUuid': None, 'message': '获取用户订单信息失败'}
            # {"cartXml":null,"noStockSkuIds":"xxx","reqInfo":null,"hasJxj":false,"addedServiceList":null,"overSea":false,"orderXml":null,"sign":null,"pin":"xxx","needCheckCode":false,"success":false,"resultCode":600157,"orderId":0,"submitSkuNum":0,"deductMoneyFlag":0,"goJumpOrderCenter":false,"payInfo":null,"scaleSkuInfoListVO":null,"purchaseSkuInfoListVO":null,"noSupportHomeServiceSkuList":null,"msgMobile":null,"addressVO":{"pin":"xxx","areaName":"","provinceId":xx,"cityId":xx,"countyId":xx,"townId":xx,"paymentId":0,"selected":false,"addressDetail":"xx","mobile":"xx","idCard":"","phone":null,"email":null,"selfPickMobile":null,"selfPickPhone":null,"provinceName":null,"cityName":null,"countyName":null,"townName":null,"giftSenderConsigneeName":null,"giftSenderConsigneeMobile":null,"gcLat":0.0,"gcLng":0.0,"coord_type":0,"longitude":0.0,"latitude":0.0,"selfPickOptimize":0,"consigneeId":0,"selectedAddressType":0,"siteType":0,"helpMessage":null,"tipInfo":null,"cabinetAvailable":true,"limitKeyword":0,"specialRemark":null,"siteProvinceId":0,"siteCityId":0,"siteCountyId":0,"siteTownId":0,"skuSupported":false,"addressSupported":0,"isCod":0,"consigneeName":null,"pickVOname":null,"shipmentType":0,"retTag":0,"tagSource":0,"userDefinedTag":null,"newProvinceId":0,"newCityId":0,"newCountyId":0,"newTownId":0,"newProvinceName":null,"newCityName":null,"newCountyName":null,"newTownName":null,"checkLevel":0,"optimizePickID":0,"pickType":0,"dataSign":0,"overseas":0,"areaCode":null,"nameCode":null,"appSelfPickAddress":0,"associatePickId":0,"associateAddressId":0,"appId":null,"encryptText":null,"certNum":null,"used":false,"oldAddress":false,"mapping":false,"addressType":0,"fullAddress":"xxxx","postCode":null,"addressDefault":false,"addressName":null,"selfPickAddressShuntFlag":0,"pickId":0,"pickName":null,"pickVOselected":false,"mapUrl":null,"branchId":0,"canSelected":false,"address":null,"name":"xxx","message":null,"id":0},"msgUuid":null,"message":"xxxxxx商品无货"}
            # {'orderXml': None, 'overSea': False, 'noStockSkuIds': 'xxx', 'reqInfo': None, 'hasJxj': False, 'addedServiceList': None, 'cartXml': None, 'sign': None, 'pin': 'xxx', 'needCheckCode': False, 'success': False, 'resultCode': 600158, 'orderId': 0, 'submitSkuNum': 0, 'deductMoneyFlag': 0, 'goJumpOrderCenter': False, 'payInfo': None, 'scaleSkuInfoListVO': None, 'purchaseSkuInfoListVO': None, 'noSupportHomeServiceSkuList': None, 'msgMobile': None, 'addressVO': {'oldAddress': False, 'mapping': False, 'pin': 'xxx', 'areaName': '', 'provinceId': xx, 'cityId': xx, 'countyId': xx, 'townId': xx, 'paymentId': 0, 'selected': False, 'addressDetail': 'xxxx', 'mobile': 'xxxx', 'idCard': '', 'phone': None, 'email': None, 'selfPickMobile': None, 'selfPickPhone': None, 'provinceName': None, 'cityName': None, 'countyName': None, 'townName': None, 'giftSenderConsigneeName': None, 'giftSenderConsigneeMobile': None, 'gcLat': 0.0, 'gcLng': 0.0, 'coord_type': 0, 'longitude': 0.0, 'latitude': 0.0, 'selfPickOptimize': 0, 'consigneeId': 0, 'selectedAddressType': 0, 'newCityName': None, 'newCountyName': None, 'newTownName': None, 'checkLevel': 0, 'optimizePickID': 0, 'pickType': 0, 'dataSign': 0, 'overseas': 0, 'areaCode': None, 'nameCode': None, 'appSelfPickAddress': 0, 'associatePickId': 0, 'associateAddressId': 0, 'appId': None, 'encryptText': None, 'certNum': None, 'addressType': 0, 'fullAddress': 'xxxx', 'postCode': None, 'addressDefault': False, 'addressName': None, 'selfPickAddressShuntFlag': 0, 'pickId': 0, 'pickName': None, 'pickVOselected': False, 'mapUrl': None, 'branchId': 0, 'canSelected': False, 'siteType': 0, 'helpMessage': None, 'tipInfo': None, 'cabinetAvailable': True, 'limitKeyword': 0, 'specialRemark': None, 'siteProvinceId': 0, 'siteCityId': 0, 'siteCountyId': 0, 'siteTownId': 0, 'skuSupported': False, 'addressSupported': 0, 'isCod': 0, 'consigneeName': None, 'pickVOname': None, 'shipmentType': 0, 'retTag': 0, 'tagSource': 0, 'userDefinedTag': None, 'newProvinceId': 0, 'newCityId': 0, 'newCountyId': 0, 'newTownId': 0, 'newProvinceName': None, 'used': False, 'address': None, 'name': 'xx', 'message': None, 'id': 0}, 'msgUuid': None, 'message': 'xxxxxx商品无货'}
            # {"orderXml":null,"cartXml":null,"noStockSkuIds":"","reqInfo":null,"hasJxj":false,"overSea":false,"addedServiceList":null,"sign":null,"pin":null,"needCheckCode":true,"success":false,"resultCode":0,"orderId":0,"submitSkuNum":0,"deductMoneyFlag":0,"goJumpOrderCenter":false,"payInfo":null,"scaleSkuInfoListVO":null,"purchaseSkuInfoListVO":null,"noSupportHomeServiceSkuList":null,"msgMobile":null,"addressVO":null,"msgUuid":null,"message":"验证码不正确，请重新填写"}
            # 下单成功
            # {'overSea': False, 'orderXml': None, 'cartXml': None, 'noStockSkuIds': '', 'reqInfo': None, 'hasJxj': False, 'addedServiceList': None, 'sign': None, 'pin': 'xxx', 'needCheckCode': False, 'success': True, 'resultCode': 0, 'orderId': 8740xxxxx, 'submitSkuNum': 1, 'deductMoneyFlag': 0, 'goJumpOrderCenter': False, 'payInfo': None, 'scaleSkuInfoListVO': None, 'purchaseSkuInfoListVO': None, 'noSupportHomeServiceSkuList': None, 'msgMobile': None, 'addressVO': None, 'msgUuid': None, 'message': None}

            if resp_json.get('success'):
                logger.info('订单提交成功! 订单号：%s', resp_json.get('orderId'))
                return True
            else:
                resultMessage, result_code = resp_json.get('message'), resp_json.get('resultCode')
                if result_code == 0:
                    # self._save_invoice()
                    if '验证码不正确'in resultMessage:
                        resultMessage = resultMessage + '(验证码错误)'
                    else:
                        resultMessage = resultMessage + '(下单商品可能为第三方商品，将切换为普通发票进行尝试)'
                elif result_code == 60077:
                    resultMessage = resultMessage + '(可能是购物车为空 或 未勾选购物车中商品)'
                elif result_code == 60123:
                    resultMessage = resultMessage + '(需要在payment_pwd参数配置支付密码)'
                for i in urls:
                    if sku_id in i:
                        urls.remove(i)
                logger.info('订单提交失败,避免死循环去除异常id[%s]',sku_id)
                logger.info('订单提交失败, 错误码：%s, 返回信息：%s', result_code, resultMessage)
                logger.info(resp_json)
                return False
        except Exception as e:
            print(traceback.format_exc())
            continue


'''

'''


def item_removed(sku_id):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Referer": "http://trade.jd.com/shopping/order/getOrderInfo.action",
        "Connection": "keep-alive",
        'Host': 'item.jd.com',
    }
    url = 'https://item.jd.com/{}.html'.format(sku_id)
    page = requests.get(url=url, headers=headers)
    return '该商品已下柜' not in page.text


'''
购买环节
测试三次
'''


def buyMask(sku_id):
    cancel_select_all_cart_item()
    cart = cart_detail()
    if sku_id in cart:
        logger.info('%s 已在购物车中，调整数量为 %s', sku_id, 1)
        cart_item = cart.get(sku_id)
        change_item_num_in_cart(
            sku_id=sku_id,
            vender_id=cart_item.get('vender_id'),
            num=1,
            p_type=cart_item.get('p_type'),
            target_id=cart_item.get('target_id'),
            promo_id=cart_item.get('promo_id')
        )
    else:
        add_item_to_cart(sku_id)
    risk_control = get_checkout_page_detail()
    if len(risk_control) > 0:
        if submit_order(risk_control,sku_id):
            return True
    return False


flag = 1
while (1):
    try:
        if flag == 1:
            validate_cookies()
            getUsername()
        checkSession = requests.Session()
        checkSession.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Connection": "keep-alive"
        }
        logger.info('第' + str(flag) + '次 ')
        flag += 1
        for i in urls:
            # 商品url
            skuId = i.split('skuId=')[1].split('&')[0]
            skuidUrl = 'https://item.jd.com/' + skuId + '.html'
            response = checkSession.get(i)
            if (response.text.find('无货') > 0):
                logger.info('[%s]类型口罩无货', skuId)
            else:
                if item_removed(skuId):
                    logger.info('[%s]类型口罩有货啦!马上下单', skuId)
                    if buyMask(skuId):
                        message.send(skuidUrl, False)
                        sys.exit(1)
                    else:
                        message.send(skuidUrl, False)
                else:
                    logger.info('[%s]类型口罩有货，但已下柜商品', skuId)
        timesleep = random.randint(3, 8)
        time.sleep(timesleep)
        if flag % 20 == 0:
            logger.info('校验是否还在登录')
            validate_cookies()
    except Exception as e:

        print(traceback.format_exc())
        time.sleep(10)
