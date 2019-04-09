# -*- coding: UTF-8 -*-
# 爬取图片

import urllib
import re

def get_html(url):
  page = urllib.urlopen(url)
  html = page.read()
  return html
# 通过html获取所有图片
def get_image(html_code):
  reg = r'src="(.+?\.jpg)" width'
  reg_img = re.compile(reg)
  img_list = reg_img.findall(html_code)
  x = 0
  for img in img_list:
    urllib.urlretrieve(img, '%s.jpg' %x)
    x += 1

print u'--------Image Crawler--------'
print u'please input a url: '
url = raw_input()
if url:
  pass
else:
  print u'---default url---'
  url = 'http://tieba.baidu.com/p/1753935195'
print u'crawl html...'
html_code = get_html(url)
print u'download images...'
get_image(html_code)
print u'done.'
raw_input('Press Enter to exit')

