# Run this script from this dir -- it downloads files here.

# Data sets from: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HG7NV7
# Data dictionary: http://stat-computing.org/dataexpo/2009/the-data.html

set -x

for yr in 2005 2006 2007; do
  curl --output datasets/$yr.csv.bz2 --create-dirs http://stat-computing.org/dataexpo/2009/$yr.csv.bz2
  bunzip2 ./datasets/$yr.csv.bz2
done

