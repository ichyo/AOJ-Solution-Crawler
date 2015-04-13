from crawler import AOJSolutionCrawler

def main():
    def handle(problem, user, language, solution):
        print("{} solved {} by {}".format(user, problem, language))
        print("solution:\n{}\n".format(solution))

    crawler = AOJSolutionCrawler(handle)
    crawler.crawle()

if __name__ == '__main__':
    main()

