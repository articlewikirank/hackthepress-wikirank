from Referencer.ReferenceRanker import *
from Referencer.DomainCreator import *

domcre = DomainGetter()
refrank = RefRanker()

list_of_articles = domcre.run('Q64', 100)
print(refrank.run(list_of_articles))