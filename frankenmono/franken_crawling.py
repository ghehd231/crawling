import requests
from bs4 import BeautifulSoup

def getList(page):
    print(page)
    response = requests.get("http://www.frankenmono.com/product/shop_list.asp?page="+page+"&top_val=store&shop_chk=ALL&search_value=&shop_chk2=")
    result = response.text

    soup = BeautifulSoup(result, "html.parser")

    result2 = soup.select('.item > a:nth-child(1)')

    for a in result2:
        getDetail(a.get('href'))

    page_plus = int(page)+1

    if len(result2) > 0:
        getList(str(page_plus))
    else:
        print('-------end Crawlling-------')


# end getList()

def getDetail(href):
    res = requests.get('http://www.frankenmono.com'+href)
    result = res.text

    soup = BeautifulSoup(result, "html.parser")
    #상품 정보 table 전체 가져오기
    table = soup.select('#detail_right > div > table tr')

    #--------코드 가져오기----------
    #
    # code = table[1].text
    # #strip() => str 변수의 모든 공백 제거
    # code = code.strip()
    #
    # #code 기준으로 잘라서 리스트로 반환
    # code = code.split('code')
    #
    # #split 으로 잘라온 후 code[~]으로 불러올때의 타입은 str이다
    # code = code[1].strip()
    # print(code)

    # #--------이미지 가져오기------------
    image = soup.select('#detail_left img')
    first_image = image[0].get('src')
    print(first_image)

# end getDetail

getList('1')