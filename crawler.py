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

    def problem_url(self, pid):
        """return url of the problem pid"""
        raise NotImplementedError

    def problems(self):
        """generate all problem_ids"""
        raise NotImplementedError

    def scripe(self, url):
        """parse the page and generate (user_id, lang, solution)s"""
        raise NotImplementedError

    def handle(self, pid, uid, lang, solution):
        """handle given (problem_id, user_id, language, solution)"""
        self.handler(pid, uid, lang, solution)

    def crawle(self, problems):
        for pid in problems:
            url = self.problem_url(pid)
            self.logger.info("{} scriping problem_id={} ...".format(self.__class__, pid))
            for uid, lang, solution in self.scripe(url):
                self.handle(pid, uid, lang, solution)

    def crawle_all(self):
        self.crawle(self.problems())


class AOJSolutionCrawler(SolutionCrawler):
    def problem_url(self, pid):
        url_base = "http://judge.u-aizu.ac.jp/onlinejudge/solution.jsp?pid="
        return url_base + pid

    def problems(self):
        volumes = [0, 1, 2, 3, 5, 6, 10, 11, 12, 13, 15, 20, 21, 22, 23, 24, 25, 26]
        for v in volumes:
            problems = aojtools.api.ProblemListSearchAPI(v).problem
            for p in problems:
                pid = p.id
                yield pid

    def scripe(self, url):
        sc = AOJSolutionScriper()
        r = requests.get(url)
        return sc.scripe(r.text)
