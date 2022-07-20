import requests
from bs4 import BeautifulSoup
import math

def extract_brand_info():
  result = requests.get("http://www.alba.co.kr/")
  soup = BeautifulSoup(result.text, 'html.parser')
  searchBrandInfo = soup.find("div", id="MainSuperBrand").find_all("a",{"class": "brandHover"})
  brand_list=[]
  url_list=[]
  for info in searchBrandInfo:
    brand_list.append(info.find("strong").text.replace("/",""))
    url_list.append(info["href"])
  return {'brand': brand_list, 'url': url_list}
  

def extract_job(result):
  place = result.find("td",{"class":"local first"})
  if place is not None:
    place = place.text
  else: 
    place = None
  title = result.find("span",{"class":"company"})
  if title is not None:
    title = title.text
  else:
    title = None
  time = result.find("td",{"class":"data"}).text
  pay = result.find("td",{"class":"pay"}).text
  date = result.find("td",{"class":"regDate"}).text
  return {'place':place,
            'title':title,
            'time':time,
            'pay':pay,
            'date':date}

def extract_max_page(url):
  result = requests.get(url)
  soup = BeautifulSoup(result.text, 'html.parser')
  jobCount = int(soup.find("p",{"class":"jobCount"}).find("strong").text.replace(",",""))
  return math.ceil(jobCount/50)
  
def extract_jobs(url):
  jobs=[]
  max_page = extract_max_page(url)

  for page in range(max_page):
    pageUrl = url+f"job/brand/main.asp?page={page+1}&pagesize=50"
    result = requests.get(pageUrl)
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find("tbody").find_all("tr",{"class":""})
  
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs

    