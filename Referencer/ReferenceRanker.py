import urllib.request
import json
from bs4 import BeautifulSoup
from urllib.parse import urlparse

class RefRanker():
    """ Class to rank references based on their occurance on Wikipedia
    """

    def get_pages(self, title, lang_code):
        """ Get Wikipedia pages (based on language code) with a given title
        :param title: Title of a Wikipedia page
        :param lang_code: Language code for the Wikipedia
        :return: List of reference sections
        """
        reference_sections = []
        link = 'https://' + lang_code + '.wikipedia.org/api/rest_v1/page/mobile-sections/' + title
        try:
            with urllib.request.urlopen(link) as url:
                page_data = json.loads(url.read().decode())
                for ref_sec in page_data['remaining']['sections']:
                    if 'isReferenceSection' in ref_sec and ref_sec['isReferenceSection']:
                        reference_sections.append(ref_sec['text'].strip().replace('\n', ''))
        except:
            print('NOOOOOO ----->' + link)
            return None
        return reference_sections

    # mw-references
    # mw:ExtLink
    def get_full_references(self, list_of_articles, lang_code):
        """ Get the parsed reference based on a list of articles
        :param list_of_articles: List of articles on Wikipedia
        :param lang_code: Language code for the Wikipedia
        :return: references, parsed
        """
        reference_data = {}
        for link in list_of_articles:
            article = link.replace('https://' + lang_code + '.wikipedia.org/wiki/', '')
            pages = self.get_pages(article, lang_code)
            if not pages:
                continue
            for page in pages:
                soup = BeautifulSoup(page, "html.parser")
                for a in soup.find_all('a', {'rel': 'mw:ExtLink'}):
                    if article in reference_data:
                        reference_data[article].append(a.get('href'))
                    else:
                        reference_data[article] = [a.get('href')]
        return reference_data

    def get_sorted_references(self, full_reference_data):
        """
        :param full_reference_data: Full reference data by article
        :return: Reference data counted and sorted
        """
        counted_data = {}
        for page, references in full_reference_data.items():
            for ref in references:
                link = urlparse(ref).netloc.replace('www.', '')
                if link in counted_data:
                    counted_data[link] += 1
                else:
                    counted_data[link] = 1
        counted_data_sorted = {}

        for k in sorted(counted_data, key=counted_data.get, reverse=True):
            counted_data_sorted[k] = counted_data[k]

        return counted_data_sorted

    def run(self, list_of_articles, lang_code='en'):
        print(list_of_articles)
        reference_data = self.get_full_references(list_of_articles, lang_code)
        return self.get_sorted_references(reference_data)


