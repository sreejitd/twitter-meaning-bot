from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request
req = urllib.request.Request(
    url="https://randomword.com/", 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
f = urllib.request.urlopen(req)
#print(f.read().decode('utf-8'))
soup = BeautifulSoup(f, 'lxml')
type(soup)
word=soup.find('div',{'id':'random_word'})
meaning=soup.find('div',{'id':'random_word_definition'})
text1=word.get_text()
text2=meaning.get_text()
print(text1)
print(text2)