from bs4 import BeautifulSoup
import requests
import re


def check_footer(tag):
    classes = tag.get('class')
    if not classes:
        return False 
    for item in classes: 
        if re.search('footer', item, re.I):
            return True
    return False



def get_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }

    response = requests.get(url,headers=headers)
    if response.status_code != 200:
        return "ERROR!!!"
    soup = BeautifulSoup(response.text,'html.parser')
    title = url[url.rfind('/')+1:]

    if soup.body:
        for tag in soup.body.find_all():
            if tag.name in ['nav','img','input','style','footer','sup']:
                tag.decompose()
            if tag.name == 'div':
                if check_footer(tag):
                    tag.decompose()
        text = soup.body.get_text(separator='\n', strip=True)
    else:
        text = ""
        
    return (title + '\n\n' + text)


