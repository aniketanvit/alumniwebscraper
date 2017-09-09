#   Aniket Anvit
#   aniket.anvit@rutgers.edu

import sys
import webscraper
import webrequesthandler
import webrequestrandomizer

def main(args):
    GOOGLE = 'http://www.google.com/search?q='
    alumniScraper = webscraper.WebScraper(
        webrequesthandler.WebRequestHandler(
            GOOGLE,
            webrequestrandomizer.WebRequestRandomizer()
        )
    )
    alumniScraper.scrape(args[1])

if __name__ == '__main__':
    main(sys.argv)