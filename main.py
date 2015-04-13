from crawler import AOJSolutionCrawler

def handle(problem, user, language, solution):
    print("{} solved {} by {}".format(user, problem, language))
    print("solution:\n{}\n".format(solution))

def example1():
    crawler = AOJSolutionCrawler(handle)
    crawler.crawle_all()

def example2():
    crawler = AOJSolutionCrawler(handle)
    problems = ['2607', '2608']
    crawler.crawle(problems)

if __name__ == '__main__':
    example2()

