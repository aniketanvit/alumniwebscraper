#   Aniket Anvit
#   aniket.anvit@rutgers.edu

try:
    import requests
except ImportError:
    raise ImportError("requests package missing...")

try:
    from lxml import html
except ImportError:
    raise ImportError("lxml package missing...")


class WebRequestHandler(object):

    """
    This class handles the http requests made to the search engine
    """

    def __init__(self, url, randomizer, link_xpath):
        self.baseUrl = url
        self.request_randomizer = randomizer
        self._link_xpath = link_xpath
        self.MAXLINKS = 10


    def get_top10_links(self, alumni):
        request_url = self.baseUrl + str(alumni).replace(' ', '%20')
        response = requests.get(request_url, self._get_random_request_header())
        if (int(response.status_code) != 200):
            raise IOError("Search Engine did not return valid result for the request...") #NetworkError (??)
        tree = html.fromstring(response.content)
        redirect_links = tree.xpath (self._link_xpath)
        valid_links = self._get_valid_links_from_redirect_links(redirect_links)
        alumni_links = []
        for link in valid_links:
            alumni_links.append([alumni, link])
        return alumni_links

    def _get_random_request_header(self):
        header_dictionary = {}
        header_dictionary['user-agent'] = self.request_randomizer.get_random_user_agent()
        header_dictionary['accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        #header_dictionary['set-cookie'] = 'SIDCC=AE4kn7_jK2wkHhmLhIHQbDXqRb0ngLP7UwODVJyeFz30wtDCTkNXL4OHcO85DqdyNtUK4EryKHuJfoEZHgfvPA; expires=Fri, 08-Dec-2017 21:09:47 GMT; path=/; domain=.google.com; priority=high'
        return header_dictionary

    def _get_valid_links_from_redirect_links(self, redirect_links):
        """
        This method is a temporary hack until I find something better
        :param redirect_links:
        :return:
        """
        prefix = '/url?q='
        postfix = '&'
        valid_links = []
        for index in range(0, min(self.MAXLINKS, len(redirect_links)), 1):
            rlink = str(redirect_links[index])
            if (prefix in rlink):
                strt = rlink.index(prefix)
                if (postfix in rlink):
                    end = rlink.index (postfix)
                    valid_links.append(rlink[strt + 7:end])
                else:
                    valid_links.append(rlink[strt + 7:])
        return valid_links