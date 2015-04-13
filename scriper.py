import re
import requests
import scrapelib
import lxml.html
class AOJSolutionScriper:
    def __init__(self, requests_per_minute=20):
        self.requests = scrapelib.Scraper(requests_per_minute=requests_per_minute)

    def scripe(self, html):
        """scripe html at http://judge.u-aizu.ac.jp/onlinejudge/solution.jsp?pid=\d{4,4}"""
        res = []
        for url in self._reviews(html):
            r = self.requests.get(url)
            review = r.text
            uid, lang, sol = self._parse_review(review)
            yield (uid, lang, sol)

    def _reviews(self, html):
        url_base = "http://judge.u-aizu.ac.jp/onlinejudge/"
        pat = r'<a href="(review.jsp\?rid=\d{1,20}#1)">'
        r = re.compile(pat)
        return [url_base + m.group(1) for m in r.finditer(html)]
    
    def _parse_review(self, html):
        root = lxml.html.fromstring(html)
        # parse source of solution
        source = root.xpath('//div[@id="codeBody"]')[0]
        source_txt = lxml.html.tostring(source, method='text', encoding='utf-8').strip()

        # parse user id
        pat = r'<a href="user.jsp\?id=(.{1,30})">.{1,30}</a></p>'
        r = re.compile(pat)
        m = r.search(html)
        user_id = m.group(1)

        # parse language 
        lang = root.xpath('//table[@class="explore"]/tr/td')[1]
        lang_txt = lxml.html.tostring(lang, method='text', encoding='utf-8').strip()

        return (user_id, lang_txt, source_txt)

