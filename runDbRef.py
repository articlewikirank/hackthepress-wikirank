from Referencer.dbDomainGetter import *
from Referencer.dbRefRanker import *
import json, sys, os

if len(sys.argv) < 2:
    print("usage runDbRef.py <domain id>")
    exit(0)

dir = "dbData"
if not os.path.exists(dir):
    os.mkdir(dir)

dbdomcre = dbDomainGetter()
domain = sys.argv[1]

list_of_articles = dbdomcre.run(domain, 50)
print(list_of_articles)

dbRef = dbRefRanker()
ref_counts = dbRef.run(list_of_articles)
print(ref_counts)
dictRefCounts = { i : ref_counts[i] for i in ref_counts }

data = {domain:dictRefCounts}
content = json.dumps(data, sort_keys=True, indent=4)

f = open("dbData/" +domain+ ".json", "w")
f.write(content)
f.close

