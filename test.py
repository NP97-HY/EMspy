import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re
from spyForEastMoney.Sentiment.test import Test 


if __name__ == "__main__":
    # headers = {
    #     "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0"
    #     }
    # url = "https://guba.eastmoney.com/news,000999,956162338.html"
    # res = urllib.request.Request(url=url,headers=headers)
    # reponse = urllib.request.urlopen(res)
    # html = reponse.read().decode("utf-8")
    # bs = BeautifulSoup(html,"html.parser")
    # rule = re.compile(r'(ttbt">(.*?)</div>)',re.S)
    # rule2 = re.compile(r'(body">(.*?)</div>)',re.S)
    # op = open("spyForEastMoney/data_homepage/eastmoney{}.txt".format(2),"w")
    # print(type(bs.find_all('div',id="post_content")))
    # for tit in bs.find_all('div',id="post_content"):#(.*?)xeditor(.*?)
    #     tit = str(tit)
    #     #print("tit=",tit)
    #     list1 = re.findall(rule,tit)
    #     str1 = str(list1[0]).split(",")
    #     list2 = re.findall(rule2,tit)
    #     str2 = str(list2[0]).split(",")
    #     str2 = str2[1].split(">")
    #     op.write(str(str1[1].replace("\\n","").replace("\\r","").replace(" ","")+str2[1].replace("\\n","").replace("\\r","").replace(" ","")))
    # op.close()