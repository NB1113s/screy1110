import urllib.request
from bs4 import BeautifulSoup
import json
import requests

url = "http://gigazine.net/"

def rank(word):
	if word=="人気記事":
		html = urllib.request.urlopen(url)
		soup = BeautifulSoup(html, "html.parser")

		# gigazineサイトの常に最新記事のurlを取り出す
		geturl = soup.find('div', attrs={'id': 'section'}).h2.a.get("href")
				
		# 最新記事を開き、人気記事一覧を取得
		url2= geturl
		html2 = urllib.request.urlopen(url2)
		soup2 = BeautifulSoup(html2, "lxml")

		list=[]
		#記事ページ内にある人気記事を表示している部分を探す
		rank = soup2.find('div',id='ranking-entry')
		#人気記事一覧の中のa要素を取得
		rankli=rank.find_all('a')

		for ui in rankli:
			#人気記事のリンクを取得getu　タイトルを取得gett
			getu=ui.get("href")
			gett = ui.text
		
			#人気記事のリンク先でトップ画像を取得getimg 
			url3= url[:-1]+getu
			html3 = urllib.request.urlopen(url3)
			soup3 = BeautifulSoup(html3, "lxml")
			getcnt = soup3.find('div',{'class':'cntimage'})
			getimg = getcnt.find('img').get('src')
			
			#リストに記事タイトル、url、画像urlを格納
			list.append([gett,url3,getimg])

	# for i in range(ranklist):
	# 	for i in range(0,int(len(result))):
	# 		print(result[i][0],result[i][1],"\n")
	# list=[str(i) for i in list]
	# result = '\n'.join(list)
	return list

# result=rank("人気記事")
# for arr in result:
# 	print(arr[1])
# 	print(result[arr][2],"\n")