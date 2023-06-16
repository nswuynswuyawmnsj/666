import xml.etree.ElementTree as ET
import feedparser
import requests
from bs4 import BeautifulSoup
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.html import HtmlParser
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


# 指定 OPML 文件路径
opml_file ='C:/Users/David/1.opml'

# 解析 OPML 文件
tree = ET.parse(opml_file)
root = tree.getroot()

# 遍历 OPML 文件中的所有链接
for outline in root.iter('outline'):
    # 检查链接是否包含 RSS 订阅源
    if outline.get('type') == 'rss':
        # 获取链接的 URL
        rss_url = outline.get('xmlUrl')

        # 使用 FeedParser 库解析 RSS 订阅源
        feed = feedparser.parse(rss_url)

        # 遍历订阅源中的每篇文章，提取摘要并输出
        for entry in feed.entries:
            # 获取文章链接
            link = entry.link

            # 使用 requests 库获取文章 HTML
            response = requests.get(link)
            html = response.content

            # 使用 BeautifulSoup 库解析 HTML
            soup = BeautifulSoup(html, 'html.parser')

            # 提取文章标题
            title = soup.find('title').text

            # 提取文章正文
            article = ''
            for p in soup.find_all('p'):
                article += p.text.strip()

            # 使用 Sumy 库生成摘要
            LANGUAGE = 'english'
            SENTENCES_COUNT = 3

    