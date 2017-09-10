#   Aniket Anvit
#   aniket.anvit@rutgers.edu

import sys
import webscraper
import webrequesthandler
import webrequestrandomizer

def main(args):
    GOOGLE = 'http://www.google.com/search?q='
    alumni_scraper = webscraper.WebScraper(
        webrequesthandler.WebRequestHandler(
            GOOGLE,
            webrequestrandomizer.WebRequestRandomizer(),
            '//h3/a/@href'
        )
    )
    alumni_scraper.scrape(args[1])

if __name__ == '__main__':
    main(sys.argv)