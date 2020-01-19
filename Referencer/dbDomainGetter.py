from SPARQLWrapper import SPARQLWrapper, JSON


class dbDomainGetter():

    def query_wikidata(self, domain, limit_articles_number=None):
        articles_list = []
        sparql = SPARQLWrapper("http://query.wikidata.org/sparql")
        query = """
            SELECT ?item ?domain ?article
            WHERE 
            {
              ?item wdt:P31 wd:%s .
              ?article schema:about ?item .
              ?article schema:isPartOf <https://en.wikipedia.org/> .
            }
        """ % (domain)
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
