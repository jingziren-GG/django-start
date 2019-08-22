# -*- coding:utf-8 -*-
import requests
import random
from bs4 import BeautifulSoup
import pymssql
import os



def get_data():
    headers = Ua_headers()
    response = requests.get('https://nba.hupu.com/standings',headers=headers,verify=False)
    return response.text


def Ua_headers():
    user_agent_list = [
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',]
    user_agent = random.choice(user_agent_list)
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    headers['user_agent'] = user_agent
    return headers




def Analyze_data(data):
    soup = BeautifulSoup(data,'html.parser')
    datas = soup.find('tbody')
    datas_tr = datas.find_all('tr')
    conn = pymssql.connect("DESKTOP-SCIMUGR", "sa", "zxc1230.", "NBA")
    cursor = conn.cursor()
    cursor.execute('truncate table index_nbadata')
    for tr in datas_tr:
        print(tr)
        td = tr.find_all("td")
        if len(td) == 1:
            area = td[0].text
        else:
            da1 = td[0].text # 排名
            da2 = td[1].text # 队名
            da3 = td[2].text # 胜场
            da4 = td[3].text # 败场
            da5 = td[4].text # 胜率
            try:
                img_url = td[1].find("a")['href']
                get_img(img_url,td[1].text)
                img = "/static/images/"+ da2 + '.png' # os.getcwd() + "\\NBA\\
            except TypeError:
                pass
            try:
                cursor.execute("insert into index_nbadata values('%d','%s','%d','%d','%s','%s','%s')"%(
                    int(da1),da2,int(da3),int(da4),da5,img,area
                ))
            except ValueError:
                pass
            conn.commit()


def get_img(url,name):
    path = os.getcwd() + '\\NBA_web\\index\\static\\images\\'
    print(path)
    headers = Ua_headers()
    response = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(response.text,'lxml')
    img = soup.find('div',{'class':'img'})
    img_url = img.find("img")['src']
    pon = requests.get(img_url)
    with open(path+name+'.png','ab+') as im:
        im.write(pon.content)
        im.close()
    print('保存图片成功')



if __name__ == "__main__":
    pon = get_data()
    Analyze_data(pon)
    # url = 'https://nba.hupu.com/teams/raptors'
    # get_img(url,'雄鹿')