#   Aniket Anvit
#   aniket.anvit@rutgers.edu

try:
    import csv
except ImportError:
    raise ImportError ("csv package missing...")

import os
import time
import random

class WebScraper(object):

    """
    This class handles all actions from csv file reading, searching, till csv file writing
    """

    def __init__(self, search_handler):
        self.search_handler = search_handler

    def scrape(self, filename):
        output_file_path = self._get_output_file_path_for(filename)
        count = 0
        try:
            with open (filename, 'rb') as input_file:
                with open (output_file_path, 'wb') as output_file:
                    alumni_list = csv.reader (input_file, delimiter=',')
                    output_file_writer = csv.writer(output_file, delimiter=',')
                    for row in alumni_list:
                        alumni_name = row[0]
                        try:
                            # Necessary to keep scraper from blocking the IP
                            time.sleep(self._get_random_sleep_time())
                            #
                            links = self.search_handler.get_first10_search_results(alumni_name)
                            output_file_writer.writerow(links)
                            count += 1
                            print 'Scraping completed for {0} alumni'.format(count)
                        except IOError:
                            raise IOError("Scraper has been blocked by the search engine...")
                        except Exception as e:
                            print e.__doc__
                            print e.message
                            print 'Error occurred for alumni - {0}'.format(alumni_name)
        except Exception as e:
            print e.__doc__
            print e.message
            print 'Error occurred during scraping...'

    def _get_output_file_path_for(self, file):
        input_file_basename = os.path.splitext(file)[0]
        return (input_file_basename + '_output.csv')

    def _get_random_sleep_time(self):
        return random.randint(10, 15)