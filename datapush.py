import json
import requests
from requests_html import HTMLSession 
from bs4 import BeautifulSoup as bs # importing BeautifulSoup
session = HTMLSession()
with open('users.json', 'r+') as f:
    temp=json.load(f)
    list2 = temp['entries']
    for i in list2:
        if "https://www.youtube.com/" in i['url']:
            video_url = i['url']
            # get the html content
            response = session.get(video_url)
            # execute Java-script
            response.html.render(sleep=1)
            # # create bs object to parse HTML
            soup = bs(response.html.html, "html.parser")
            youtube_time=soup.find("meta", itemprop="datePublished")["content"]
            description=soup.find("meta", itemprop="description")["content"]
            i['youtube_time']=youtube_time
            i['body']=description
    temp['entries']=list2
    f.seek(0)
    json.dump(temp, f, indent=2)
    f.truncate()
with open('users.json', 'r+') as f:
    data = json.load(f)
with open('users.json', 'r+') as f:
    # data = json.load(f)
    json_object = json.load(f)
    list1 = json_object['entries']
    list1.clear()
    json_object["entries"] = list1
    f.seek(0)
    json.dump(json_object, f, indent=2) 
    f.truncate()
session.close()
headers={"Bearer":"token"}
r = requests.post("https://xurge-coming.bubbleapps.io/version-test/api/1.1/wf/entries/?start_id=11111111&end_id=22222222",headers=headers,json=data)
print(r.status_code, r.reason)
