from crawler import AOJSolutionCrawler

def main():
    def handle(pid, uid, lang, sol):
        print("{} {} {} {}".format(pid, uid, lang, sol))
    a = AOJSolutionCrawler(handle)
    a.crawle()

if __name__ == '__main__':
    main()

