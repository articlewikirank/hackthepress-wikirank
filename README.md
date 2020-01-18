<p align="center">
  <img height="200" src="logo 2.png">
</p>

WikiRank is a tool to rank reliability of news articles by using the frequency of Wikipedia citations from different sources on a topic as a proxy for reliability.

## How WikiRank works


1. **News article:** The user provides a news article for WikiRank to analyse
1. **Topic:** WikiRank performs a keyword extraction to define the topic or topics of the article
1. **Wikidata:** The user defines the Wikidata item for the topic based on suggestions, the Wikidata item links to Wikipedia article for the topic.
1. **Wikidata statements:** WikiRank uses Wikidata statements (e.g [instance of](https://www.wikidata.org/wiki/Property:P31) and [occupation](https://www.wikidata.org/wiki/Property:P106) to understand the context of the topic to form a 'topic domain'
1. **Wikipedia references:** WikiRank counts the number of citations from each news source in Wikipedia articles in the ‘topic domain’ to find the most used reference sources
