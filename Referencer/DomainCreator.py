from SPARQLWrapper import SPARQLWrapper, JSON
import requests
import json

class DomainGetter():
    """" Get a list of articles for a domain of a given entity
    """

    def query_wikidata(self, entity, limit_articles_number=None):
        """ Query Wikidata to get a list of articles in the domain of the given entity
        :param entity: Entity ID for which we look the domain up in the form "Q123"
        :param limit_articles_number: Limit the number of articles that are returned from the SPARQL request (optional)
        :return: Return a list of articles in English Wikipedia in the domain
        """
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
    """ Get a domain for a given entity, based on a keyword
    """

    def get_entity_from_keyword(self, keyword):
        """ Given a keyword, get the respective Wikidata entity ID
        :param keyword: Keyword string
        :return: List of entities matching the keyword
        """
        url = "https://www.wikidata.org/w/api.php?action=wbsearchentities&language=en&format=json&limit=3&search=" + keyword
        req = requests.get(url)
        data = json.loads(req.text)
        entities = []
        for x in data['search']:
            print(x['label'])
            entities.append(x['id'])
        return entities

    def get_domain_for_entity(self, entity):
        """ Get a domain for a given entity ID
        :param entity: entity ID in the format "Q123"
        :return: return a list of domains through the Wikidata API
        """
        url = 'http://www.wikidata.org/wiki/Special:EntityData/' + entity + '.json'
        req = requests.get(url)
        data = json.loads(req.text)
        domains = set()
        for x in data['entities'][entity]['claims']['P31']:
            domains.add(x['mainsnak']['datavalue']['value']['id'])
        return list(domains)

    def run(self, keyword):
        entity = self.get_entity_from_keyword(keyword)
        return self.get_domain_for_entity(entity)

class EntityGetter():
    """ For a given keyword, return an entity ID
    """

    def get_entity_from_keyword(self, keyword):
        """ Get an entity ID based on label match through Wikidata API
        :param keyword: Keyword as string
        :return: Entity ID in the form "Q123"
        """
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
