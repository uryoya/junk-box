import lxml.html
import requests

target_url = 'http://seesaawiki.jp/w/qvarie/d/%A5%E6%A5%CB%A5%B3%A1%BC%A5%C96.0%B0%CA%B9%DF%A4%C7%BB%C8%CD%D1%A4%C7%A4%AD%A4%EB%B3%A8%CA%B8%BB%FA%28%B4%E9%CA%D4%29'
target_html = requests.get(target_url).text
root = lxml.html.fromstring(target_html)

contents = []
for n in range(1, 44):
    contents += root.cssselect('h4#content_1_{}'.format(n))

#contents = root.cssselect('h4#content_1_2')
#for content in contents:
#    print(content.text)

for content in contents:
    print(content.text_content())
