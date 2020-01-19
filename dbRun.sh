while read -r line; do
  python runDbRef.py $line
done < "domainList.txt"