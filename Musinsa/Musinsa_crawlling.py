import requests
from bs4 import BeautifulSoup

def getList(page):
    print(page)
    # method to insert numbers into strings: {page}
    response = requests.get("https://store.musinsa.com/app/contents/bestranking/?d_cat_cd=&u_cat_cd=001&range=nw&price=&ex_soldout=&sale_goods=&new_product_yn=&list_kind=&page={page}&display_cnt=80&sex=&popup=&sale_rate=&price1=&price2=&chk_new_product_yn=&chk_sale=&chk_soldout=")
    result = response.text
    soup = BeautifulSoup(result, "html.parser")

    list = soup.select('#catelist > div:nth-child(2) > dl > dd > ul > li > a')
    for a in list:
        obj = a.get('onclick')
        obj = obj.split(';')
        obj = obj[0]
        obj = obj.split(',')
        obj = obj[2].replace("'","")
        print(obj.strip())
        getTop20(obj)

    # response2 = requests.get('https://static.msscdn.net/mfile_outsrc/js/common/common.js?20181114')
    # result2 = response2.text
    # soup2 = BeautifulSoup(result2, "html.parser")
    # print(soup2.find_all())
    # page_plus = int(page) + 1
    #
    # if len(result) > 0:
    #     getList(page_plus)

# end getList()

def getTop20(val):
    response2 = requests.get("https://store.musinsa.com/app/contents/bestranking/?d_cat_cd=&u_cat_cd{val}8&range=nw&price=&ex_soldout=&sale_goods=&new_product_yn=&list_kind=&page=1&display_cnt=80&sex=&popup=&sale_rate=&price1=&price2=")
    result2 = response2.text

    soup2 = BeautifulSoup(result2, "html.parser")

    goods = soup2.select('.list-box > ul > li >.li_inner')
    print(goods)


getList('1')