<p align="center">
  <img height="200" src="logo 2.png">
</p>

WikiRank is a tool to rank reliability of news articles by using the frequency of Wikipedia citations from different sources on a topic as a proxy for reliability.

## How the tool works


1. **News article:** The user provides a news article for the tool to analyse
1. **Topic:** Perform keyword extraction to define the topic of the article |
1. **Wikidata:** User defines the Wikidata item for the topic based on suggestions, the Wikidata item which links to Wikipedia articles
1. **Wikidata statements:** The tool uses Wikidata statements (e.g instance of and occupation to understand the context of the topic to form a Domain
1. **Wikipedia references:** Count the number of citations from each news source in Wikipedia articles in the ‘Domain’ to find the most used reference sources
