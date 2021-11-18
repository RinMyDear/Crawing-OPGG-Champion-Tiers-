import requests
from bs4 import BeautifulSoup
def download():
    htmls=[]
    url=f'https://br.op.gg/champion/statistics'
    print("craw html:", url)
    r = requests.get(url,
                        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"})
    if r.status_code != 200:
        raise Exception("error")
    htmls.append(r.text)
    return htmls
data=download()
champion=[]
def single(html):
    soup=BeautifulSoup(html,'html.parser')
    items=soup.find_all(class_='tabItem champion-trend-tier-ADC')
    for item in items:
        itemname=item.find_all(class_='champion-index-table__name')
        for name in itemname:
            champion.append(name.string)
tiers=[]
def tier(html):
    soup=BeautifulSoup(html,'html.parser')
    items=soup.find_all(class_='tabItem champion-trend-tier-ADC')
    for item in items:
        value=item.find_all(class_="champion-index-table__cell champion-index-table__cell--value")
        for i in value:
            num=i.find('img')
            if num==None:
                pass
            else:
                for tag in i:
                    tag=str(tag)
                    for j in tag:
                        if j.isdigit():
                            tiers.append(j)                   
tier(data[0])
single(data[0])
all={}
for i in range(0,len(champion)):
    all[champion[i]]=tiers[i]
print(all)