from urllib import request
import random
import json
import time
from urllib import error
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import mysql.connector
#User_Agent池
ua=UserAgent()

#ip池
ips=["122.72.18.34:80","61.160.208.222:8080","120.27.131.204:3128","202.38.92.100:3128"]
with open('/home/lenovo/桌面/HackthonPro/movieid.json','r') as f:
    movieIds=json.loads(f.read())
    conn = mysql.connector.connect(user='root', password='pqc19960320',
                                       database='Hackerthon', host="120.77.220.239", port=32777)
    #游标
    cursor = conn.cursor()
    print("游标建立")
    count=0
    for movieid in movieIds:
        for i in range(0,101,20):
            proxy=request.ProxyHandler({'http':random.choice(ips)})
            url="https://movie.douban.com/subject/"+str(movieid)+"/comments?start="+str(i)+"&limit=20&sort=new_score&status=P"
            opener=request.build_opener(proxy,request.ProxyHandler)
            opener.addheaders=[('User-Agent',ua.random)]
            print(">>>>>>>>>>>>>>>>>.")
            data=opener.open(url).read().decode()
            print("<<<<<<<<<<<<<<<<<<<<<")
            print(data[8:90])
            #匹配并且存入数据库
            soup = BeautifulSoup(data, 'html.parser')
            results = soup.find_all("p", attrs={"class": ""}, recursive=True)
            for index, vaule in enumerate(results[0:-6]):
                content=vaule.get_text().strip()
                print(content)
                try:
                    cursor.execute("insert into allcomment (content,movieid) values('%s',%d)" % ( content,int(movieid)))
                except mysql.connector.errors.DatabaseError:
                    time.sleep(3)
                time.sleep(0.2)
                print(count)
                count+=1
    # cursor.commit()
    # conn.close()
    conn.commit()
    cursor.close()
# import mysql.connector
# conn = mysql.connector.connect(user='root', password='pqc19960320',
#                                        database='Hackerthon', host="120.77.220.239", port=32777)
#     #游标
# cursor = conn.cursor()
# cursor.execute("insert into allcomment (content,movieid) values('%s',%d)" % ("哈哈", int(1)))
# conn.commit()
# cursor.close()