import time
import aojtools
import requests
import logging
from scriper import AOJSolutionScriper
class SolutionCrawler:
    def __init__(self, handler):
        self.handler = handler
        self.logger = logging
        self.logger.basicConfig(filename='crawler.log', level=logging.INFO)

    def problems(self):
        """return list of (problem_id, url)"""
        raise NotImplementedError

    def scripe(self, url):
        """parse the page and return list of (user_id, lang, solution)"""
        raise NotImplementedError

    def handle(self, pid, uid, lang, solution):
        """handle given (problem_id, user_id, language, solution)"""
        self.handler(pid, uid, lang, solution)

    def crawle(self):
        for pid, url in self.problems():
            self.logger.info("{} scriping problem_id={} ...".format(self.__class__, pid))
            for uid, lang, solution in self.scripe(url):
                self.handle(pid, uid, lang, solution)

class AOJSolutionCrawler(SolutionCrawler):
    def problems(self):
        volumes = [0, 1, 2, 3, 5, 6, 10, 11, 12, 13, 15, 20, 21, 22, 23, 24, 25, 26]
        url_base = "http://judge.u-aizu.ac.jp/onlinejudge/solution.jsp?pid="
        res = []
        for v in volumes:
            problems = aojtools.api.ProblemListSearchAPI(v).problem
            for p in problems:
                pid = p.id
                res.append((pid, url_base+pid))
        return res

    def scripe(self, url):
        sc = AOJSolutionScriper()
        r = requests.get(url)
        return sc.scripe(r.text)
