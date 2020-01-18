from Referencer.ReferenceRanker import *
from Referencer.DomainCreator import *
from Referencer.TextExtractor import *

textextr = TextRank4Keyword()
entityget = EntityGetter()
domcre = DomainGetter()
refrank = RefRanker()

text = ''
with open('samplearticle.md') as infile:
    for line in infile:
        text += line.strip() + ' '

keywords = textextr.run(text, 2)

entities = []
for keyword in keywords:
    entities.append(entityget.run(keyword))

print(entities)

entity = entities[0][0]

list_of_articles = domcre.run(entity, 100)
print(refrank.run(list_of_articles))