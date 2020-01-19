from SPARQLWrapper import SPARQLWrapper, JSON
import requests
import json

class DomainGetter():

    def query_wikidata(self, entity, limit_articles_number=None):
        articles_list = []
        sparql = SPARQLWrapper("http://query.wikidata.org/sparql")
        query = """
            SELECT ?item ?domain ?article
            WHERE 
            {
              wd:%s wdt:P31 ?domain .
              ?item wdt:P31 ?domain .
              ?article schema:about ?item .
              ?article schema:isPartOf <https://en.wikipedia.org/> .
            }
        """ % (entity)
        if limit_articles_number:
            query += " LIMIT " + str(limit_articles_number)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        for result in results["results"]["bindings"]:
            articles_list.append(result["article"]["value"])
        return list(set(articles_list))

    def run(self, entity, limit_articles_number=None):
        article_list = self.query_wikidata(entity, limit_articles_number)
        return article_list

class EntityDomainGetter():

    def get_entity_from_keyword(self, keyword):
        url = "https://www.wikidata.org/w/api.php?action=wbsearchentities&language=en&format=json&limit=3&search=" + keyword
        req = requests.get(url)
        data = json.loads(req.text)
        entities = []
        for x in data['search']:
            print(x['label'])
            entities.append(x['id'])
        return entities

    def get_domain_for_entity(self, entity):
        url = 'http://www.wikidata.org/wiki/Special:EntityData/' + entity + '.json'
        req = requests.get(url)
        data = json.loads(req.text)
        domains = set()
        for x in data['entities'][entity]['claims']['P31']:
            domains.add(x['mainsnak']['datavalue']['value']['id'])
        return list(domains)

class EntityGetter():

    def get_entity_from_keyword(self, keyword):
        url = "https://www.wikidata.org/w/api.php?action=wbsearchentities&language=en&format=json&limit=3&search=" + keyword
        req = requests.get(url)
        data = json.loads(req.text)
        entities = []
        for x in data['search']:
            print(x['label'])
            entities.append(x['id'])
        return entities

    def run(self,keyword):
        return self.get_entity_from_keyword(keyword)
