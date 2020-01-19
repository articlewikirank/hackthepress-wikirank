<p align="center">
  <img height="100" src="WikiRank logo.png">
</p>

**WikiRank** is a multilingual tool to rank reliability of news articles by using the frequency of Wikipedia citations from different sources on a topic as a proxy for reliability. WikiRank reuses the work the work Wikipedia contributors have done in finding credible sources of information.

----

## How WikiRank works


1. **News article:** The user provides a news article for WikiRank to analyse.
1. **Topic:** WikiRank performs a keyword extraction to define the topics of the article.
1. **Wikidata:** WikiRank links the Wikidata item to the extracted topic.
1. **Wikidata statements:** WikiRank uses Wikidata statements (e.g [instance of](https://www.wikidata.org/wiki/Property:P31) and [occupation](https://www.wikidata.org/wiki/Property:P106) to understand the context of the topic to form a 'topic domain'
1. **Wikipedia references:** WikiRank counts the number of citations from each news source in Wikipedia articles in the ‘topic domain’ to find the most used reference sources for that topic.

----

**Made by:**

Lucie Kaffee&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reuben Thomas&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Alex Ma&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Alessandro Toppetti&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Erdinc Mutlu&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;John Cummings&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Kai Landolt


