# AOJ-Solution-Crawler
Correcting solutions of the problems in Aizu online judge

## usage
```
from crawler import AOJSolutionCrawler

def handle(problem, user, language, solution):
    print("{} solved {} by {}".format(user, problem, language))
    print("solution:\n{}\n".format(solution))

crawler = AOJSolutionCrawler(handle)
crawler.crawle()
```
