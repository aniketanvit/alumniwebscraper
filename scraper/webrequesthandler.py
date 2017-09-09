#   Aniket Anvit
#   aniket.anvit@rutgers.edu

try:
    import requests
except ImportError:
    raise ImportError("requests package missing...")

try:
    import BeautifulSoup
except ImportError:
    raise ImportError("BeautifulSoup package missing...")


class WebRequestHandler(object):

    """
    This class handles the http requests made to the search engine
    """

    def __init__(self, url, randomizer, urlTag = None):
        self.baseUrl = url
        self.request_randomizer = randomizer
        if(urlTag is None):
            self._urlTag = 'cite'
        else:
            self._urlTag = urlTag

    def get_first10_search_results(self, alumni):
        request_url = self.baseUrl + str(alumni).replace(' ', '%20')
        response = requests.get(request_url, self._get_random_request_header())
        if (int(response.status_code) != 200):
            raise IOError("Search Engine did not return valid result for the request...") #NetworkError (??)
        bs = BeautifulSoup
        soup = bs.BeautifulSoup(response.text)
        soup_links = soup.findAll(self._urlTag)
        alumni_links = []
        alumni_links.append(alumni)
        for link in soup_links:
            alumni_links.append(link.text)
        return alumni_links

    def _get_random_request_header(self):
        header_dictionary = {}
        header_dictionary['User-Agent'] = self.request_randomizer.get_random_user_agent()
        return header_dictionary