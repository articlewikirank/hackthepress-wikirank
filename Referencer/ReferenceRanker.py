import urllib.request
import json
from bs4 import BeautifulSoup
from urllib.parse import urlparse

class RefRanker():

    def get_pages(self, title, lang_code):
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
        reference_data = {}
        for article in list_of_articles:
            #title = link.replace('https://' + lang_code + '.wikipedia.org/wiki/', '')
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

        return counted_data

    def run(self, list_of_articles, lang_code='en'):
        reference_data = self.get_full_references(list_of_articles, lang_code)
        return self.get_sorted_references(reference_data)


