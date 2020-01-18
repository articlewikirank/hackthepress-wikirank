from SPARQLWrapper import SPARQLWrapper, JSON

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
