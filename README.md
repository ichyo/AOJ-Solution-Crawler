# AOJ-Solution-Crawler
Collecting solutions for problems in Aizu Online Judge

## usage
```python
from crawler import AOJSolutionCrawler

def handle(problem, user, language, solution):
    print("{} solved {} by {}".format(user, problem, language))
    print("solution:\n{}\n".format(solution))

crawler = AOJSolutionCrawler(handle)
crawler.crawle()
```
